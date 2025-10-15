# 📚 Course Lab Notebooks

This directory contains Jupyter notebooks from the **DeepLearning.AI Agentic AI Course**. These notebooks demonstrate various agentic AI design patterns and concepts.

---

## 📋 Notebook Overview

### Graded Assignments

| Notebook | Module | Focus Area | Key Concepts |
|----------|--------|------------|--------------|
| **C1M2_Assignment.ipynb** | Module 2 | Reflection in Research | • Draft-Reflect-Revise cycle<br>• Essay improvement workflow<br>• AISuite basics |
| **C1M3_Assignment.ipynb** | Module 3 | Tool Use & Reflection | • Research with external tools<br>• arXiv + Tavily integration<br>• HTML report generation |
| **C1M5_Assignment.ipynb** | Module 5 | Multi-Agent Workflows | • Planning agent<br>• Research-Writer-Editor pipeline<br>• Agent coordination |

### Ungraded Labs (UGL)

| Notebook | Module | Focus Area | Skills Developed |
|----------|--------|------------|------------------|
| **M2_UGL_1.ipynb** | Module 2 | SQL Query Generation | • Natural language to SQL<br>• Reflection with external feedback<br>• Query refinement (V1 → V2) |
| **M2_UGL_2.ipynb** | Module 2 | Chart Generation | • Code generation for matplotlib<br>• Visual reflection<br>• Iterative improvement |
| **M3_UGL_1.ipynb** | Module 3 | Functions as Tools | • Converting Python functions to LLM tools<br>• AISuite tool calling<br>• Multi-tool orchestration |
| **M3_UGL_2.ipynb** | Module 3 | Email Assistant | • Simulated email backend<br>• CRUD operations with tools<br>• Natural language commands |
| **M4_UGL_1.ipynb** | Module 4 | Component Evaluation | • Evaluating research sources<br>• Preferred domain validation<br>• Objective metrics |
| **M5_UGL_1_R.ipynb** | Module 5 | Planning with Code | • Code as action pattern<br>• TinyDB for state management<br>• Sunglasses inventory system |
| **M5_UGL_2.ipynb** | Module 5 | Marketing Research Team | • Multi-agent collaboration<br>• Market research → Design → Copy<br>• Campaign report generation |

---

## 🚀 Getting Started

### Prerequisites

1. **Python Environment**: Python 3.8 or higher
2. **Dependencies**: Install from parent directory's `requirements.txt`
3. **API Keys**: Configure in `.env` file in parent directory

### Setup Instructions

**Step 1: Install Dependencies**

```bash
# From the project root directory
pip install -r ../requirements.txt
```

**Step 2: Configure API Keys**

Create a `.env` file in the **parent directory** (not in Course Lab Notebooks/):

```env
# Required API Keys
OPENAI_API_KEY=sk-...
TAVILY_API_KEY=tvly-...

# Optional Configuration
DLAI_TAVILY_BASE_URL=https://api.tavily.com
```

**Step 3: Start Jupyter**

```bash
# From Course Lab Notebooks directory
jupyter notebook
```

Or from project root:

```bash
jupyter notebook "Course Lab Notebooks/"
```

---

## 📝 Using the Notebooks

### Importing Project Modules

Many notebooks need to import from the parent `src/` directory. Add this cell at the top of any notebook:

```python
# Setup imports from parent src/ directory
import sys
sys.path.append('..')

# Now you can import project modules
from src.agents import research_agent, writer_agent, editor_agent
from src.research_tools import arxiv_search_tool, tavily_search_tool, wikipedia_search_tool
from src.planning_agent import planner_agent, executor_agent_step
```

**Or use the helper script**:

```python
# Alternative: Use the setup script
import setup_imports  # This adds parent directory to path
from src.agents import research_agent
```

### Common Imports Pattern

Most notebooks follow this import pattern:

```python
# Standard library
import json
from datetime import datetime

# Third-party
from dotenv import load_dotenv
import aisuite as ai
from IPython.display import display, HTML, Markdown

# Load environment variables
load_dotenv(dotenv_path='../.env')  # Load from parent directory

# Create AISuite client
client = ai.Client()
```

---

## 🎯 Learning Paths

### Beginner Path

Start with these notebooks in order:

1. **C1M2_Assignment.ipynb** - Learn basic reflection pattern
2. **M3_UGL_1.ipynb** - Understand tool calling
3. **C1M3_Assignment.ipynb** - Combine tools with reflection
4. **C1M5_Assignment.ipynb** - Multi-agent workflows

### Intermediate Path

Focus on specialized applications:

1. **M2_UGL_1.ipynb** - SQL generation with feedback
2. **M2_UGL_2.ipynb** - Data visualization agents
3. **M3_UGL_2.ipynb** - Email automation
4. **M4_UGL_1.ipynb** - Component-level evaluation

### Advanced Path

Explore complex multi-agent systems:

1. **M5_UGL_1_R.ipynb** - Code execution and planning
2. **M5_UGL_2.ipynb** - Full marketing team simulation
3. **C1M5_Assignment.ipynb** - Custom agent pipelines

---

## 🔧 Troubleshooting

### Import Errors

**Problem**: `ModuleNotFoundError: No module named 'src'`

**Solution**: Add parent directory to Python path:
```python
import sys
sys.path.append('..')
```

---

### API Key Errors

**Problem**: `OPENAI_API_KEY not found`

**Solution**: Ensure `.env` file is in the **parent directory** and load it:
```python
from dotenv import load_dotenv
load_dotenv(dotenv_path='../.env')
```

---

### Tool Call Errors

**Problem**: `Tool 'arxiv_search_tool' not found`

**Solution**: Import and pass tools correctly:
```python
from src.research_tools import arxiv_search_tool, tavily_search_tool

tools = [arxiv_search_tool, tavily_search_tool]

response = client.chat.completions.create(
    model="openai:gpt-4.1",
    messages=messages,
    tools=tools,
    tool_choice="auto",
    max_turns=5
)
```

---

### Rate Limiting

**Problem**: `RateLimitError` from OpenAI

**Solutions**:
- Add delays between requests: `time.sleep(1)`
- Use cheaper models: `gpt-4.1-mini` instead of `gpt-4.1`
- Reduce `max_results` in tool calls
- Monitor API usage at <a href="https://platform.openai.com/usage" target="_blank">OpenAI Dashboard</a>

---

## 📚 Key Concepts by Module

### Module 2: Reflection

**Core Idea**: Agents review and improve their own outputs

**Pattern**:
```
V1 (Initial) → Reflection (Critique) → V2 (Improved)
```

**Notebooks**: C1M2_Assignment, M2_UGL_1, M2_UGL_2

---

### Module 3: Tool Use

**Core Idea**: Extend agent capabilities with external functions

**Pattern**:
```
User Query → Agent selects tools → Execute tools → Agent synthesizes
```

**Notebooks**: C1M3_Assignment, M3_UGL_1, M3_UGL_2

---

### Module 4: Evaluation

**Core Idea**: Systematic quality assessment of agent outputs

**Patterns**:
- Component-level evaluation
- Objective metrics with ground truth
- Domain-specific validation

**Notebooks**: M4_UGL_1

---

### Module 5: Multi-Agent Systems

**Core Idea**: Specialized agents collaborate on complex tasks

**Pattern**:
```
Planner → Agent 1 → Agent 2 → Agent 3 → Final Output
            ↓           ↓           ↓
         Context    Context    Context
```

**Notebooks**: C1M5_Assignment, M5_UGL_1_R, M5_UGL_2

---

## 🎓 Additional Resources

- **Course Forum**: <a href="https://community.deeplearning.ai/c/course-q-a/agentic-ai/567" target="_blank">DeepLearning.AI Community</a>
- **AISuite Docs**: <a href="https://github.com/andrewyng/aisuite" target="_blank">GitHub Repository</a>
- **OpenAI API**: <a href="https://platform.openai.com/docs" target="_blank">API Documentation</a>
- **Tavily API**: <a href="https://tavily.com/docs" target="_blank">Search API Docs</a>

---

## 💡 Best Practices

### 1. Always Load Environment Variables

```python
from dotenv import load_dotenv
load_dotenv(dotenv_path='../.env')
```

### 2. Use Appropriate Models

- **Planning**: `o4-mini` (strong reasoning)
- **Research**: `gpt-4.1` (complex queries)
- **Writing**: `gpt-4.1-mini` (cost-effective)

### 3. Set Reasonable Token Limits

```python
response = client.chat.completions.create(
    model="openai:gpt-4.1-mini",
    messages=messages,
    max_tokens=4000,  # Prevent runaway costs
    temperature=0.7
)
```

### 4. Handle Errors Gracefully

```python
try:
    result = tool_function(query)
except Exception as e:
    print(f"Tool error: {e}")
    result = {"error": str(e)}
```

### 5. Clean Up Resources

```python
# Close database connections
db.close()

# Clear large variables
del large_dataframe
import gc
gc.collect()
```

---

## 🔄 Notebook Workflow

### Typical Notebook Structure

1. **Imports & Setup**: Load libraries, configure environment
2. **Tool Definitions**: Define or import external tools
3. **Agent Functions**: Create agent logic
4. **Example Execution**: Run sample queries
5. **Experimentation**: Modify and test variations
6. **Cleanup**: Display results, save outputs

### Example Notebook Flow

```python
# 1. Setup
import sys
sys.path.append('..')
from src.agents import research_agent
from dotenv import load_dotenv
load_dotenv(dotenv_path='../.env')

# 2. Execute
result = research_agent("Your query here")

# 3. Display
from IPython.display import Markdown
display(Markdown(result))

# 4. Save (optional)
with open('output.md', 'w') as f:
    f.write(result)
```

---

## 📊 Notebook Statistics

| Category | Count | Total Cells (approx) |
|----------|-------|---------------------|
| Graded Assignments | 3 | ~60 cells |
| Ungraded Labs | 7 | ~140 cells |
| **Total** | **10 notebooks** | **~200 cells** |

**Estimated Completion Time**: 8-12 hours total

---

## ✅ Completion Checklist

Use this checklist to track your progress:

- [ ] C1M2_Assignment - Reflection in Research Agent
- [ ] M2_UGL_1 - SQL Query Generation with Reflection
- [ ] M2_UGL_2 - Chart Generation with Visual Reflection
- [ ] C1M3_Assignment - Tool Use and Reflective Agents
- [ ] M3_UGL_1 - Turning Functions into Tools
- [ ] M3_UGL_2 - Email Assistant Workflow
- [ ] M4_UGL_1 - Component-level Evaluation
- [ ] C1M5_Assignment - Agentic Workflows
- [ ] M5_UGL_1_R - Customer Service with Code Planning
- [ ] M5_UGL_2 - Multi-Agent Marketing Research Team

---

## 🤝 Contributing

Found an issue or improvement? Contributions are welcome!

1. Test your changes in a clean environment
2. Ensure all notebooks run without errors
3. Update this README if adding new notebooks
4. Follow existing code style and patterns

---

**Last Updated**: October 15, 2024  
**Course**: DeepLearning.AI - Agentic AI  
**Status**: Complete ✅

