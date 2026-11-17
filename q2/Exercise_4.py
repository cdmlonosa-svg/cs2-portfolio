# Exercise 4. Multiplication Table Generator

# This defines a function named show_table with given_number as a parameter
def show_table(number):
# This creates a loop using i (i is a variable for each number) starting from 1 to 11 (excluding 11, so it's from 1 to 10).
# It has an increment of 1 because it is the default increment.
    for i in range(1, 11):
# This multiplies the given number from the user by i with product as a variable.
        product = number * i
# This prints the given number mutiplied by i is equal to product
        print(f"{number} x {i} = {product}")

# This asks the user for a number.
number = int(input("Enter a number: "))

# This calls the function and pass the user's number as an argument. This prints the multiplication table of the given number.
show_table(number)
