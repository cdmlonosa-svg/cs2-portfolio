student_name = input("Enter student name: ").strip()
if not student_name:
    print("REGISTRATION NOT ACCEPTED")
    printError: ("Error: Student name is required.")
else:
    section = input("Enter section (Dahlia, Rosal, Ilang-Ilang, Sampaguita): ").strip()
    valid_sections = ["Dahlia", "Rosal", "Ilang-Ilang", "Sampaguita"]
    if section not in valid_sections:
        print("REGISTRATION NOT ACCEPTED")
        print("Error: Please enter a valid section.")
    else:
        club = input("Enter club (Robotics, Science, Mathematics, Programming): ").strip()
        valid_clubs = ["Robotics", "Science", "Mathematics", "Programming"]
        if club not in valid_clubs:
            print("REGISTRATION NOT ACCEPTED")
            print("Error: Please choose a valid club.")
        else:
            email = input("Enter school email: ").strip()
            if "@" not in email or "." not in email:
                print("REGISTRATION NOT ACCEPTED")
                print("Error: Please enter a valid email.")
            else:
                attendance = input("Enter attendance status (Present, Absent, Late): ").strip()
                valid_attendance = ["Present", "Absent", "Late"]
                if attendance not in valid_attendance:
                    print("REGISTRATION NOT ACCEPTED")
                    print("Error: Please enter a valid attendance status.")
                else:
                    print("------------------------------")
                    print("REGISTRATION ACCEPTED")
                    print("------------------------------")
                    print(f"Student: {student_name}")
                    print(f"Section: {section}")
                    print(f"Club: {club}")
                    print(f"Email: {email}")
                    print(f"Attendance: {attendance}")
