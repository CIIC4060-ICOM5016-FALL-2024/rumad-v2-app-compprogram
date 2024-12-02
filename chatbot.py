import streamlit as st
from langchain_ollama import ChatOllama
from sentence_transformers import SentenceTransformer
from Models.SyllabusModel import SyllabusDAO
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage, AIMessage

#Context setup----------------------------------------------
def get_context(user_query):
  model = SentenceTransformer("all-mpnet-base-v2")
  dao = SyllabusDAO()
  context = []

  emb = model.encode(user_query)
  chunks = dao.getFragments(str(emb.tolist()))
  for f in chunks:
    # print(f)
    context.append(f[3])
  
  documents = "\\n".join(c for c in context)
  return documents



# Streamlit UI Setup

def configure_page():
  st.set_page_config(
    page_title = "Ollama Chat App",
    layout = "centered",
    initial_sidebar_state="expanded"
  )
  st.title("Chatting with Ollama")



def get_response(query, chat_history, documents):
  template = """You are an assistant for question-answering tasks.
    Use the following documents to answer the question, and read any [UNK] token as a newline, double check your work.
    If you don't know the answer, just say that you don't know.
    Use five sentences maximum and keep the answer concise:

    Documents: {documents}
    Chat History (Use Only if Necessary): {chat_history}
    User question: {user_question}
    """
  
  prompt = ChatPromptTemplate.from_template(template)
  llm = ChatOllama(model="llama3.1:8b", temperature=0.3,)
  chain = prompt | llm |  StrOutputParser()
  return chain.stream({
    "chat_history": chat_history,
    "user_question": query,
    "documents": documents
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
      documents = get_context(user_query)
      ai_response = st.write_stream(get_response(user_query, st.session_state.messages, documents))

    st.session_state.messages.append(AIMessage(ai_response))

  

configure_page()
display_messages()