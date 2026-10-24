def calculate_average(score1, score2, score3):
  return (score1 + score2 + score3) / 3
  
def get_performance(average):
  if average >= 85:
    return "Mastery"
  elif average >= 70:
    return "Developing"
  else:
    return "Needs Review"
    
def is_eligible(average, completed_tasks):
  return average >= 85 and completed_tasks >= 3

score1 = float(input("Enter score 1: "))
score2 = float(input("Enter score 2: "))
score3 = float(input("Enter score 3: "))
completed_tasks = int(input("Enter number of completed tasks: "))
average = calculate_average(score1, score2, score3)
performance = get_performance(average)
eligible = is_eligible(average, completed_tasks)

print(f"Average: {average}")
print(f"Performance: {performance}")
print(f"Eligible for Challenge: {eligible}")

#DOCUMENTATION QUESTIONS
# 1. Which function returns a number, which returns a string, and which returns a Boolean?
# calculate_average() returns a number, get_performance() returns a string, and is_eligible() returns a Boolean value.
# 2. Explain how the average moves from calculate_average() into get_performance().
# calculate_average() calculates the result and returns it to the main program, where it is stored in 'average' (a variable). Then, the 'average' variable is passed as an argument into get_performance().
# 3. What happens when a student has a high average but has completed fewer than three tasks?
# The student will still receive a high performance category like "Mastery", but is_eligible() will return False because the eligibility condition requires both an average of at least 85 and at least 3 completed tasks.
# 4. Why is return more appropriate than simply printing the result inside each function?
# Using return allows the functions to pass their output back to the main program so it can be saved in variables and reused in other parts of the code. If a function only prints the result, that data cannot be passed into another function or used for other checks.
