import re 
from os import listdir

#replace with real directory of syllabuses
files = listdir(r"C:\Users\btgmn\OneDrive\Documents\RUM DOCS\Semester Fall 2024\Database\GithubDB\rumad-v2-app-compprogram\syllabuses")
# print(files)

course = {
    "cname": "",
    "ccode": "",
    "cdesc": ""
}
list_of_courses = []

for f in files:
    print(f) #The file name to parse
    string_to_parse = f
    course_name = re.split(r"[-.]", string_to_parse) #tokenizes it so that we can know the name and desc
    course_name.pop()
    print(course_name)
    course.update({
        "cname": course_name[0],
        "ccode": course_name[1],
        "cdesc": " ".join(course_name[2:])
        })
    list_of_courses.append(course)    