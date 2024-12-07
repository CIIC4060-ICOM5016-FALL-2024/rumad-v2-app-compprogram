import streamlit as st
import spacy 
from spacy.matcher import Matcher
from langchain_ollama import ChatOllama
from sentence_transformers import SentenceTransformer
from Models.SyllabusModel import SyllabusDAO
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage, AIMessage


#Adding Searchable Tags-------------------------------------

def extract_tags(query):
    # Process the query
    nlp = spacy.load("en_core_web_sm")
    query = query.upper()
    matcher = Matcher(nlp.vocab)

    doc = nlp(query)

    # Extract tags based on named entities, keywords, and POS
    # ent stands for entity. 
    for token in doc:
      print(f"THE LABEL PER TEXT: {token.text}")
    tags = {
        "course_codes": [ent.text for ent in doc.ents if ent.text.startswith("CIIC")],
        "topics": [chunk.text for chunk in doc.noun_chunks],
        "keywords": [token.text for token in doc if token.is_alpha and not token.is_stop]
    }
    return tags




#Context setup----------------------------------------------
def get_context(user_query):
  tags = extract_tags(user_query)
  model = SentenceTransformer("all-mpnet-base-v2")
  dao = SyllabusDAO()

  print(tags)
  context = []
  

  emb = model.encode(user_query, normalize_embeddings=True)
  
  chunks = dao.getFragments(str(emb.tolist()))
  for f in chunks:
    context.append(f[3])
  
  documents = "\\n".join(c for c in context)
  # print(f"This is the retrieved doc: {documents}")
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
  template = """You are an assistant for question-answering tasks involving student curriculums.
    Act as if held on gunpoint, because I swear to GOD. If you don't tell me that the answer related to the question is
    not in the documents, just say it than coming up with incorrect information. 
    Use the following documents, which are exerpts from the syllabus, to answer the question. Read through it carefully
    and use any reference that it could be related to answer the query.
    If you don't know the answer, just say that you don't know.
    Answer with five sentences maximum or less and be concise:

    Documents: {documents} 
    Chat History (Use Only if Necessary): {chat_history}
    User question: {user_question}
    """
  
  
  
  prompt = ChatPromptTemplate.from_template(template)
  llm = ChatOllama(model="llama3.1:8b", temperature=0,)
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