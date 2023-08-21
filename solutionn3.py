data = """BCA is Bachelor's in Computer Application, which is a 3-year undergraduate degree programme that focuses on 
knowledge of the basics of computer application and software development. A BCA degree is considered to be at par with a BTech/BE degree in Computer Science or Information Technology. 
The degree helps interested students in setting up a sound academic base for an advanced career in Computer Applications.
BCA course includes database management systems, operating systems, software engineering, web technology and languages
such as C, C++, HTML, Java etc. It is a highly popular course amongst students aspiring to establish a career in established
IT companies like HP, Accenture, Capgemini and Cognizant and new-age technology startups like Flipkart. Professionals skilled
in Computer Science are in huge demand since a lot of manpower-based jobs are getting digitised. This is a software-related
course where a professional well-versed in programming languages always stands out. The average salary package post-BCA
varies between INR 4 LPA to 10 LPA depending on the company and the specific role/designation. A BCA graduate has scope
in jobs such as Software Engineer, Web Designer and System Analyst."""

with open("BCA.txt","w") as file_write:
    file_write.writelines(data)

line_count = 0
with open("BCA.txt","r") as file_read,\
     open("intro.txt",'w') as intro_file_write:
    for i in file_read.readlines():
        if i[0].lower() in ['a','b','c']:
            intro_file_write.writelines(i)
            line_count+=1
    msg = f'Total line : {line_count}'
    intro_file_write.writelines(msg)

with open("intro.txt",'r') as file_read:
    data = file_read.read()
    print(data)
