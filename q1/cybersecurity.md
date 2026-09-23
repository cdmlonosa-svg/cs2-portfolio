# Fundamentals of Cybersecurity and Data Privacy
**Activity:** PSHS Secure Club Registration System
**Name:** Your Name
**Section:** Your Section
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

**Case Number:**
**Case Title:**
> Briefly describe the case here.
---
### 1. What cybersecurity threat is shown?
> Write your answer here.
### 2. What warning signs make the situation suspicious?
> Write your answer here.
### 3. What may be affected?
Check or describe all that apply:
- Data
- Account
- Application
- Device
- Network
- Financial information
> Explain your answer.
### 4. What information could be exposed or misused?
> Write your answer here.
### 5. What should the user do to reduce the risk?
> Write your answer here.
---
# Part B - Data Privacy and Secure Data Capture
A proposed Club Registration System wants to collect the following information.
Determine whether each item is really necessary.
| Data | Collect / Do Not Collect | Reason |
|---|---|---|
| Student Name | | |
| Section | | |
| Club Choice | | |
| School Email | | |
| Attendance Status | | |
| Password | | |
| OTP | | |
| Home Address | | |

| Parent Bank Account | | |
---
## Privacy Question
Why is it safer to collect only information that the program actually needs?
> Write your answer here.
---
# Part C - Security-Focused Validation Rules
Complete the table before writing your program.
| Data Captured | Expected Input | Possible Risk | Invalid Input Example | Validation Rule | Error
Message |
|---|---|---|---|---|---|
| Student Name | | | | | |
| Section | | | | | |
| Club Choice | | | | | |
| School Email | | | | | |
| Attendance Status | | | | | |
---
## Secure Data Capture Questions
### 1. What should your program accept?
> Write your answer here.
### 2. What should your program reject?
> Write your answer here.
### 3. How do your validation rules help reduce incorrect or unsafe input?
> Write your answer here.
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
# Paste your final program here.
```
---
## Security Practices Applied
### Required Input
> Explain how you handled blank input.
### Allowed Values
> Explain which fields accept only predefined values.
### Format Check
> Explain your simple email validation rule.
### Error Messages
> Explain why clear error messages are useful.
### Data Minimization
> Explain what information you intentionally did NOT collect and why.
---
# Part E - Testing and Reflection
## Testing
| Test | Input Situation | Expected Output | Actual Output | Result |
|---:|---|---|---|---|
| 1 | All data valid | | | |
| 2 | Blank student name | | | |
| 3 | Invalid section | | | |

| 4 | Invalid club choice | | | |
| 5 | Email missing `@` | | | |
| 6 | Email missing `.` | | | |
| 7 | Invalid attendance status | | | |
| 8 | Different valid inputs | | | |
Use:
- **PASS** if the actual result matches the expected result.
- **FAIL** if it does not.
---
# Reflection
### 1. What is one cybersecurity threat that can affect an application or user?
> Write your answer here.
### 2. How can users reduce the risk of phishing or suspicious messages?
> Write your answer here.
### 3. How can validation rules improve the security of user input?
> Write your answer here.
### 4. Why should a program avoid collecting unnecessary personal information?
> Write your answer here.
### 5. How did SG7's input validation concepts become security practices in SG8?
> Write your answer here.
---
# Files for This Activity
- [`secure_registration.py`](secure_registration.py)
- `cybersecurity.md`
---
[← Back to Main Portfolio](../README.md)
