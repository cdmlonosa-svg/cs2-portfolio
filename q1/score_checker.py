# Ask the user to input a student score
score = int(input("Enter student score: "))

# Validate that the score falls within the allowed 0-100 range
if score < 0 or score > 100:
    print("Invalid score.")

# Classify scores from 90 to 100 as Outstanding
elif score >= 90:
    print("Outstanding")

# Classify scores from 80 to 89 as Very Satisfactory
elif score >= 80 and score < 90:
    print("Very Satisfactory")

# Classify scores from 75 to 79 as Satisfactory
elif score >= 75 and score < 80:
    print("Satisfactory") 

# Classify all remaining valid scores below 75 as Needs Improvement
else:
    print("Needs Improvement")
