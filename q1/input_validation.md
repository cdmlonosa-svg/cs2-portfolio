# Input Validation and Output Verification    
**Activity:** PSHS Workshop Registration Validator    
**Name:** Carl Dwayne M. Loñosa    
**Section:** Dahlia    
**Quarter:** 1    
---
## Activity Overview
In this activity, I created a program that validates information entered into a PSHS workshop registration
system.
The program checks whether user input satisfies specific requirements before accepting the registration.
The program validates:
- student name
- age
- grade level
- email address and
- registration code.

---
# Part A - Validation Requirements
Complete the table below before writing your program.
| Data Captured | Expected Input | Validation Type | Invalid Input Example | Validation Rule | Error Message |
|---|---|---|---|---|---|
| Student Name | Non-empty string | Presence | `""` (Blank) | Cannot be empty | Student name is required. |
| Age | Integer (11–18) | Data Type & Range | `fourteen` or `25` | Must be a number between 11 and 18 | Age must be a number. / Age must be from 11 to 18. |
| Grade Level | Integer (7–12) | Acceptable Value | `13` | Must be 7, 8, 9, 10, 11, or 12 | Invalid grade level. |
| Email Address | String with `@` and `.` | Pattern | `studentpshs.edu.ph` | Must include both '@' and '.' characters | REGISTRATION NOT ACCEPTED |
| Registration Code | String | Length | `ABC` (3 chars) | Must contain exactly 6 characters | The registration code must contain exactly 6 characters. |

---
## Validation Questions
### 1. Why should the student name not be blank?
> It shouldn't be blank because the name is required.
### 2. Why should age be checked for both data type and range?
> The data type is checked to ensure that the age is an integer and the range is checked because there is an age limit.
### 3. Why should grade level only accept specific values?
> Because it's strictly PSHS grade levels.
### 4. What format requirements did you use for the email address?
> A simple structural pattern check that requires "@" and "."
### 5. What length requirement did you use for the registration code?
> Exactly 6 characters
---
# Part B - Program Design
Before writing your program, create either a **flowchart or pseudocode** showing its logic.
## Pseudocode

```text
START
    INPUT name
    IF name is empty THEN
        DISPLAY "Student name is required."
        EXIT
    
    INPUT age_str
    TRY convert age_str to integer (age)
    IF conversion fails THEN
        DISPLAY "Age must be a number."
        EXIT
    IF age < 11 OR age > 18 THEN
        DISPLAY "Age must be from 11 to 18."
        EXIT

    INPUT grade_str
    TRY convert grade_str to integer (grade)
    IF conversion fails OR grade not in [7, 8, 9, 10, 11, 12] THEN
        DISPLAY "Invalid grade level."
        EXIT

    INPUT email
    IF "@" not in email OR "." not in email THEN
        DISPLAY "REGISTRATION NOT ACCEPTED"
        EXIT

    INPUT code
    IF length of code != 6 THEN
        DISPLAY "The registration code must contain exactly 6 characters."
        EXIT

    DISPLAY "------------------------------"
    DISPLAY "REGISTRATION ACCEPTED"
    DISPLAY "------------------------------"
    DISPLAY name
    DISPLAY age
    DISPLAY grades
    DISPLAY email
    DISPLAY code
END

```

---
# Part C - Program Implementation
## Programming Language
>Python
## Source Code File
[`workshop_validator.py`](workshop_validator.py)
## Final Code
```python
# name = input("Enter student name: ").strip()
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
```

---
## Validation Techniques Used
### Presence Validation
> I used presence validation in the student name input to verify that it isn't empty.
### Data Type Validation
> I used data type validation in the age and grade level inputs using a try-except structure.
### Range Validation
> I used range validation in the age input.

### Acceptable Value Validation
> I used acceptable validation in the grade level to allow only PSHS grade levels.

### Pattern Validation
> I used pattern validation in the email input to check if it contains both "@" and "."
### Length Validation
> I used length validation in the registration code because it has to be strictly 6 characters long.
---
# Part D - Testing
Test your program using both valid and invalid inputs.
| Test | Input / Condition | Validation Being Tested | Expected Output | Actual Output | Result |
|---:|---|---|---|---|---|
| 1 | All inputs valid (`Carl`, `13`, `8`, `carl@example.com`, `CS2026`) | Normal case | REGISTRATION ACCEPTED | REGISTRATION ACCEPTED | PASS |
| 2 | Blank student name (`""`) | Presence | Student name is required. | Student name is required. | PASS |
| 3 | Age = `fourteen` | Data type | Age must be a number. | Age must be a number. | PASS |
| 4 | Age = `11` | Minimum boundary | REGISTRATION ACCEPTED | REGISTRATION ACCEPTED | PASS |
| 5 | Age = `18` | Maximum boundary | REGISTRATION ACCEPTED | REGISTRATION ACCEPTED | PASS |
| 6 | Age = `10` | Range | Age must be from 11 to 18. | Age must be from 11 to 18. | PASS |
| 7 | Grade Level = `13` | Acceptable value | Invalid grade level. | Invalid grade level. | PASS |
| 8 | Email = `studentpshs.edu.ph` | Pattern | REGISTRATION NOT ACCEPTED | REGISTRATION NOT ACCEPTED | PASS |
| 9 | Registration Code = `ABC` | Length | The registration code must contain exactly 6 characters. | The registration code must contain exactly 6 characters. | PASS |
| 10 | Registration Code = `CS2026` | Valid length | REGISTRATION ACCEPTED | REGISTRATION ACCEPTED | PASS |


---
# Part E - Output Verification

## Verification Test 1
**Input:**
```text
Name: Carl
Age: 13
Grade: 8
Email: carl@example.com
Code: CS2026




```
**Expected Output:**
```text
------------------------------
REGISTRATION ACCEPTED
------------------------------
Student: Carl
Age: 13
Grade Level: 8
Email: carl@example.com
Registration Code: CS2026


```
**Actual Output:**
```text
------------------------------
REGISTRATION ACCEPTED
------------------------------
Student: Carl
Age: 13
Grade Level: 8
Email: carl@example.com
Registration Code: CS2026


```
**Result:** PASS
**Explanation:**
> The output is correct because all inputs passed the validations.
---
## Verification Test 2
**Input:**
```text
Name: Dwayne
Age: 10
Grade: 9
Email: dwayne@example.com
Code: AB1234


```
**Expected Output:**
```text
REGISTRATION NOT ACCEPTED
Age must be from 11 to 18.


```
**Actual Output:**
```text
REGISTRATION NOT ACCEPTED
Age must be from 11 to 18.


```
**Result:** PASS 
**Explanation:**
> The output is correct because it identified that 10 (the age) is less that 11.
---
## Verification Test 3
**Input:**
```text
Name: Jerry
Age: 15
Grade: 10
Email: jerry@example.com
Code: ABC



```
**Expected Output:**
```text
REGISTRATION NOT ACCEPTED
The registration code must contain exactly 6 characters.


```
**Actual Output:**

```text
REGISTRATION NOT ACCEPTED
The registration code must contain exactly 6 characters.

```
**Result:** PASS
**Explanation:**
> The output is correct because it identified that the code is less than 6 characters.
---
---
# Reflection
Answer briefly.
### 1. Why should a program validate input before processing it?
> It prevents wrong data from corrupting records and crashing.
### 2. What is the difference between input validation and output verification?
> Input validation evaluates and filters user submissions before they enter the system, while output verification confirms that the final processed results match expectations.
### 3. Which validation technique was easiest for you to implement? Why?
> Presence validation, because I only need to check if the input is empty or not.
### 4. Which validation technique was most challenging? Why?
> Data type validation, because it's my first time using try-except in my program.
### 5. How did testing invalid inputs help you improve your program?
> Testing invalid inputs helped uncover blind spots in my program and opened new doors for possible improvement.
---
# Files for This Activity
- [`workshop_validator.py`](workshop_validator.py)
- [`input_validation.md`](input_validation.md)
---

[← Back to Main Portfolio](../README.md)
