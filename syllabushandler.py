from pypdf import PdfReader
import fitz
import re
from os import listdir
from langchain.text_splitter import RecursiveCharacterTextSplitter, SentenceTransformersTokenTextSplitter
from Models.ClassModel import ClassDAO
from Models.SyllabusModel import SyllabusDAO
import torch.nn.functional as F


from sentence_transformers import SentenceTransformer

#model = SentenceTransformer("all-MiniLM-L6-v2")
model = SentenceTransformer("all-mpnet-base-v2")


#If your root folder is rumadv2, just put in syllabuses
files = listdir(r"rumad-v2-app-compprogram/syllabuses")
print(files)

#extract chunks

unwanted_data = [
    r"12\.\s*a.*",
    r"13\.\s* Academic[\s\S]*Integrity[\s\S]*?(?=UPR Students General Bylaws)",
    r"the\s*university\s*+of\s*puerto\s*rico\s*promotes[\s\S]*?(?=UPR Students General Bylaws)"
    r"According\s*to\s*Law\s*51.*?(?=\n13.)",
    r"University\s*of\s*Puerto\s*Rico\s*-\s*Mayagüez[\s\S]*?(?=\nCIIC|INSO|Course)",
]


def normalize_text(text):
    """
    Normalize the document text by removing unwanted characters, replacing non-standard spaces,
    and normalizing whitespace.
    """
    # Replace non-breaking spaces and tabs with standard spaces
    text = text.replace("\u00A0", " ").replace("\t", " ")
    

    # Remove unwanted non-ASCII characters while keeping Spanish characters
    # Keep Latin-1 Supplement and Latin Extended-A ranges (includes Spanish special characters)
    text = re.sub(r"[^\w\sáéíóúüñÁÉÍÓÚÜÑ.,%!?¿¡-]", "", text)
    # text = re.sub(r"^(☒|☐)\s*.+\s+\d+%$", ",", text)
    
    # Collapse multiple spaces into a single space
    # text = re.sub(r"\s+", " ", text)
    
    # Trim leading and trailing whitespace
    return text.strip()


def remove_unwanted_data(text):
    text = normalize_text(text)
    for pattern in unwanted_data:
        text = re.sub(pattern, "", text, flags=re.IGNORECASE)
    return text


def remove_pattern_from_pdf(file_path):
    doc = fitz.open(file_path)
    content = []
    for page in doc:
        text = page.get_text()
        cleaned_text = remove_unwanted_data(text)
        content.append(cleaned_text.strip())
    return content


 

classDAO = ClassDAO()
SyllabusDAO = SyllabusDAO()


for f in files:
    # this variables also was changed
    fname = r"rumad-v2-app-compprogram/syllabuses/" + f
    print(f)
    #parsing file -----------------------------------------
    string_to_parse = f
    course_name = re.split(r"[-.]", string_to_parse) #tokenizes it so that we can know the name and desc
    course_name.pop() #so that .pdf is not there, although it's not needed 

    #You get this from the current file name
    cname = course_name[0]
    ccode = course_name[1]

    #--------------------------------------------------------
    


    pdf_texts = remove_pattern_from_pdf(fname)
    print(pdf_texts)
    # Filter the empty strings
    pdf_texts = [text for text in pdf_texts if text]

    

    print(pdf_texts[0])

    #split
    character_splitter = RecursiveCharacterTextSplitter(
        separators=["\n\n", "\n", ". ", " ", ""],
        chunk_size=300,
        chunk_overlap=150)
    character_split_texts = character_splitter.split_text('\n\n'.join(pdf_texts))

    # print(character_split_texts[5])
    print(f"\nTotal chunks: {len(character_split_texts)}")

    [print(t) for t in character_split_texts]
    print()
    #Token
    token_splitter = SentenceTransformersTokenTextSplitter(chunk_overlap=50, tokens_per_chunk=256)

    token_split_texts = []
    for text in character_split_texts:
        token_split_texts += token_splitter.split_text(text)
    print("token")
    # print(token_split_texts[5])
    [print(t) for t in token_split_texts]
    print(f"\nTotal Splitted chunks: {len(token_split_texts)}") 
    
    # exit(1)

    # get the course that the syllabus is about 
    cid = classDAO.GetCIDbyNameAndCode(cname, ccode)


    for t in token_split_texts:
        emb = model.encode(t, normalize_embeddings=True)
        print(t)
        SyllabusDAO.insertFragment(cid, emb.tolist(), t)
    print("Done file: " + f)
   
