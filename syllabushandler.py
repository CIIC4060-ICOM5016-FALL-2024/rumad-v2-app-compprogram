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

files = listdir("rumad-v2-app-compprogram//syllabuses")
print(files)

#extract chunks

def remove_headers_from_pdf(file_path, patterns):
    doc = fitz.open(file_path)
    content = []
    for page in doc:
        text = page.get_text()
        # Remove header using regex
        cleaned_text = re.sub(patterns[0], '', text, flags=re.IGNORECASE)
        cleaned_text = re.sub(patterns[1], '', cleaned_text, flags=re.IGNORECASE)
        cleaned_text = re.sub(patterns[2], '', cleaned_text, flags=re.IGNORECASE)
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
    r"|12\. According to Law 51\s*"
    r"Students will identify themselves with the Institution and the instructor of the course for purposes of\s*"
    r"assessment \(exams\) accommodations\. For more information please call the Student with Disabilities Office\s*"
    r"which is part of the Dean of Students office \(Office #4\)  at  \(787\)265-3862 or \(787\)832-4040 extensions\s*"
    r"3250 or 3258\.\s*"
)
AcademicIntegrityPattern = (
    r"|13\. Academic Integrity\s*-The University of Puerto Rico promotes the highest standards of academic and scientific integrity\. Article\s*"
    r"6\.2 of the UPR Students General Bylaws \(Board of Trustees Certification 13, 2009-2010\) states that\s*"
    r"academic dishonesty includes, but is not limited to: fraudulent actions; obtaining grades or academic\s*"
    r"degrees by false or fraudulent simulations; copying the whole or part of the academic work of another\s*"
    r"person; plagiarizing totally or partially the work of another person; copying all or part of another person\s*"
    r"answers to the questions of an oral or written exam by taking or getting someone else to take the exam on\s*"
    r"his/her behalf; as well as enabling and facilitating another person to perform the aforementioned\s*"
    r"behavior\. ​Any of these behaviors will be subject to disciplinary action in accordance with the disciplinary\s*"
    r"procedure laid down in the ​UPR Students General Bylaws\.\s*"
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
        chunk_size=750,
        chunk_overlap=185)
    character_split_texts = character_splitter.split_text('\n\n'.join(pdf_texts))

    print(character_split_texts[5])
    print(f"\nTotal chunks: {len(character_split_texts)}")

    [print(t) for t in character_split_texts]
    print()
    #Token
    token_splitter = SentenceTransformersTokenTextSplitter(chunk_overlap=50, tokens_per_chunk=200)

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
   


