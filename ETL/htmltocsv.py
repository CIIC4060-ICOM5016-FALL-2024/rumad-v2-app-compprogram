import xml.etree.ElementTree as ET
import csv

# Load and parse the XML file
tree = ET.parse('courses.xml')
root = tree.getroot()

# Open a CSV file for writing
with open('courses.csv', 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    # Write the header
    writer.writerow(['cid', 'cname', 'ccode', 'cdesc', 'term', 'years', 'cred', 'csyllabus'])
    
    # Iterate over each <Courses> element in the XML
    for course in root.findall('Courses'):
        # Initialize variables
        cid = course.find('classid').text if course.find('classid') is not None else ''
        cred = course.find('cred').text if course.find('cred') is not None else ''
        cdesc = course.find('description').text if course.find('description') is not None else ''
        csyllabus = course.find('syllabus').text if course.find('syllabus') is not None else ''
        term = course.find('term').text if course.find('term') is not None else ''
        years = course.find('years').text if course.find('years') is not None else ''
        
        # Extract data from <classes> sub-element
        classes = course.find('classes')
        if classes is not None:
            ccode = classes.find('code').text if classes.find('code') is not None else ''
            cname = classes.find('name').text if classes.find('name') is not None else ''
        else:
            ccode = ''
            cname = ''
        
        # Write the row to CSV
        writer.writerow([cid, cname, ccode, cdesc, term, years, cred, csyllabus])

print("CSV file has been created successfully.")
