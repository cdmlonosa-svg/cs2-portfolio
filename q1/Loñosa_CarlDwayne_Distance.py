import math
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))
d = pow(x2 - x1, 2) + pow(y2 - y1, 2)
distance = round(math.sqrt(d), 2)
print(f"The distance between the two points is: {distance}")
#REFLECTION
#The math library simplified my program by providing me with built-in mathematical functions, which made my code simpler and easier to understand.
#pow() helped me because it raised the difference between the x and y coordinates
#sqrt() helped me because it computed the square root of the sum of the squared differences.
#If pow() wasn' t available, I would've used ** 2 (example: (x2 - x1) ** 2).
#If sqrt() wasn' t available, I would've used ** 0.5 (example: (d) ** 0.5). 
