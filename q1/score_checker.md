# Clean Decision Code Makeover: Student Score Checker
**Name: Carl Dwayne M. Loñosa**  
**Section: 8-Dahlia** 
---
## Activity Overview

In this activity, I improved a Student Score Checker program by applying proper coding standards and
selection structures.
The program accepts a student score from 0 to 100 and determines the appropriate classification.

The classifications are:
| Score | Classification |
|---:|---|
| 90–100 | Outstanding |
| 80–89 | Very Satisfactory |
| 75–79 | Satisfactory |
| 0–74 | Needs Improvement |

Scores below 0 or above 100 are considered invalid.

---

# Part 1 - Analyze the Logic

## Input  
What information does the program need?
> The program needs an integer value representing the student's score.

## Valid Range
**Minimum valid score:**  
Minimum valid score: 0

**Maximum valid score:**  
Maximum valid score: 100

## Possible Outputs
1. Invalid score.
2. Outstanding
3. Very Satisfactory
4. Satisfactory
5. Needs Improvement

## Boundary condition
> The if condition `score < 0 or score > 100` is used to determine whether the score falls outside the limit.

## Multiple decision paths
> The `elif` and `else` statements check the input (`>= 90`, `score >= 80 and score < 90`, `score >= 75 and score < 80`, and the remaining scores) to classify valid scores into their appropriate performance.

---

## Part 2 - Flowchart
<img width="967" height="710" alt="image" src="https://github.com/user-attachments/assets/700b7e08-c796-4865-85d9-6880a575798c" />

---

# Part 3 - Pseudocode  
START  
INPUT score  
IF score < 0 OR score > 100 THEN  
DISPLAY "Invalid score."  
ELSE IF score >= 90 THEN  
DISPLAY "Outstanding"  
ELSE IF score >= 80 AND score < 90 THEN  
DISPLAY "Very Satisfactory"  
ELSE IF score >= 75 AND score < 80 THEN  
DISPLAY "Satisfactory"  
ELSE  
DISPLAY "Needs Improvement"  
ENDIF  
END  

---

# Part 4 - Clean Code Implementation  
## ![Score Checker Source Code](score_checker.py)

---
# Part 5 - Testing
| Test | Input | Purpose | Expected Output | Actual Output | Result |
|---|---:|---|---|---|---|
| 1 | -1 | Below minimum | Invalid score. | Invalid score. | PASS |
| 2 | 0 | Minimum boundary | Needs Improvement | Needs Improvement | PASS |
| 3 | 74 | Below Satisfactory boundary | Needs Improvement | Needs Improvement | PASS |
| 4 | 75 | Satisfactory boundary | Satisfactory | Satisfactory | PASS |
| 5 | 80 | Very Satisfactory boundary | Very Satisfactory |  Very Satisfactory | PASS |
| 6 | 90 | Outstanding boundary | Outstanding | Outstanding | PASS |
| 7 | 100 | Maximum boundary | Outstanding | Outstanding | PASS |
| 8 | 101 | Above maximum | Invalid score. | Invalid score. | PASS |




