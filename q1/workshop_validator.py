name = input("Enter student name: ").strip()
if not name:
    print("REGISTRATION NOT ACCEPTED")
    print("Student name is required.")
else:
    age = input("Enter age: ").strip()
    try:
        ageInt = int(age)
        if ageInt < 11 or ageInt > 18:
            print("REGISTRATION NOT ACCEPTED")
            print("Age must be from 11 to 18.")
        else:
            grades = input("Enter grade level (7-12): ").strip()
            validGrades = ["7", "8", "9", "10", "11", "12"]
            if grades not in validGrades:
                print("REGISTRATION NOT ACCEPTED")
                print("Invalid grade level.")
            else:
                gradeInt = int(grades)
                email = input("Enter email: ").strip()
                if "@" not in email or "." not in email:
                    print("REGISTRATION NOT ACCEPTED")
                    print("Invalid email address.")
                else:
                    regCode = input("Enter registration code (6 characters): ").strip()
                    if len(regCode) != 6:
                        print("REGISTRATION NOT ACCEPTED")
                        print("The registration code must contain exactly 6 characters.")
                    else:
                        print("------------------------------")
                        print("REGISTRATION ACCEPTED")
                        print("------------------------------")
                        print(f"Student: {name}")
                        print(f"Age: {age}")
                        print(f"Grade Level: {grades}")
                        print(f"Email: {email}")
                        print(f"Registration Code: {regCode}")
    except ValueError:
        print("REGISTRATION NOT ACCEPTED")
        print("Age must be a number.")

#ADDITIONAL LEARNING RESOURCE
#Code, B. [Bro Code]. (2024, June 29). Learn Python EXCEPTION HANDLING in 5 minutes! 🚦 [Video]. YouTube. https://www.youtube.com/watch?v=V_NXT2-QIlE

