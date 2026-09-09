name = input("Enter student name: ").strip()
if not name:
    print("REGISTRATION NOT ACCEPTED")
    print("Student name is required.")
else:
    age_input = input("Enter age: ").strip()
    try:
        age = int(age_input)
        if age < 11 or age > 18:
            print("REGISTRATION NOT ACCEPTED")
            print("Age must be from 11 to 18.")
        else:
            grade_input = input("Enter grade level (7-12): ").strip()
            valid_grades = ["7", "8", "9", "10", "11", "12"]
            if grade_input not in valid_grades:
                print("REGISTRATION NOT ACCEPTED")
                print("Invalid grade level.")
            else:
                grade_level = int(grade_input)
                email = input("Enter email: ").strip()
                if "@" not in email or "." not in email:
                    print("REGISTRATION NOT ACCEPTED")
                    print("Invalid email address.")
                else:
                    reg_code = input("Enter registration code (6 characters): ").strip()
                    if len(reg_code) != 6:
                        print("REGISTRATION NOT ACCEPTED")
                        print("The registration code must contain exactly 6 characters.")
                    else:
                        print("-------------------------------")
                        print("REGISTRATION ACCEPTED")
                        print("-------------------------------")
                        print(f"Student: {name}")
                        print(f"Age: {age}")
                        print(f"Grade Level: {grade_level}")
                        print(f"Email: {email}")
                        print(f"Registration Code: {reg_code}")
    except ValueError:
        print("REGISTRATION NOT ACCEPTED")
        print("Age must be a number.")
      
#LEARNING RESOURCE:
#Code, B. [Bro Code]. (2024, June 29). Learn Python EXCEPTION HANDLING in 5 minutes! 🚦 [Video]. YouTube. https://www.youtube.com/watch?v=V_NXT2-QIlE
