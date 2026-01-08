''''
 IERG 1080B Introduction to Python for Engineering Applications

 I declare that the assignment here submitted is original
 except for source material explicitly acknowledged,
 and that the same or closely related material has not been
 previously submitted for another course.
 I also acknowledge that I am aware of University policy and
 regulations on honesty in academic work, and of the disciplinary
 guidelines and procedures applicable to breaches of such
 policy and regulations, as contained in the website.

 University Guideline on Academic Honesty:
   http://www.cuhk.edu.hk/policy/academichonesty/

 Student Name : Leung Chi Hei
 Student ID   : 1155212427
 Class/Section: IERG1080B
 Date         : 6/1/2026
'''

def printCourse(title = "Python", dept = "IERG", code = 1080, gpa_max = 4.0):
    
    # Replace [Input Your Format String] with your answer. You may edit the arguments.
    print("The course {1} {2} is about '{0}'.\nYou can get at most {3} GPA.".format(title, dept, code, gpa_max))


if __name__ == "__main__":
    printCourse() 