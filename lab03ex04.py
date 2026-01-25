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
 Date         : 25/1/2026
'''

def create_student_dict(data_str):
    """
    Convert input string to dictionary of students and their grades.
    
    Args:
        data_str: String in format "name1:grade1,grade2;name2:grade3,grade4"
    
    Returns:
        Dictionary with names as keys and lists of grades as values
    """
    student_dict = {}
    # TODO: Parse the input string and populate student_dict
    # Example: "Alice:85,90;Bob:92,88" -> {'Alice': [85, 90], 'Bob': [92, 88]}
    # Hint: Use .split with proper delimiter and loops
    students = data_str.split(';')
    
    for entry in students:
        if ':' in entry:
            name, grades_str = entry.split(':')
            grades = [int(g) for g in grades_str.split(',')]
            student_dict[name] = grades

    return student_dict

def calculate_averages(student_dict):
    """
    Calculate average grade for each student.
    
    Args:
        student_dict: Dictionary of students and their grades
    
    Returns:
        Dictionary with names as keys and average grades as values
    """
    averages = {}
    # TODO: Calculate average for each student
    # Round averages to 2 decimal places
    for name, grades in student_dict.items():
        averages[name] = sum(grades) / len(grades)
    return averages

def find_above_threshold(averages, threshold):
    """
    Find students with average grade above threshold.
    
    Args:
        averages: Dictionary of student averages
        threshold: Minimum grade threshold
    
    Returns:
        List of student names above threshold
    """
    above_threshold = []
    # TODO: Find students with average > threshold
    for name, avg in averages.items():
        if avg > threshold:
            above_threshold.append(name)
    return above_threshold

def main():
    input_line = input().strip()
    
    if ' ' in input_line:
        data_str, threshold_str = input_line.rsplit(' ', 1)
        threshold = float(threshold_str)
    else:
        data_str = input_line
        threshold = 0.0

    student_dict = create_student_dict(data_str)
    averages = calculate_averages(student_dict)
    above_threshold = find_above_threshold(averages, threshold)

    print(f"Student grades: {student_dict}")
    print("Average grades:")
    for name, avg in averages.items():
        print(f"{name}: {avg:.2f}")
    print(f"Students above threshold: {above_threshold}")

if __name__ == "__main__":
    main()