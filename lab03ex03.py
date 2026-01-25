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

def run_tasks(tasks=[(10, 2), (5, 0), ("8", 2), (9, 3)]):

    success = 0

    for x, y in tasks:
        # Add try-except-else-finally here
        try:
            result = x // y
        except ZeroDivisionError:
            print("Error: division by zero")
        except TypeError:
            print("Error: invalid input")
        else:
            print(f"Result: {result}")
            success += 1
        finally:
            print("=== Task finished ===")
        pass

    print(f"Successful tasks: {success}")


if __name__ == "__main__":
    run_tasks()
