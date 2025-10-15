"""
Setup script for Course Lab Notebooks
Add this cell at the top of any notebook that needs to import from src/

Usage in notebook:
    import sys
    sys.path.append('..')
    from src.agents import research_agent, writer_agent, editor_agent
    from src.research_tools import arxiv_search_tool, tavily_search_tool, wikipedia_search_tool
    from src.planning_agent import planner_agent, executor_agent_step
"""

import sys
import os

# Add parent directory to path for imports
parent_dir = os.path.abspath(os.path.join(os.getcwd(), '..'))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

print(f"✅ Added {parent_dir} to Python path")
print("✅ You can now import from src/ directory")
print("\nExample imports:")
print("  from src.agents import research_agent, writer_agent, editor_agent")
print("  from src.research_tools import arxiv_search_tool, tavily_search_tool")
print("  from src.planning_agent import planner_agent")

