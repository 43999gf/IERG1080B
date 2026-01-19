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

def print_avg(my_dict):
    """The function prints the average of int values"""
    # Modify the code here
    count = 0
    sum = 0
    result = 0
    for value in my_dict.values():
      if isinstance(value, int) and not isinstance(value, bool):
        sum += value
        count += 1
    if count == 0:
      print(0.0000)
    result = (sum / count)
    print(f"{result:.4f}")
    pass

if __name__ == "__main__":
    my_dict = {
    "Alice": 95,
    "Bob": 65,
    "Charlie": 100,
    "secret": "XYAS2",
    "myList": [42, 123, 42],
    "Sorted": False,
    }
    print_avg(my_dict) # for testing