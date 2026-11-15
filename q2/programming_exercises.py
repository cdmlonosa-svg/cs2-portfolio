# Exercise 1: Count Even Numbers

# In this line, it creates a loop using i (i is a variable for each number) starting from 1 to 21 (excluding 21, so it's from 2 to 20) with an increment of 2.
for i in range(2, 21, 2):
#This prints each even number.
  print(i)

# Exercise 2: The Countdown Timer

# This sets 10 as the starting point because the countdown timer starts at 10.
number = 10
# This starts the loop and checks a condition (while number is greater than 0). The loop will continue as long as number is greater than 0.
while number > 0:
# This prints each number greater than 0.
    print(number)
# This subtracts 1 from the current number (It is the same as number = number - 1). 
# Without this, the code will loop infinitely because the number stays the same without it.
    number -= 1
# This prints the words, "Time is up!" after the countdown timer ends.
print("Time is up!")

# Exercise 3: Skip Multiples

# In this line, it creates a loop using i (i is a variable for each number) starting from 1 to 16 (excluding 16, so it's from 1 to 15).
# It has an increment of 1 because it is the default increment.
for i in range(1, 16):
# This checks if the remainder of i divided by 3 is 0. If its remainder isn't 0, then the code skips the if block to print i.
  if i % 3 == 0:
# If the remainder of i is 0, then all the lines written below continue will be skipped so i won't be printed
    continue
# This prints i after it goes through the if block without a remainder of 0.
  print(i)
  
# Exercise 4. Multiplication Table Generator

#This defines a function named multiplication_table with given_number as a parameter
def multiplication_table(given_number):
# This creates a loop using i (i is a variable for each number) starting from 1 to 11 (excluding 11, so it's from 1 to 10).
# It has an increment of 1 because it is the default increment.
    for i in range(1, 11):
# This multiplies the given number from the user by i with product as a variable.
        product = given_number * i
 #This prints the given number mutiplied by i is equal to product
        print(f"{given_number} x {i} = {product}")

# This asks the user for a number.
given_number = int(input("Enter a number: "))

# This calls the function and pass the user's number as an argument. This prints the multiplication table of the given number.
multiplication_table(given_number)
