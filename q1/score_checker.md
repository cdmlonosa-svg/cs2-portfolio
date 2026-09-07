# Clean Decision Code Makeover: Student Score Checker
**Name: Carl Dwayne M. Loñosa**  
**Section: 8-Dahlia** 
---
## Activity Overview

In this activity, I improved a Student Score Checker program by applying proper coding standards and
selection structures.
The program accepts a student score from 0 to 100 and determines the appropriate classification.

# Part 1 - Analyze the Logic

## Input  
What information does the program need?
> The program needs an integer value representing the student's score.

## Valid Range
**Minimum valid score:**  
Minimum valid score: 0

**Maximum valid score:**  
Maximum valid score: 100

## Possible Outputs:
1. Invalid score.
2. Outstanding
3. Very Satisfactory
4. Satisfactory
5. Needs Improvement

## Boundary condition?
> The if condition `score < 0 or score > 100` is used to determine whether the score falls outside the limit.

## Multiple decision paths:
> The `elif` and `else` statements check the input (`>= 90`, `>= 80`, `>= 75`, and the remaining scores) to classify valid scores into their appropriate performance.
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
## [Score Checker Source Code](./q1/score_checker.py)





