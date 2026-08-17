from src.agentic_ai.states.state import State

class Chatbot_with_ToolNode:
    """
    Chatbot logic snhnace with tool integration.
    """

    def __init__(self,model):
        self.llm_model = model

    def process(self, state: State) -> dict:
        """
        Processes the input state and generates a response with tool integration.
        """

        user_input = state["messages"][-1] if state["messages"] else ""
        llm_res = self.llm_model.invoke([{"role": "user", "content": user_input}])

        # Simulate tool-specific logic
        tool_res = f"Tool integration for: '{user_input}"

        return {"messages": [llm_res, tool_res]}

    def create_chatbot(self, tools):
        """
        Returns a chatbot node function.
        """
        llm_with_tools = self.llm_model.bind_tools(tools)

        def chatbot_node(state: State):
            """
            Chatbot logic for processing the input state and returning a response.
            """
            return {"messages": [llm_with_tools.invoke(state["messages"])]}

        return chatbot_node