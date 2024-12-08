import streamlit as st
import spacy
import re
from sentence_transformers.util import normalize_embeddings
from spacy.matcher import Matcher
from langchain_ollama import ChatOllama
from sentence_transformers import SentenceTransformer
from Models.SyllabusModel import SyllabusDAO
from Models.ClassModel import ClassDAO
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage, AIMessage


#Adding Searchable Tags-------------------------------------

def extract_tags(query):
    # Process the query
    nlp = spacy.load("en_core_web_sm")
    matcher = Matcher(nlp.vocab) #Initialize matcher
    patterns = [[{"POS": "PROPN", "LENGTH": 4}, {"DEP": "nummod", "LENGTH": 4}]] #Each ccode is length 4, and a numeric modifier of length 4
    matcher.add("COURSEID", patterns)

    query = query.upper() #makes everything in CAPS for normalizing
    doc = nlp(query) #processes query using a natural language process
    matches = matcher(doc)
    # Extract tags based on named entities, keywords, and POS
    # ent stands for entity. 
        
    for match_id, start, end in matches:
      string_id = nlp.vocab.strings[match_id]  # Get string representation
      span = doc[start:end]  # The matched span
      print(match_id, string_id, start, end, span.text) #Debug print

    tags = {
        "course_codes": [doc[start:end].text for match_id, start, end in matches],
        "topics": [chunk.text for chunk in doc.noun_chunks],
        "keywords": [token.text for token in doc if token.is_alpha and not token.is_stop]
    }
    print(tags)
    return tags




#Context setup----------------------------------------------
SyllabusDAO = SyllabusDAO()
ClassDAO = ClassDAO()
def get_context(user_query):
  tags = extract_tags(user_query)
  model = SentenceTransformer("all-mpnet-base-v2")

  strings_to_parse = tags["course_codes"]
  cid = 0

  if strings_to_parse:
    course_name = re.split(" ", strings_to_parse[0]) #tokenizes it so that we can know the name 
      #You get this from the current file name
    cname = course_name[0]
    ccode = course_name[1]
    # print(course_name)
    cid = ClassDAO.GetCIDbyNameAndCode(cname, ccode)
  # print(f"this is the cid: {cid}")
  
  context = []
  
  # print(tags["course_codes"])
  emb = model.encode(user_query, normalize_embeddings=True)
  
  #possibility for there not to be any mention of course codes
  # print (cid)
  if tags["course_codes"]:
    print("CID GET")
    chunks = SyllabusDAO.getFragmentsByCID(str(emb.tolist()), cid)
    for f in chunks:
      context.append(f[3])
  else:
    print("NORMAL GET")
    # keywordsList = tags["keywords"] #look for extracted keywords from user_query
    # StringKeyword = ', '.join(keywordsList) #keywordsList is a list, so turn it into string to embed
    # keywordEmbedding = model.encode(StringKeyword, normalize_embeddings=True)

    # MixEmbed = 0.7 * keywordEmbedding + 0.3 * emb #makes sure to highlight the extracted keywords form the user query and add more weight to them
    # MixEmbed = normalize_embeddings(MixEmbed) #normalizing

    chunks = SyllabusDAO.getFragments(str(emb.tolist()))
    for f in chunks:
      context.append(f[3])
  
  documents = "\\n".join(c for c in context)
  print(f"This is the retrieved doc: {documents}")
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
  template = """Act as a IT help desk employee and use the documents given, not chat history to answer the question. 
    Chat history is only used to recall what were previous questions, not previous answers.
    The given documents are syllabuses that help answer the question.      
    Read through it carefully.
    Cite the source.
    If it's something that you can list out, put them in bullet point format.
: 

  

    Documents: {documents} 
    Chat History (Use Only if Necessary): {chat_history}
    User question: {user_question}
    """
  
  
  
  prompt = ChatPromptTemplate.from_template(template)
  llm = ChatOllama(model="llama3.1:8b", temperature=0.1,)
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