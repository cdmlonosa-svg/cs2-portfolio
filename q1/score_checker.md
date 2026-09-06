# Part 1 - Analyze the Logic

Input: What information does the program need?
The program needs an integer value representing the student's score.

Boundary: What is the minimum valid score?
Minimum valid score: 0

Boundary: What is the maximum valid score?
Maximum valid score: 100

Possible Outputs: What outcomes can the program produce?
1. Invalid score.
2. Outstanding
3. Very Satisfactory
4. Satisfactory
> 5. Needs Improvement

Selection Pattern: Which part uses a boundary condition?
The if condition `score < 0 or score > 100` is used to determine whether the score falls outside the limit.

Selection Pattern: Which part uses multiple decision paths? 
The `elif` and `else` statements check the input (`>= 90`, `>= 80`, `>= 75`, and the remaining scores) to classify valid scores into their appropriate performance..


