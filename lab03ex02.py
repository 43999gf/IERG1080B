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

def decode_sensor_data(codes=[0, 1, 3, 5, 4]):

    critical_count = 0

    for code in codes:
        status = ("OK", "WARNING", "ERROR", "CRITICAL", "UNKNOWN")
        # Use match-case here

        match code:
            case 0:
                print(f"Code {code}: {status[0]}")
            case 1:
                print(f"Code {code}: {status[1]}")
            case 2:
                print(f"Code {code}: {status[2]}")
            case 3 | 4:
                print(f"Code {code}: {status[3]}")
                critical_count += 1
            case _:
                print(f"Code {code}: {status[4]}")
            
                

    print(f"Critical sensors: {critical_count}")


if __name__ == "__main__":
    decode_sensor_data()
