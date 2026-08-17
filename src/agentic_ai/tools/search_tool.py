from langgraph.prebuilt import ToolNode
from langchain_community.tools.tavily_search import TavilySearchResults

def get_tools():
    """
    Return the list of tools to be used in the chatbot
    """
    tools=[TavilySearchResults(max_results = 2)]

    return tools

def create_tool_node(tools):
    """
    creates and returns a tool node for the graph
    """
    return ToolNode(tools = tools)

