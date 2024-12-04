import streamlit as st
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage, AIMessage

# Streamlit UI Setup

def configure_page():
  st.set_page_config(
    page_title = "Ollama Chat App",
    layout = "centered",
    initial_sidebar_state="expanded"
  )
  st.title("Chatting with Ollama")



def get_response(query, chat_history):
  template = """You are an assistant for question-answering tasks.
    Use five sentences maximum and keep the answer concise:

    Chat History: {chat_history}
    User question: {user_question}
    """
  
  prompt = ChatPromptTemplate.from_template(template)
  llm = ChatOllama(model="llama3.1", temperature=0.3,)
  chain = prompt | llm |  StrOutputParser()
  return chain.stream({
    "chat_history": chat_history,
    "user_question": query
  })


def display_messages():
  if "messages" not in st.session_state:
    st.session_state.messages = []

  for message in st.session_state.messages:
    if isinstance(message, HumanMessage):
      with st.chat_message("Human"):
        st.markdown(message.content)

    else:
       with st.chat_message("AI"):
        st.markdown(message.content)


  user_query = st.chat_input("Message Ollama")
  if user_query is not None and user_query != "":
    st.session_state.messages.append(HumanMessage(user_query))

    with st.chat_message("Human"):
      st.markdown(user_query)

    with st.chat_message("AI"):
      ai_response = st.write_stream(get_response(user_query, st.session_state.messages))

    st.session_state.messages.append(AIMessage(ai_response))

configure_page() 

if(st.session_state.login_in == False):
    st.write("Please log in to use the Chat Bot")

    if(st.button("Log in")):
        st.switch_page("Main_page.py")

else:
  display_messages()