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
 Date         : 15/1/2026
'''

def number_filter(a, b):
    """The function returns a list of integers after filtering"""
    # Modify the code here
    output = []
    for i in range(a, b + 1):
      if i % 5 == 0 and not i % 3 == 0:
        output.append(i)
    return(output)


if __name__ == "__main__":
    a = int(input())
    b = int(input())
    
    if a > b:
      a, b = b, a
    number_filter(a, b) # for testing