import streamlit as st
import spacy
import re
import numpy as np
import torch
import torch.nn.functional as F
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
    patterns = [
        [{"POS": "PROPN", "LENGTH": 4}, {"DEP": "nummod", "LENGTH": 4}],
        [{"SHAPE": "XXXXdddd"}],
        [{"TEXT": {"REGEX": r"\b\w{4}(?:\s*[-_.:/,]+\s*)\d{4}\b"}}]
                ] #Each ccode is length 4, and a numeric modifier of length 4
    matcher.add("COURSEID", patterns)

    query = query.upper() #makes everything in CAPS for normalizing
    doc = nlp(query) #processes query using a natural language process
    matches = matcher(doc)
    # Extract tags based on named entities, keywords, and POS (Part of speech)
    # ent stands for entity. 
        
    # for match_id, start, end in matches:
    #   string_id = nlp.vocab.strings[match_id]  # Get string representation
    #   span = doc[start:end]  # The matched span
    #   print(match_id, string_id, start, end, span.text) #Debug print

    for token in doc:
      print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
            token.shape_, token.is_alpha, token.is_stop)

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
  # print(strings_to_parse[0])
  cid = []
  if strings_to_parse:
    for course in strings_to_parse:
      #Tokenizes to match lookahead of digits, or hyphen
      parsed_course = re.split(r'(-|\d+)', course)

      #strips leading whitespace if possible
      result = " ".join(part for part in parsed_course if part).strip()

      #gets rid of any delimiter that could be used to indicate course code
      result = re.sub(r"[-_.:/,]", "", result)
      
      course_name = re.split(" ", result) #tokenizes it so that we can know the name

      #remove any extra whitespace, it might seem redundant, but its needed 
      course_name = " ".join(part for part in course_name if part).strip()
      course_name = re.split(" ", course_name)
        #You get this from the current file name
      cname = course_name[0]
      ccode = course_name[1]
      # print(course_name)
      cid.append(ClassDAO.GetCIDbyNameAndCode(cname, ccode))
  # print(f"this is the cid: {cid}")
  
  context = []
  
  # print(tags["course_codes"])
  emb = model.encode(user_query, normalize_embeddings=True)
  print(type(emb))
  
  #possibility for there not to be any mention of course codes
  # print (cid)
  if tags["course_codes"]:
    print("CID GET")
    for id in cid:
      chunks = SyllabusDAO.getFragmentsByCID(str(emb.tolist()), id) #returns a list of chunks related to the asked syllabus
      for f in chunks:
        context.append(f[3])
  else:
    print("NORMAL GET")
    query_weight = 0.3
    topic_weight = 0.5
    keyword_weight = 0.7
    
    topics = tags["topics"] # Save the list of topics extracted from memory
    keywords = tags["keywords"] # Save the list of keywords extracted from memory

    topics = ', '.join(topics)
    keywords= ', '.join(keywords) #keywordsList is a list, so turn it into string to embed

    #embedding 
    topics_emb = model.encode(topics, normalize_embeddings=True)
    key_emb = model.encode(keywords, normalize_embeddings=True)

    weighted_embed = (keyword_weight * key_emb) + (topic_weight * topics_emb) + (query_weight * emb)  #makes sure to highlight the extracted keywords form the user query and add more weight to them
    
    # transforming into torch tensor type to normalize
    weighted_embed = torch.from_numpy(weighted_embed)
    weighted_embed = F.normalize(weighted_embed, p=2.0, dim=0)
    

    chunks = SyllabusDAO.getFragments(str(weighted_embed.tolist()))
    for f in chunks:
      context.append(f[3])
  
  documents = "\\n".join(c for c in context)
  # print(f"This is the retrieved context: {documents}")
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
    If there's no mention of the course in the provided documetnts, then it doesn't exist.
    If it's something that you can list out, put them in bullet point format:

  

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