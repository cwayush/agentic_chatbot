from langgraph.graph import START,END
from langgraph.graph import StateGraph
from src.agentic_ai.states.state import State
from src.agentic_ai.nodes.chatbot_node import Chatbot_Node

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

        self.chatbot_node=Chatbot_Node(self.llm)

        self.graph_builder.add_node("chatbot",self.chatbot_node.process)

        self.graph_builder.add_edge(START,"chatbot")
        self.graph_builder.add_edge("chatbot",END)

    def setup_graph(self, usecase: str):
        """
        Sets up the graph for the selected use case.
        """
        if usecase == "Basic Chatbot":
            self.chatbot_build_graph()

        return self.graph_builder.compile()