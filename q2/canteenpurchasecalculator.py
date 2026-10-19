def calculate_total(price, quantity):
    return price * quantity
  
def calculate_change(payment, total):
    """Calculates change or checks for shortage."""
    return payment - total
price = float(input("Enter item price: "))
quantity = int(input("Enter quantity: "))
amount_paid = float(input("Enter amount paid: "))

total_cost = calculate_total(price, quantity)

change = calculate_change(amount_paid, total_cost)

print(f"Total Cost: PHP {total_cost}")

if change < 0:
    print(f"Additional Amount Needed: PHP {change * -1:.2f}")
else:
    print(f"Change: PHP {change:.2f}")
  # Documentation Questions:
# 1. What does each function do?
# calculate_total() multiplies the item price by the quantity and returns the total cost.
# calculate_change() takes the payment and total cost, subtracts the total from payment to find the change, or handles insufficient funds.
#
# 2. What is the difference between the parameters price and quantity and the actual arguments passed to the function?
# Parameters (price, quantity) are the placeholder variables defined in the function header.
# Arguments are the actual values or variables passed into the function when it is called.
#
# 3. Where is the returned total stored, and how is it reused?
# The returned total is stored in a variable (like 'total_cost') in the main program and then passed as an argument into calculate_change().
#
# 4. Why is it useful to separate total calculation from change calculation?
# It keeps the code readable and easier to debug or independently reuse parts of the program.
