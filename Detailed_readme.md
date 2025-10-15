# 🤖 Agentic AI Research System

> **Automated Academic Research & Report Generation powered by Multi-Agent AI**

**What this does in 30 seconds:**  
You enter a research query → System generates a 2400+ word academic report with citations → Takes 2-5 minutes → Costs $0.05-0.10 per report.

---

## 🚀 5-Minute Quick Start

### Step 1: Get API Keys (2 minutes)

```bash
# Get these first - you'll need them immediately:
1. OpenAI API Key: https://platform.openai.com/api-keys
   - Click "Create new secret key"
   - Copy it immediately (you won't see it again)
   - Cost: ~$0.05-0.10 per report

2. Tavily API Key: https://tavily.com
   - Sign up (free tier available)
   - Copy API key from dashboard
```

### Step 2: Install (2 minutes)

```bash
# Clone and setup
git clone <repo-url>
cd agentic-ai-public
python -m venv venv

# Windows:
venv\Scripts\activate

# Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

**⚠️ CRITICAL:** If `pip install` fails with PostgreSQL errors:
```bash
# Windows: Install PostgreSQL from https://www.postgresql.org/download/
# Or use SQLite instead (see troubleshooting below)

# Mac:
brew install postgresql

# Linux:
sudo apt-get install postgresql postgresql-contrib
```

### Step 3: Configure (1 minute)

Create `.env` file in project root:

```env
# REQUIRED - Get these first!
OPENAI_API_KEY=sk-proj-xxxxxxxxxxxxxxxxxx
TAVILY_API_KEY=tvly-xxxxxxxxxxxxxxxx

# For Tavily (use this exact URL)
DLAI_TAVILY_BASE_URL=https://api.tavily.com

# DATABASE - Choose ONE option:

# Option A: Local PostgreSQL (recommended for production)
DATABASE_URL=postgresql://postgres:yourpassword@localhost:5432/agentic_ai

# Option B: SQLite (easier for testing, no install needed)
DATABASE_URL=sqlite:///./agentic_ai.db
```

**🚨 Common Mistake:** Don't use `postgres://` - use `postgresql://`!

### Step 4: Run (<1 minute)

```bash
# Start server
uvicorn main:app --reload

# Open browser
http://localhost:8000

# Enter query like:
"Research quantum computing applications in cryptography. 
Include recent developments, key challenges, and future prospects."

# Wait 2-5 minutes → Get your report!
```

---

## ⚠️ What Can Go Wrong (Troubleshooting First!)

### Problem 1: `ModuleNotFoundError: No module named 'aisuite'`

**Fix:**
```bash
# Make sure virtual environment is activated
# Windows: Look for "(venv)" in your prompt
# Then:
pip install --upgrade pip
pip install -r requirements.txt
```

---

### Problem 2: `DATABASE_URL not set` or Connection Errors

**Quick Fix (Use SQLite):**
```bash
# In .env file, use:
DATABASE_URL=sqlite:///./agentic_ai.db

# Restart server
```

**Proper Fix (PostgreSQL):**
```bash
# 1. Install PostgreSQL
# Windows: https://www.postgresql.org/download/windows/
# Mac: brew install postgresql
# Linux: sudo apt-get install postgresql

# 2. Create database
createdb agentic_ai

# 3. Set DATABASE_URL in .env:
DATABASE_URL=postgresql://postgres:yourpassword@localhost:5432/agentic_ai
```

---

### Problem 3: `OPENAI_API_KEY not found`

**Fix:**
```bash
# 1. Check .env file exists in project root (same folder as main.py)
# 2. Check no spaces around = sign:
#    ✅ CORRECT: OPENAI_API_KEY=sk-...
#    ❌ WRONG: OPENAI_API_KEY = sk-...
# 3. Restart server after editing .env
```

---

### Problem 4: `RateLimitError` from OpenAI

**What happened:** You're hitting API rate limits

**Fix:**
```python
# Check your usage: https://platform.openai.com/usage

# If you're on free tier ($5 credit):
# - Each report costs $0.05-0.10
# - You can generate ~50-100 reports total

# Solutions:
# 1. Add payment method at https://platform.openai.com/account/billing
# 2. Wait for rate limit to reset (usually 1 minute)
# 3. Use smaller queries to reduce token usage
```

---

### Problem 5: Takes Forever / Hangs

**Expected:** 2-5 minutes per report  
**If longer:** Check these:

```bash
# 1. Is it really stuck? Check task progress:
http://localhost:8000/task_progress/YOUR_TASK_ID

# 2. Check server logs for errors
# Look for "ERROR" or "timeout" messages

# 3. Common causes:
# - arXiv PDF download timeout (it downloads full PDFs)
# - Tavily API slow response
# - LLM generating very long output

# 4. Restart and try simpler query:
"Research machine learning basics"
```

---

## 🏗️ How It Actually Works (The Real Flow)

### The Architecture You Need to Understand

![Complete Architecture](improved_architecture_flowchart.png)

**Key Insight #1: SEQUENTIAL, not Parallel**
```
User Query 
  → Planning Agent (10-20s) 
    → Research Agent (20-60s) 
      → Writer Agent (30-90s) 
        → Editor Agent (20-60s) 
          → Final Report

Total: 2-5 minutes
```

**Key Insight #2: The EXECUTOR Agent (Missing from Most Docs!)**
```python
# This is the actual orchestrator that runs everything:
executor_agent_step(
    step_title="Research agent: Use Tavily...",
    history=[previous_outputs],  # ← This is how context flows!
    prompt=original_user_query
)

# It enriches each step with context from ALL previous steps
# That's why the Writer knows what the Researcher found
```

**Key Insight #3: Tool Calling is THE Magic**
```python
response = client.chat.completions.create(
    model="openai:gpt-4.1",
    messages=messages,
    tools=[tavily_search_tool, arxiv_search_tool, wikipedia_search_tool],
    tool_choice="auto",     # ← LLM decides which tools to use
    max_turns=5,            # ← Can call tools up to 5 times in one request!
    temperature=0           # ← Deterministic for reproducibility
)

# What happens:
# 1. LLM: "I need to search arXiv for 'quantum computing'"
# 2. System: Downloads PDF, extracts 5000 chars of text
# 3. LLM: "Now I have data, let me synthesize..."
# 4. System: Returns final answer with sources
```

**Key Insight #4: Threading Model**
```
Main Thread (FastAPI)                Background Thread
     │                                       │
     ├─ Receives POST /generate_report      │
     ├─ Creates task in DB                  │
     ├─ Spawns background thread ──────────>│
     ├─ Returns task_id immediately         ├─ Runs planner_agent
     │                                      ├─ Runs executor_agent
     ├─ Handles GET /task_progress          │   ├─ Research
     ├─ (poll every 2 seconds)              │   ├─ Writer
     │<──────────────────────────────────   │   ├─ Editor
     ├─ Returns progress updates            │   └─ Saves to DB
     │                                      │
     └─ Returns final report                └─ Thread completes
```

---

## 💡 Understanding the Agents (What Each One Actually Does)

### Planning Agent (`src/planning_agent.py`)

**What it does:** Breaks your query into 7 executable steps

**Input Example:**
```python
"Research quantum computing applications"
```

**Output Example:**
```python
[
  "Research agent: Use Tavily to perform broad web search...",
  "Research agent: For each item, search arXiv for matching papers...",
  "Research agent: Synthesize and rank findings...",
  "Writer agent: Draft structured outline...",
  "Editor agent: Review for coherence...",
  "Writer agent: Generate final Markdown report with citations..."
]
```

**Why it matters:** Without this, agents would run randomly!

**Model:** `o4-mini` (reasoning model, not just text generation)

---

### Research Agent (`src/agents.py`)

**What it does:** Gathers information from 3 sources in one call

**The Magic:** `max_turns=5` means it can do this:
```
Turn 1: LLM decides "Search Tavily for general info"
        → Tavily returns 5 web results
Turn 2: LLM decides "Now search arXiv for academic papers"  
        → arXiv returns 3 papers + downloads PDFs + extracts text (5000 chars each)
Turn 3: LLM decides "Get Wikipedia background"
        → Wikipedia returns article summary
Turn 4: LLM decides "I have enough data, synthesizing..."
        → Returns comprehensive findings
```

**Output Example:**
```markdown
# Research Findings

## Web Sources (Tavily)
1. "Quantum Computing Breakthrough" - Nature.com
   - Key points...
   - URL: https://...

## Academic Papers (arXiv)
1. "Quantum Error Correction" (2024)
   - Authors: Smith et al.
   - Summary: [First 5000 chars of actual PDF]
   - arXiv:2401.12345

## Background (Wikipedia)
- Quantum computing is...
```

**Models:** `gpt-4.1-mini` (cost-effective) or `gpt-4.1` (more powerful)

**Time:** 20-60 seconds (PDF downloads are slow!)

---

### Writer Agent (`src/agents.py`)

**What it does:** Writes 2400+ word academic reports

**Structure it follows:**
```markdown
# Title

## Abstract (100-150 words)

## Introduction
- Context
- Research question
- Significance

## Background/Literature Review
- Existing work
- Theoretical framework

## Methodology (if applicable)
- Research approach
- Data sources

## Key Findings/Results
- Main outcomes
- Evidence

## Discussion
- Interpretation
- Implications
- Limitations

## Conclusion
- Summary
- Future directions

## References
[1] Author et al. (2024). Title. URL
[2] ...
```

**Citation Style:**
```markdown
Recent studies [1, 2] show that quantum computing...

## References
[1] Smith, J. (2024). Quantum Error Correction. 
    https://arxiv.org/abs/2401.12345
[2] Nature.com. (2024). Quantum Breakthrough.
    https://nature.com/articles/...
```

**Model:** `gpt-4.1-mini` (temperature=0 for consistency)

**Time:** 30-90 seconds

---

### Editor Agent (`src/agents.py`)

**What it does:** Reviews and improves the draft

**Changes it makes:**
- ✅ Strengthens thesis statements
- ✅ Clarifies complex concepts
- ✅ Improves sentence flow
- ✅ Fixes awkward phrasing
- ✅ Standardizes terminology
- ✅ **Preserves all citations** (critical!)

**Model:** `gpt-4.1-mini` (temperature=0)

**Time:** 20-60 seconds

---

## 📊 Cost & Performance Reality Check

### What One Report Actually Costs

```
Research Agent:     ~5,000 tokens input  + ~3,000 output  = $0.02
Writer Agent:       ~3,000 tokens input  + ~4,000 output  = $0.02
Editor Agent:       ~4,000 tokens input  + ~4,000 output  = $0.02
-------------------------------------------------------------------
Total:              ~15,000-20,000 tokens                 = $0.05-0.10

With arXiv PDF extraction: Add ~$0.01-0.02
With multiple iterations: Add ~$0.02-0.05
```

### What Time Really Looks Like

| Phase | Time | Why |
|-------|------|-----|
| Planning | 10-20s | o4-mini is slower (reasoning model) |
| Research | 20-60s | PDF downloads + text extraction |
| Writing | 30-90s | Generating 2400+ words |
| Editing | 20-60s | Reviewing + improving |
| **Total** | **2-5 min** | **Can't be faster (API latency)** |

### Token Limits You'll Hit

```python
# Context window: 128K tokens
# What this means in practice:

✅ Can handle: ~200 pages of text input
✅ Can handle: 3-5 long research papers
✅ Can handle: 50-100 web articles

❌ Will fail: Trying to process entire books
❌ Will fail: 100+ research papers in one query
❌ Will fail: Queries requiring >128K tokens of context
```

---

## 🎯 Using Notebooks (The Import Problem Everyone Has)

### The Problem

```python
# In Course Lab Notebooks/some_notebook.ipynb
from src.agents import research_agent  # ← This FAILS!
# ModuleNotFoundError: No module named 'src'
```

### The Solution (Choose One)

**Option 1: Add to every notebook** (recommended)
```python
# Cell 1 of your notebook
import sys
sys.path.append('..')  # Go up one directory to project root

# Now imports work:
from src.agents import research_agent, writer_agent, editor_agent
from src.research_tools import arxiv_search_tool
```

**Option 2: Use the helper**
```python
# Cell 1
import setup_imports  # Automatically adds parent to path

# Cell 2
from src.agents import research_agent
```

**Option 3: Run from project root**
```bash
# Instead of:
cd "Course Lab Notebooks"
jupyter notebook

# Do this:
jupyter notebook "Course Lab Notebooks/C1M2_Assignment.ipynb"
```

---

## 🔧 Advanced Configuration

### Using Different Models

```python
# In src/planning_agent.py, line 27:
def planner_agent(topic: str, model: str = "openai:o4-mini"):
    # Change to:
    model: str = "openai:gpt-4.1"  # More expensive but sometimes better

# In src/agents.py, line 15:
def research_agent(prompt: str, model: str = "openai:gpt-4.1-mini"):
    # Change to:
    model: str = "openai:gpt-4.1"  # Better at complex research

# Cost comparison:
# gpt-4.1-mini:  $0.15/1M input, $0.60/1M output  (cheap)
# gpt-4.1:       $3.00/1M input, $15.00/1M output (expensive)
# o4-mini:       $1.00/1M input, $4.00/1M output  (reasoning)
```

### Changing Report Length

```python
# In src/agents.py, line 158:
def writer_agent(
    prompt: str,
    model: str = "openai:gpt-4.1-mini",
    min_words_total: int = 2400,       # ← Change this
    min_words_per_section: int = 400,  # ← And this
):
    # Example: Shorter reports
    min_words_total: int = 1200,       # ~5 pages
    min_words_per_section: int = 200,  # Shorter sections
```

### Adjusting Tool Behavior

```python
# In src/research_tools.py, line 147:
_INCLUDE_PDF       = True   # Set False to skip PDF downloads
_EXTRACT_TEXT      = True   # Set False to use abstracts only
_MAX_PAGES         = 6      # Increase for more text (slower!)
_TEXT_CHARS        = 5000   # Characters to extract per paper
_SLEEP_SECONDS     = 1.0    # Delay between arXiv requests
```

---

## 📚 Project Structure (Where Everything Lives)

```
agentic-ai-public/
│
├── main.py                    ← START HERE: FastAPI server
│   ├── POST /generate_report  ← Creates tasks
│   ├── GET /task_progress     ← Polling endpoint
│   └── GET /task_status       ← Gets final result
│
├── .env                       ← PUT YOUR API KEYS HERE
│   ├── OPENAI_API_KEY=...
│   ├── TAVILY_API_KEY=...
│   └── DATABASE_URL=...
│
├── src/
│   ├── planning_agent.py      ← Creates plan (7 steps max)
│   │   └── planner_agent()    ← Uses o4-mini
│   │
│   ├── agents.py              ← The 3 main agents
│   │   ├── research_agent()   ← Gathers info (tools)
│   │   ├── writer_agent()     ← Writes report (2400+ words)
│   │   └── editor_agent()     ← Reviews & improves
│   │
│   └── research_tools.py      ← Tool implementations
│       ├── tavily_search_tool()    ← Web search
│       ├── arxiv_search_tool()     ← Academic papers + PDF
│       └── wikipedia_search_tool() ← Encyclopedia
│
├── templates/
│   └── index.html             ← Web UI (JavaScript polling)
│
├── Course Lab Notebooks/      ← Learning materials
│   ├── setup_imports.py       ← Import helper
│   └── *.ipynb                ← 10 notebooks
│
└── requirements.txt           ← Dependencies (pip install)
```

---

## 🎓 Model Comparison (Which One to Use)

| Model | Use For | Speed | Cost | Quality | When to Choose |
|-------|---------|-------|------|---------|----------------|
| **o4-mini** | Planning | Slow (10-20s) | Medium | Excellent reasoning | Default for planner |
| **gpt-4.1** | Research/Writing | Medium (5-10s) | High | Best | Complex queries, important reports |
| **gpt-4.1-mini** | Research/Writing/Editing | Fast (3-5s) | Low | Good | Default, cost-effective |
| **gpt-3.5-turbo** | Not recommended | Fast | Very Low | Poor | Only for testing |

**Rule of thumb:**
- **Prototyping/Testing:** Use gpt-4.1-mini everywhere
- **Production:** Use o4-mini (planning) + gpt-4.1-mini (others)
- **High Quality Needed:** Use gpt-4.1 for writer/editor
- **Budget Constrained:** Use gpt-4.1-mini everywhere, but expect lower quality

---

## 🆘 Common Questions (FAQ)

### Q: Can I use Claude or Gemini instead of OpenAI?

**A:** Yes! AISuite supports multiple providers:
```python
# In agents.py, change:
model="openai:gpt-4.1-mini"
# To:
model="anthropic:claude-3-5-sonnet-20241022"  # Claude
model="google:gemini-1.5-pro"                 # Gemini

# But you'll need to:
# 1. Install the provider: pip install anthropic
# 2. Add API key to .env: ANTHROPIC_API_KEY=...
# 3. Test thoroughly (different models behave differently)
```

---

### Q: Why does arXiv sometimes fail?

**A:** Several reasons:
1. **Domain limitation:** arXiv only covers CS, Math, Physics, etc.
   - ❌ Won't work: "Research marketing strategies"
   - ✅ Will work: "Research neural networks"

2. **PDF download timeout:** Some papers are large (>50MB)
   - Solution: Reduce `_MAX_PAGES` in research_tools.py

3. **Rate limiting:** Too many requests too fast
   - Solution: Increase `_SLEEP_SECONDS` to 2.0

---

### Q: Can I run this without PostgreSQL?

**A:** Yes! Use SQLite:
```env
# In .env:
DATABASE_URL=sqlite:///./agentic_ai.db
```
**Limitations:**
- ✅ Works fine for testing/development
- ✅ No install needed
- ❌ Not recommended for production (concurrent writes can fail)
- ❌ Can't deploy to some cloud platforms (Heroku needs PostgreSQL)

---

### Q: How do I make it faster?

**A:** You can't make it much faster due to API latency, but:
```python
# 1. Use faster models:
model="gpt-4.1-mini"  # Instead of gpt-4.1

# 2. Reduce tool calls:
max_results=3  # Instead of 5 for Tavily
_MAX_PAGES = 3  # Instead of 6 for arXiv

# 3. Shorter reports:
min_words_total: int = 1200  # Instead of 2400

# Realistic speedup: 3-4 minutes instead of 4-5 minutes
# You can't get below ~2 minutes due to sequential API calls
```

---

### Q: How do I deploy to production?

**A:** Heroku example:
```bash
# 1. Install Heroku CLI
# 2. Create app
heroku create your-app-name

# 3. Add PostgreSQL
heroku addons:create heroku-postgresql:mini

# 4. Set environment variables
heroku config:set OPENAI_API_KEY=sk-...
heroku config:set TAVILY_API_KEY=tvly-...

# 5. Deploy
git push heroku main

# 6. Run
heroku open
```

**Note:** main.py already handles Heroku's `postgres://` → `postgresql://` conversion!

---

## 📖 Learning Path

### Absolute Beginner
1. Read "5-Minute Quick Start" (top of README)
2. Run your first report
3. Read "How It Actually Works"
4. Try modifying a simple query

### Intermediate
1. Read "Understanding the Agents"
2. Try `Course Lab Notebooks/C1M2_Assignment.ipynb`
3. Modify `writer_agent()` to change report style
4. Experiment with different models

### Advanced
1. Read all agent code in `src/`
2. Complete all 10 notebooks
3. Add a new tool (e.g., Google Scholar)
4. Implement custom agent
5. Deploy to production

---

## 🎯 Success Checklist

Before asking for help, verify:

- [ ] Virtual environment is activated (`(venv)` in prompt)
- [ ] `.env` file exists in project root (same folder as `main.py`)
- [ ] API keys are set (no spaces around `=`)
- [ ] `pip install -r requirements.txt` completed successfully
- [ ] Database is accessible (PostgreSQL running OR using SQLite)
- [ ] Server starts without errors (`uvicorn main:app --reload`)
- [ ] You can access `http://localhost:8000` in browser
- [ ] You waited 2-5 minutes for first report (it's not broken!)

---

## 📞 Get Help

1. **Error in notebooks?** Check `Course Lab Notebooks/README.md`
2. **API errors?** Check OpenAI dashboard: https://platform.openai.com/usage
3. **Database errors?** Try SQLite first: `DATABASE_URL=sqlite:///./agentic_ai.db`
4. **Still stuck?** Include this info:
   - Error message (full traceback)
   - Your `.env` file (REMOVE API KEYS!)
   - Python version: `python --version`
   - OS: Windows/Mac/Linux

---

**Last Updated:** October 15, 2024  
**Version:** 2.0.0 (Improved)  
**Status:** Production Ready ✅

---

## 🎓 Why This README is Different

Most READMEs fail because they:
1. ❌ Assume you understand the architecture
2. ❌ Hide critical setup steps
3. ❌ Don't explain where things go wrong
4. ❌ Use abstract examples instead of real code
5. ❌ Don't show actual timing/costs

This README:
1. ✅ Shows you the REAL execution flow
2. ✅ Puts troubleshooting FIRST (where you'll spend time)
3. ✅ Explains the "why" not just the "what"
4. ✅ Includes actual code examples
5. ✅ Tells you what to expect (timing, cost, output)

**The #1 rule:** If you can't get it running in 5 minutes, the docs failed.

