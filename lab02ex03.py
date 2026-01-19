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
 Date         : 15/1/2026
'''

def analyze_registrations(registered_a=("S1001", "S1002", "S1003", "S1002", "S1004"), 
                          registered_b=("S1003", "S1005", "S1004", "S1006")):

    # The initial print formats are given to you. 
    # Add your code to compute the required values
    # Modify the print statement to print out the required variables

    print("=== Initial Analysis ===")
    print(f"Period A registrations: {registered_a}")
    print(f"Period B registrations: {registered_b}")
    print(f"Total registrations in Period A: {len(registered_a)}")
    print(f"Total registrations in Period B: {len(registered_b)}")
    print()
    
    print("=== Set Operations ===")
    set_a = set(registered_a)
    set_b = set(registered_b)
    sorted_a = sorted(set_a)
    sorted_b = sorted(set_b)
    intersection = sorted(set_a & set_b)
    union = sorted(set_a | set_b)
    difference = sorted(set_a - set_b)
    symmetric_difference = sorted(set_a ^ set_b)
    
    print(f"Unique students in Period A: {sorted_a}")
    print(f"Unique students in Period B: {sorted_b}")
    print(f"Registered in both periods: {intersection}")
    print(f"All unique students: {union}")
    print(f"Only in Period A: {difference}")
    print(f"Only in one period: {symmetric_difference}")
    print()
    
    mix = registered_a + registered_b
    count = mix.count("S1002")
    S1001_in_a = "S1001" in registered_a
    
    print("=== Tuple Operations ===")
    print(f"All registrations combined: {mix}")
    print(f"First 3 from Period A: {registered_a[:3]}")
    print(f"Student S1002 appears {count} times in all registrations") # Replace ?? with no. of reg.
    print(f"Student S1001 is in Period A: {S1001_in_a}") # Print True/False

    print()


if __name__ == "__main__":
    
    analyze_registrations()
