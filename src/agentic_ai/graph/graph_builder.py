from langgraph.graph import START,END
from langgraph.graph import StateGraph
from src.agentic_ai.states.state import State
from langgraph.prebuilt import tools_condition
from src.agentic_ai.nodes.chatbot_node import Chatbot_Node
from src.agentic_ai.tools.search_tool import get_tools, create_tool_node
from src.agentic_ai.nodes.chatbot_with_Tool_node import Chatbot_with_ToolNode

class GraphBuilder:
    def __init__(self,model):
        self.llm = model
        self.graph_builder = StateGraph(State)

    def chatbot_build_graph(self):
        """
        Builds a basic chatbot graph using LangGraph.
        This method initializes a chatbot node using the `Chatbot_Node` class 
        and integrates it into the graph. The chatbot node is set as both the 
        entry and exit point of the graph.
        """
        # Define the chatbot node
        self.chatbot_node=Chatbot_Node(self.llm)

        # Define Nodes in the graph
        self.graph_builder.add_node("chatbot",self.chatbot_node.process)

        # Define Edges in the graph
        self.graph_builder.add_edge(START,"chatbot")
        self.graph_builder.add_edge("chatbot",END)

    def chatbot_with_tools_build_graph(self):
        """
        Builds an advanced chatbot graph with tool integration.
        This method creates a chatbot graph that includes both a chatbot node 
        and a tool node. It defines tools, initializes the chatbot with tool 
        capabilities, and sets up conditional and direct edges between nodes. 
        The chatbot node is set as the entry point.
        """

        # Define the tool and tool node
        tools = get_tools()
        tool_node = create_tool_node(tools)

        # Define the chatbot node
        obj_chatbot_with_node = Chatbot_with_ToolNode(self.llm)
        chatbot_node = obj_chatbot_with_node.create_chatbot(tools)

        # Define Nodes in the graph
        self.graph_builder.add_node("chatbot",chatbot_node)
        self.graph_builder.add_node("tools",tool_node)

        # Define Edges in the graph
        self.graph_builder.add_edge(START,"chatbot")
        self.graph_builder.add_conditional_edges("chatbot",tools_condition)
        self.graph_builder.add_edge("tools","chatbot")
 
    def setup_graph(self, usecase: str):
        """
        Sets up the graph for the selected use case.
        """
        if usecase == "Basic Chatbot":
            self.chatbot_build_graph()

        if usecase == "Chatbot With Tool":
            self.chatbot_with_tools_build_graph()

        return self.graph_builder.compile()