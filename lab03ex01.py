'''
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
 Date         : 22/1/2026
'''

def check_access(records=[
    ("U1001", 4, False),
    ("U1002", 2, False),
    ("U1003", 1, True),
    ("U1004", 5, False)
]):

    granted = 0

    # TODO Edit the for loop
    for value in records:

        # TODO Add control flow logic here
        if value[2] == True:
            print(f"User {value[0]}: Access Granted")
            granted += 1
        elif value[1] >= 5:
            print(f"User {value[0]}: Access Granted")
            granted += 1
        elif value[1] >= 3:
            print(f"User {value[0]}: Limited Access")
        else:
            print(f"User {value[0]}: Access Denied")
         # TODO edit the f-string

    print(f"Total granted accesses: {granted}")


if __name__ == "__main__":
    check_access()
