from pypdf import PdfReader
import fitz
import re
from os import listdir
from langchain.text_splitter import RecursiveCharacterTextSplitter, SentenceTransformersTokenTextSplitter
from Models.ClassModel import ClassDAO
from Models.SyllabusModel import SyllabusDAO

from sentence_transformers import SentenceTransformer

#model = SentenceTransformer("all-MiniLM-L6-v2")
model = SentenceTransformer("all-mpnet-base-v2")

files = listdir(r"rumad-v2-app-compprogram/syllabuses")
print(files)

#extract chunks

def remove_headers_from_pdf(file_path, patterns):
    doc = fitz.open(file_path)
    content = []
    for page in doc:
        text = page.get_text()
        # Remove header using regex
        cleaned_text = re.sub(patterns[0], '', text, flags=re.IGNORECASE)
        cleaned_text = re.sub(patterns[1], '', cleaned_text, flags=re.DOTALL)
        cleaned_text = re.sub(patterns[2], '', cleaned_text, flags=re.DOTALL)
        content.append(cleaned_text.strip())
    return content




classDAO = ClassDAO()
SyllabusDAO = SyllabusDAO()
headerPattern = (
    r"University of Puerto Rico\s*-?\s*Mayagüez Campus\s*"
    r"College of Engineering\s*"
    r"Department of Computer Science and Engineering\s*"
    r"(Program in Software Engineering\s*|Program in Computer Science and Engineering\s*)?"
)
Law51Pattern =(
    r"12. According to Law 51.*"
)
AcademicIntegrityPattern = (
    r"(Law 51|Article\s*6\.2|-The University of Puerto Rico promotes the highest standards of academic and scientific integrity|[Pp]age\s*4\s*of\s*4).*"
)


for f in files:
    fname = "rumad-v2-app-compprogram//syllabuses//" + f
    print(f)
    #parsing file -----------------------------------------
    string_to_parse = f
    course_name = re.split(r"[-.]", string_to_parse) #tokenizes it so that we can know the name and desc
    course_name.pop() #so that .pdf is not there, although it's not needed 

    #You get this from the current file name
    cname = course_name[0]
    ccode = course_name[1]

    #--------------------------------------------------------
    

    
    patterns = [headerPattern, Law51Pattern, AcademicIntegrityPattern]
    pdf_texts = remove_headers_from_pdf(fname, patterns)
    # pdf_texts = remove_headers_from_pdf(fname, patterns[1])
    # pdf_texts = remove_headers_from_pdf(fname, patterns[2])
    print(pdf_texts)
    # Filter the empty strings
    pdf_texts = [text for text in pdf_texts if text]

    

    print(pdf_texts[0])

    #split
    character_splitter = RecursiveCharacterTextSplitter(
        separators=["\n\n", "\n", ". ", " ", ""],
        chunk_size=600,
        chunk_overlap=300)
    character_split_texts = character_splitter.split_text('\n\n'.join(pdf_texts))

    print(character_split_texts[5])
    print(f"\nTotal chunks: {len(character_split_texts)}")

    [print(t) for t in character_split_texts]
    print()
    #Token
    token_splitter = SentenceTransformersTokenTextSplitter(chunk_overlap=50, tokens_per_chunk=256)

    token_split_texts = []
    for text in character_split_texts:
        token_split_texts += token_splitter.split_text(text)
    print("token")
    print(token_split_texts[5])
    [print(t) for t in token_split_texts]
    print(f"\nTotal Splitted chunks: {len(token_split_texts)}") 
    
    # exit(1)

    # get the course that the syllabus is about 
    cid = classDAO.GetCIDbyNameAndCode(cname, ccode)


    for t in token_split_texts:
        emb = model.encode(t, normalize_embeddings=True)
        # current_length = len(emb)
        # remaining_length = 1000-current_length
        # for i in range(0,remaining_length):
        #     emb = np.append()

        #print(t)
        #print(emb)
        SyllabusDAO.insertFragment(cid, emb.tolist(), t)
    print("Done file: " + f)
   


