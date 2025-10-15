"""
IMPROVED Agentic AI Research System Flowchart
- Shows actual execution sequence with swim lanes
- Includes timing, data formats, error paths
- Shows the missing EXECUTOR agent
- Clarifies threading model and polling
"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle, Polygon
import matplotlib.lines as mlines

# Create larger figure for more detail
fig, ax = plt.subplots(figsize=(20, 16))
ax.set_xlim(0, 14)
ax.set_ylim(0, 18)
ax.axis('off')

# Define color scheme
color_user = '#3B82F6'      # Blue - User/Frontend
color_main = '#6366F1'      # Indigo - Main Thread
color_bg = '#8B5CF6'        # Purple - Background Thread
color_planner = '#A855F7'   # Purple - Planning
color_executor = '#EC4899'  # Pink - Executor (MISSING IN ORIGINAL!)
color_research = '#10B981'  # Green - Research
color_writer = '#F59E0B'    # Orange - Writer
color_editor = '#EF4444'    # Red - Editor
color_db = '#06B6D4'        # Cyan - Database
color_tool = '#64748B'      # Gray - Tools
color_error = '#DC2626'     # Red - Error paths
color_success = '#059669'   # Green - Success

# === TITLE ===
ax.text(7, 17.5, 'Agentic AI Research System - COMPLETE Architecture', 
        ha='center', va='center', fontsize=22, fontweight='bold')
ax.text(7, 17.1, 'Showing Threading Model, Execution Sequence, Error Handling, and Data Flow', 
        ha='center', va='center', fontsize=11, style='italic', color='#64748B')

# === SWIM LANES ===
# User/Frontend Lane
ax.add_patch(Rectangle((0.2, 14.5), 13.6, 2.3, 
             edgecolor='#3B82F6', facecolor='#EFF6FF', alpha=0.3, linewidth=2))
ax.text(0.5, 16.6, 'USER / FRONTEND', fontsize=10, fontweight='bold', color='#1E40AF')

# Main Thread Lane
ax.add_patch(Rectangle((0.2, 12), 13.6, 2.2, 
             edgecolor='#6366F1', facecolor='#EDE9FE', alpha=0.3, linewidth=2))
ax.text(0.5, 13.9, 'MAIN THREAD (FastAPI)', fontsize=10, fontweight='bold', color='#4338CA')

# Background Thread Lane
ax.add_patch(Rectangle((0.2, 3.5), 13.6, 8.2, 
             edgecolor='#8B5CF6', facecolor='#FAF5FF', alpha=0.3, linewidth=2))
ax.text(0.5, 11.4, 'BACKGROUND THREAD (Agent Execution)', fontsize=10, fontweight='bold', color='#6B21A8')

# Database Lane
ax.add_patch(Rectangle((0.2, 1.8), 13.6, 1.4, 
             edgecolor='#06B6D4', facecolor='#CFFAFE', alpha=0.3, linewidth=2))
ax.text(0.5, 3, 'DATABASE (PostgreSQL)', fontsize=10, fontweight='bold', color='#0E7490')

# External APIs Lane
ax.add_patch(Rectangle((0.2, 0.2), 13.6, 1.3, 
             edgecolor='#64748B', facecolor='#F1F5F9', alpha=0.3, linewidth=2))
ax.text(0.5, 1.3, 'EXTERNAL APIs', fontsize=10, fontweight='bold', color='#334155')

# === 1. USER INPUT (Frontend Lane) ===
user_box = FancyBboxPatch((1, 15.2), 2.2, 0.9, boxstyle="round,pad=0.1", 
                          edgecolor=color_user, facecolor=color_user, alpha=0.4, linewidth=3)
ax.add_patch(user_box)
ax.text(2.1, 15.9, '①USER', ha='center', fontsize=11, fontweight='bold')
ax.text(2.1, 15.5, 'Enters query\n"Research X"', ha='center', fontsize=8)
ax.text(2.1, 15, '⏱️ 0s', ha='center', fontsize=7, style='italic', color='#64748B')

# === 2. POST REQUEST (Frontend Lane) ===
post_box = FancyBboxPatch((3.7, 15.2), 2.2, 0.9, boxstyle="round,pad=0.1", 
                          edgecolor=color_main, facecolor=color_main, alpha=0.3, linewidth=2)
ax.add_patch(post_box)
ax.text(4.8, 15.9, '② POST', ha='center', fontsize=11, fontweight='bold')
ax.text(4.8, 15.5, '/generate_report\n{prompt: "..."}', ha='center', fontsize=8)
ax.text(4.8, 15, '⏱️ <1s', ha='center', fontsize=7, style='italic', color='#64748B')

# Arrow 1 -> 2
ax.add_patch(FancyArrowPatch((3.2, 15.65), (3.7, 15.65),
             arrowstyle='->', mutation_scale=25, linewidth=2.5, color='black'))

# === 3. CREATE TASK (Main Thread) ===
create_box = FancyBboxPatch((3.7, 12.7), 2.2, 0.9, boxstyle="round,pad=0.1", 
                            edgecolor=color_db, facecolor=color_db, alpha=0.3, linewidth=2)
ax.add_patch(create_box)
ax.text(4.8, 13.4, '③ CREATE TASK', ha='center', fontsize=10, fontweight='bold')
ax.text(4.8, 13, 'DB.add(Task)\nstatus="running"', ha='center', fontsize=7)
ax.text(4.8, 12.8, '⏱️ <100ms', ha='center', fontsize=7, style='italic', color='#64748B')

# Arrow 2 -> 3
ax.add_patch(FancyArrowPatch((4.8, 15.2), (4.8, 13.6),
             arrowstyle='->', mutation_scale=25, linewidth=2.5, color='black'))

# === 4. LAUNCH BACKGROUND THREAD (Main Thread) ===
thread_box = FancyBboxPatch((6.4, 12.7), 2.4, 0.9, boxstyle="round,pad=0.1", 
                            edgecolor=color_bg, facecolor=color_bg, alpha=0.3, linewidth=2)
ax.add_patch(thread_box)
ax.text(7.6, 13.4, '④ SPAWN THREAD', ha='center', fontsize=10, fontweight='bold')
ax.text(7.6, 13, 'threading.Thread(\n  run_workflow)', ha='center', fontsize=7)
ax.text(7.6, 12.8, '⏱️ <10ms', ha='center', fontsize=7, style='italic', color='#64748B')

# Arrow 3 -> 4
ax.add_patch(FancyArrowPatch((5.9, 13.15), (6.4, 13.15),
             arrowstyle='->', mutation_scale=25, linewidth=2.5, color='black'))

# === 5. RETURN TASK_ID (Main Thread -> Frontend) ===
taskid_box = FancyBboxPatch((9.2, 12.7), 2.2, 0.9, boxstyle="round,pad=0.1", 
                            edgecolor=color_success, facecolor=color_success, alpha=0.3, linewidth=2)
ax.add_patch(taskid_box)
ax.text(10.3, 13.4, '⑤ RETURN', ha='center', fontsize=10, fontweight='bold')
ax.text(10.3, 13, '{"task_id":\n"uuid..."}', ha='center', fontsize=7)
ax.text(10.3, 12.8, '⏱️ <50ms', ha='center', fontsize=7, style='italic', color='#64748B')

# Arrow 4 -> 5
ax.add_patch(FancyArrowPatch((8.8, 13.15), (9.2, 13.15),
             arrowstyle='->', mutation_scale=25, linewidth=2.5, color='black'))

# === 6. POLLING LOOP (Frontend) ===
poll_box = FancyBboxPatch((11.7, 15.2), 2.2, 0.9, boxstyle="round,pad=0.1", 
                          edgecolor=color_user, facecolor=color_user, alpha=0.4, linewidth=3)
ax.add_patch(poll_box)
ax.text(12.8, 15.9, '⑥ POLL', ha='center', fontsize=11, fontweight='bold')
ax.text(12.8, 15.5, 'GET /task_progress\nEvery 2s', ha='center', fontsize=8)
ax.text(12.8, 15, '⏱️ 2-300s', ha='center', fontsize=7, style='italic', color='#64748B')

# Arrow 5 -> 6 (curved)
ax.add_patch(FancyArrowPatch((10.3, 13.6), (12.8, 15.2),
             arrowstyle='->', mutation_scale=25, linewidth=2, color='#3B82F6',
             connectionstyle="arc3,rad=.3"))

# === BACKGROUND THREAD EXECUTION ===

# 7. PLANNING AGENT
plan_box = FancyBboxPatch((1, 10.2), 2.5, 1.1, boxstyle="round,pad=0.1", 
                          edgecolor=color_planner, facecolor=color_planner, alpha=0.4, linewidth=3)
ax.add_patch(plan_box)
ax.text(2.25, 11, '⑦ PLANNER', ha='center', fontsize=11, fontweight='bold')
ax.text(2.25, 10.6, 'planner_agent(topic)\nModel: o4-mini\nReturns: List[steps]', ha='center', fontsize=7)
ax.text(2.25, 10.3, '⏱️ 10-20s', ha='center', fontsize=7, style='italic', color='#64748B')

# Arrow from thread spawn to planner
ax.add_patch(FancyArrowPatch((7.6, 12.7), (2.25, 11.3),
             arrowstyle='->', mutation_scale=25, linewidth=2.5, color='#8B5CF6'))

# 8. EXECUTOR AGENT (THE MISSING PIECE!)
exec_box = FancyBboxPatch((4, 10.2), 2.5, 1.1, boxstyle="round,pad=0.1", 
                          edgecolor=color_executor, facecolor=color_executor, alpha=0.4, linewidth=3)
ax.add_patch(exec_box)
ax.text(5.25, 11, '⑧ EXECUTOR', ha='center', fontsize=11, fontweight='bold', color='#BE185D')
ax.text(5.25, 10.6, '🔄 FOR each step:\n  execute with context\n  update progress', ha='center', fontsize=7)
ax.text(5.25, 10.3, '⏱️ Loops through', ha='center', fontsize=7, style='italic', color='#64748B')

# Arrow planner -> executor
ax.add_patch(FancyArrowPatch((3.5, 10.65), (4, 10.65),
             arrowstyle='->', mutation_scale=25, linewidth=2.5, color='black'))
ax.text(3.75, 10.9, 'steps[]', fontsize=7, ha='center', bbox=dict(boxstyle='round,pad=0.3', facecolor='white'))

# 9. RESEARCH AGENT
research_box = FancyBboxPatch((7, 10.2), 2.5, 1.1, boxstyle="round,pad=0.1", 
                              edgecolor=color_research, facecolor=color_research, alpha=0.4, linewidth=2)
ax.add_patch(research_box)
ax.text(8.25, 11, '⑨ RESEARCH', ha='center', fontsize=10, fontweight='bold')
ax.text(8.25, 10.6, 'Tools: Tavily+arXiv+Wiki\nmax_turns=5\ntool_choice="auto"', ha='center', fontsize=7)
ax.text(8.25, 10.3, '⏱️ 20-60s', ha='center', fontsize=7, style='italic', color='#64748B')

# Arrow executor -> research
ax.add_patch(FancyArrowPatch((6.5, 10.65), (7, 10.65),
             arrowstyle='->', mutation_scale=25, linewidth=2.5, color='black'))

# Tool calling detail box
tool_detail = FancyBboxPatch((7.2, 8.7), 2.1, 1.2, boxstyle="round,pad=0.05", 
                             edgecolor=color_tool, facecolor='white', alpha=0.9, linewidth=1, linestyle='dashed')
ax.add_patch(tool_detail)
ax.text(8.25, 9.7, 'Tool Calling Loop:', fontsize=8, ha='center', fontweight='bold')
ax.text(8.25, 9.4, '1. LLM picks tool\n2. Execute locally\n3. Return to LLM\n4. Repeat (max 5)', 
        ha='center', fontsize=6)

# 10-12. EXTERNAL TOOLS
tools_y = 0.6
# Tavily
ax.add_patch(FancyBboxPatch((1, tools_y), 1.8, 0.6, boxstyle="round,pad=0.05", 
             edgecolor=color_tool, facecolor=color_tool, alpha=0.3, linewidth=1))
ax.text(1.9, tools_y+0.45, '⑩ Tavily API', fontsize=8, fontweight='bold')
ax.text(1.9, tools_y+0.15, 'Web search (5 results)\n⏱️ 1-2s', ha='center', fontsize=6)

# arXiv  
ax.add_patch(FancyBboxPatch((3.3, tools_y), 1.8, 0.6, boxstyle="round,pad=0.05", 
             edgecolor=color_tool, facecolor=color_tool, alpha=0.3, linewidth=1))
ax.text(4.2, tools_y+0.45, '⑪ arXiv API', fontsize=8, fontweight='bold')
ax.text(4.2, tools_y+0.15, '+ PDF extract (5000char)\n⏱️ 5-15s/paper', ha='center', fontsize=6)

# Wikipedia
ax.add_patch(FancyBboxPatch((5.6, tools_y), 1.8, 0.6, boxstyle="round,pad=0.05", 
             edgecolor=color_tool, facecolor=color_tool, alpha=0.3, linewidth=1))
ax.text(6.5, tools_y+0.45, '⑫ Wikipedia', fontsize=8, fontweight='bold')
ax.text(6.5, tools_y+0.15, 'Article summary\n⏱️ ~1s', ha='center', fontsize=6)

# Arrows from research to tools
ax.add_patch(FancyArrowPatch((8.25, 10.2), (6.5, 1.2),
             arrowstyle='<->', mutation_scale=15, linewidth=1.5, color=color_tool, linestyle='dashed'))

# 13. WRITER AGENT
writer_box = FancyBboxPatch((10, 10.2), 2.5, 1.1, boxstyle="round,pad=0.1", 
                            edgecolor=color_writer, facecolor=color_writer, alpha=0.4, linewidth=2)
ax.add_patch(writer_box)
ax.text(11.25, 11, '⑬ WRITER', ha='center', fontsize=10, fontweight='bold')
ax.text(11.25, 10.6, 'Draft 2400+ words\nCitations [1], [2]\nAcademic structure', ha='center', fontsize=7)
ax.text(11.25, 10.3, '⏱️ 30-90s', ha='center', fontsize=7, style='italic', color='#64748B')

# Arrow research -> writer (DATA FLOW)
ax.add_patch(FancyArrowPatch((9.5, 10.65), (10, 10.65),
             arrowstyle='->', mutation_scale=25, linewidth=2.5, color='green', linestyle='dashed'))
ax.text(9.75, 10.9, 'findings', fontsize=7, ha='center', color='green', fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#D1FAE5'))

# 14. EDITOR AGENT
editor_box = FancyBboxPatch((10, 8.5), 2.5, 1.1, boxstyle="round,pad=0.1", 
                            edgecolor=color_editor, facecolor=color_editor, alpha=0.4, linewidth=2)
ax.add_patch(editor_box)
ax.text(11.25, 9.3, '⑭ EDITOR', ha='center', fontsize=10, fontweight='bold')
ax.text(11.25, 8.9, 'Review & refine\nImprove clarity\nPreserve citations', ha='center', fontsize=7)
ax.text(11.25, 8.6, '⏱️ 20-60s', ha='center', fontsize=7, style='italic', color='#64748B')

# Arrow writer -> editor (DRAFT FLOW)
ax.add_patch(FancyArrowPatch((11.25, 10.2), (11.25, 9.6),
             arrowstyle='->', mutation_scale=25, linewidth=2.5, color='orange', linestyle='dashed'))
ax.text(11.6, 9.9, 'draft', fontsize=7, color='orange', fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#FEF3C7'))

# REFLECTION LOOP (editor back to writer if needed)
ax.add_patch(FancyArrowPatch((10, 8.8), (10, 10.5),
             arrowstyle='->', mutation_scale=15, linewidth=2, color='purple', linestyle='dotted'))
ax.text(9.5, 9.65, 'feedback', fontsize=7, color='purple', rotation=90, va='center',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#F3E8FF'))

# 15. SAVE TO DB
save_box = FancyBboxPatch((10, 6.8), 2.5, 0.8, boxstyle="round,pad=0.1", 
                          edgecolor=color_db, facecolor=color_db, alpha=0.4, linewidth=2)
ax.add_patch(save_box)
ax.text(11.25, 7.4, '⑮ SAVE RESULT', ha='center', fontsize=10, fontweight='bold')
ax.text(11.25, 7, 'DB.update(result)\nstatus="done"', ha='center', fontsize=7)

# Arrow editor -> save
ax.add_patch(FancyArrowPatch((11.25, 8.5), (11.25, 7.6),
             arrowstyle='->', mutation_scale=25, linewidth=2.5, color='black'))
ax.text(11.6, 8, 'final', fontsize=7, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#D1FAE5'))

# Database storage visualization
db_store = FancyBboxPatch((8, 2.1), 3.5, 0.8, boxstyle="round,pad=0.05", 
                          edgecolor='#0891B2', facecolor='#ECFEFF', alpha=0.8, linewidth=2)
ax.add_patch(db_store)
ax.text(9.75, 2.7, 'tasks table', fontsize=9, ha='center', fontweight='bold')
ax.text(9.75, 2.3, '(id, prompt, status, result)', ha='center', fontsize=7)

# Arrow save -> DB
ax.add_patch(FancyArrowPatch((11.25, 6.8), (10, 2.9),
             arrowstyle='->', mutation_scale=20, linewidth=2, color='#0891B2'))

# 16. FRONTEND RECEIVES (polling completes)
final_box = FancyBboxPatch((10, 15.2), 2.2, 0.9, boxstyle="round,pad=0.1", 
                           edgecolor=color_success, facecolor=color_success, alpha=0.4, linewidth=3)
ax.add_patch(final_box)
ax.text(11.1, 15.9, '⑯ DISPLAY', ha='center', fontsize=11, fontweight='bold')
ax.text(11.1, 15.5, 'Render Markdown\nShow report', ha='center', fontsize=8)
ax.text(11.1, 15, '⏱️ Total: 2-5min', ha='center', fontsize=7, style='italic', color='#DC2626', fontweight='bold')

# Arrow DB -> Final (polling gets result)
ax.add_patch(FancyArrowPatch((9.75, 2.9), (11.1, 15.2),
             arrowstyle='->', mutation_scale=20, linewidth=2, color='#3B82F6',
             connectionstyle="arc3,rad=-.3"))
ax.text(10.3, 9, 'polling\nGET result', fontsize=7, ha='center', color='#3B82F6', 
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#EFF6FF'))

# === ERROR HANDLING PATH ===
error_box = FancyBboxPatch((1, 4.5), 3, 1.5, boxstyle="round,pad=0.1", 
                           edgecolor=color_error, facecolor='#FEE2E2', alpha=0.6, linewidth=2, linestyle='dashed')
ax.add_patch(error_box)
ax.text(2.5, 5.7, '❌ ERROR PATHS', ha='center', fontsize=10, fontweight='bold', color=color_error)
ax.text(2.5, 5.3, '• API rate limit (429)\n• Tool timeout\n• LLM error\n• DB connection fail', 
        ha='center', fontsize=7)
ax.text(2.5, 4.8, '→ status="error"\n→ graceful degradation', ha='center', fontsize=7, style='italic')

# Error arrows
ax.add_patch(FancyArrowPatch((8.25, 10.2), (4, 5.5),
             arrowstyle='->', mutation_scale=15, linewidth=1.5, color=color_error, linestyle='dashed'))

# === KEY INSIGHTS BOX ===
insights_box = FancyBboxPatch((0.5, 4), 0.1, 7.5, boxstyle="round,pad=0.05", 
                              edgecolor='#F59E0B', facecolor='#FEF3C7', alpha=0.3, linewidth=2)
ax.add_patch(insights_box)

# Insights text
insights = [
    "💡 KEY INSIGHTS:",
    "",
    "🔄 Sequential not Parallel",
    "   Research→Writer→Editor",
    "",
    "⚡ max_turns=5 crucial",
    "   Allows tool iteration",
    "",
    "🧵 Threading Model:",
    "   • Main: HTTP requests",
    "   • Background: Agents",
    "",
    "📊 Context Passing:",
    "   History list grows",
    "   Each agent sees prior",
    "",
    "🎯 Executor orchestrates",
    "   THE missing piece!",
    "",
    "⏱️ Timing:",
    "   • Planning: 10-20s",
    "   • Research: 20-60s", 
    "   • Writing: 30-90s",
    "   • Editing: 20-60s",
    "",
    "💰 Cost: ~$0.05-0.10",
    "   15K-20K tokens total"
]

for i, line in enumerate(insights):
    y_pos = 11 - (i * 0.28)
    if line.startswith("💡"):
        ax.text(0.3, y_pos, line, fontsize=9, fontweight='bold', color='#92400E')
    elif line.startswith(("🔄", "⚡", "🧵", "📊", "🎯", "⏱️", "💰")):
        ax.text(0.3, y_pos, line, fontsize=8, fontweight='bold', color='#78350F')
    elif line.strip().startswith("•"):
        ax.text(0.4, y_pos, line, fontsize=7, color='#78350F')
    elif line.strip():
        ax.text(0.3, y_pos, line, fontsize=7, color='#78350F')

# === LEGEND ===
legend_elements = [
    mlines.Line2D([0], [0], color='black', linewidth=3, label='① Sequence (numbered)'),
    mlines.Line2D([0], [0], color='green', linewidth=2, linestyle='dashed', label='Data Flow'),
    mlines.Line2D([0], [0], color='purple', linewidth=2, linestyle='dotted', label='Feedback Loop'),
    mlines.Line2D([0], [0], color='red', linewidth=2, linestyle='dashed', label='Error Path'),
    mpatches.Patch(facecolor='#EFF6FF', edgecolor='#3B82F6', label='User/Frontend', linewidth=2),
    mpatches.Patch(facecolor='#EDE9FE', edgecolor='#6366F1', label='Main Thread', linewidth=2),
    mpatches.Patch(facecolor='#FAF5FF', edgecolor='#8B5CF6', label='Background Thread', linewidth=2),
]
ax.legend(handles=legend_elements, loc='upper right', fontsize=8, framealpha=0.9)

# === DATA FORMAT ANNOTATIONS ===
formats = [
    (2.1, 14.7, 'str'),
    (4.8, 14.7, 'JSON'),
    (2.25, 9.9, 'List[str]'),
    (8.25, 9.9, 'str+HTML'),
    (11.25, 9.9, 'Markdown'),
]
for x, y, fmt in formats:
    ax.text(x, y, f'[{fmt}]', fontsize=6, ha='center', 
            bbox=dict(boxstyle='round,pad=0.2', facecolor='yellow', alpha=0.3))

plt.tight_layout()
plt.savefig('improved_architecture_flowchart.png', dpi=300, bbox_inches='tight', facecolor='white')
print("✓ Improved flowchart created: improved_architecture_flowchart.png")

