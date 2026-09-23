# Fundamentals of Cybersecurity and Data Privacy
**Activity:** PSHS Secure Club Registration System
**Name:** Carl Dwayne M. Loñosa
**Section:** Dahlia
**Quarter:** 1
---
## Activity Overview
In this activity, I analyzed a cybersecurity threat and developed secure data-capture rules for a simple
PSHS Club Registration System.
The goal is to create a program that collects only necessary information and accepts only correct,
expected, and appropriate input.
---
# Part A - Cybersecurity Threat Analysis
## Assigned Case

**Case Number:** Case 1
**Case Title:** Fake Login Alert
> A message claims that the student's account will be disabled and asks them to click a link and enter their
username and password.
---
### 1. What cybersecurity threat is shown?
> Phishing and credential harvesting
### 2. What warning signs make the situation suspicious?
> This message creates a false sense of urgency by claiming that their account account will be disabled, uses an unverified link, and randomly askes for sensitive and private information.
### 3. What may be affected?
Check or describe all that apply:
- Data [/]
- Account [/]
- Application []
- Device [/]
- Network []
- Financial information []
> An attacker can compromise the student's account, important data, or other important services on their device.
### 4. What information could be exposed or misused?
> The student's username and password.
### 5. What should the user do to reduce the risk?
> Do not enter the link, do not enter any private information, and report or delete the message.
---
# Part B - Data Privacy and Secure Data Capture
A proposed Club Registration System wants to collect the following information.
Determine whether each item is really necessary.
| Data | Collect / Do Not Collect | Reason |
|---|---|---|
| Student Name | Collect | Required to identify who is registering. |
| Section | Collect | Required to organize and verify section. |
| Club Choice | Collect | Required to know which club the student is joining. |
| School Email | Collect | Required for school communications. |
| Attendance Status | Collect | Required for club monitoring |
| Password | Do Not Collect | Unnecessary for a basic local registration form and creates security risks. |
| OTP | Do Not Collect | Unnecessary for this simple non-authentication activity. |
| Home Address | Do Not Collect | Unnecessary personal information and violates data minimization. |
| Parent Bank Account | Do Not Collect | Unnecessary financial data and major privacy and security risk. |
---
## Privacy Question
Why is it safer to collect only information that the program actually needs?
> Collecting only necessary data reduces the impact if a data breach occurs, protects user privacy, and minimizes security liabilities.

---
# Part C - Security-Focused Validation Rules
Complete the table before writing your program.
| Data Captured | Expected Input | Possible Risk | Invalid Input Example | Validation Rule | Error Message |
|---|---|---|---|---|---|
| Student Name | Text string | Blank input / Empty string | [blank] | Must not be blank (if not student_name:) |Error: Student name is required. |
| Section | Dahlia, Rosal, Ilang-Ilang, Sampaguita | Unauthorized or mistyped sections | Gaming | Must match a predefined list | Error: Please enter a valid section. |
| Club Choice | Robotics, Science, Mathematics, Programming | Invalid club entries | Sports | Must match a predefined list | Error: Please choose a valid club. |
| School Email | Valid school format | Missing crucial email symbols | studentpshs.edu.ph | Must contain both "@" and "." | Error: Please enter a valid email. |
| Attendance Status | Present, Absent, Late | Unexpected status values | Unknown | Must be Present, Absent, or Late | Error: Please enter a valid attendance status. |

---
## Secure Data Capture Questions
### 1. What should your program accept?
>  Only valid student names, approved sections, valid club choices, proper school emails, and correct attendance statuses.
### 2. What should your program reject?
> Blank names, invalid sections, unapproved clubs, emails missing "@" and ".", and invalid attendance statuses.
### 3. How do your validation rules help reduce incorrect or unsafe input?
> They reject incorrect, blank, or unexpected data before it can be processed or stored.
---
# Part D - Secure Program Implementation
## Program
Create a simple **PSHS Club Registration System**.
The program should collect only:
- Student Name
- Section
- Club Choice
- School Email

- Attendance Status
It should **not request passwords, OTPs, banking information, or unnecessary personal information**.
---
## Source Code File
[`secure_registration.py`](secure_registration.py)
---
## Final Code
```python
# student_name = input("Enter student name: ").strip()
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



```
---
## Security Practices Applied
### Required Input
> I used if not student_name: to reject blank inputs.
### Allowed Values
> valid_sections and valid_clubs because they're restricted to lists.
### Format Check
> I checked if the email contains both "@" and "."
### Error Messages
> Clear and descriptive rejection messages help users know why their input failed.
### Data Minimization
> Passwords, OTPs home addresses, and financial information because they are unnecessary for a club registration form.
---
# Part E - Testing and Reflection
## Testing
| Test | Input Situation | Expected Output | Actual Output | Result |
|---:|---|---|---|---|
| 1 | All data valid | Registration accepted | Registration accepted | PASS |
| 2 | Blank student name | Rejected | Rejected | PASS |
| 3 | Invalid section | Rejected | Rejected | PASS |
| 4 | Invalid club choice | Rejected | Rejected | PASS |
| 5 | Email missing `@` | Rejected | Rejected | PASS |
| 6 | Email missing `.` | Rejected | Rejected | PASS |
| 7 | Invalid attendance status | Rejected | Rejected | PASS |
| 8 | Different valid inputs | Accepted | Accepted | PASS |

---
## Reflection

### 1. What is one cybersecurity threat that can affect an application or user?
> Phishing, which tricks users into revealing credentials through fake alerts.
### 2. How can users reduce the risk of phishing or suspicious messages?
> By verifying sender identity, ignoring urgent demands, and avoiding clicking unverified links.
### 3. How can validation rules improve the security of user input?
> They ensure data integrity and prevent malformed entries from entering the system.
### 4. Why should a program avoid collecting unnecessary personal information?
> It reduces privacy exposure and limits potential damage if a security breach happens.
### 5. How did SG7's input validation concepts become security practices in SG8?
> Concepts like checking types and handling errors evolved from general programming logic into active security defenses against exploits.

---
# Files for This Activity
- [`secure_registration.py`](secure_registration.py)
- `cybersecurity.md`
---
[← Back to Main Portfolio](../README.md)
