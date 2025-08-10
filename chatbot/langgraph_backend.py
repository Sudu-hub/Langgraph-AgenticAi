from langgraph.graph import StateGraph,START,END
from langchain_ollama import ChatOllama
from typing import TypedDict, Annotated
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph.message import add_messages
from langchain_core.messages import BaseMessage

llm = ChatOllama(model='gemma3:4b')

#create state using message or add_messages
class ChatState(TypedDict):
    messages = Annotated[list[BaseMessage], add_messages]

#create node task function
def chat_node(state: ChatState):
    messages = state['messages'] #assign the a state to each node
    response = llm.invoke(messages)
    return {'messages': {response}}

#checkpointer
checkpointer = InMemorySaver()

# create a graph
graph = StateGraph(ChatState)

#create node
graph.add_node(START, chat_node)
graph.add_node('chat_node', END)

#compile the graph
chatbot = graph.compile(checkpointer=checkpointer)

