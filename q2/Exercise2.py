# Exercise 2: Travel Destination Manager
destinations = ["Cebu", "Manila", "Davao", "Baguio", "Palawan"]

print("All Travel Destinations:")
for destination in destinations:
    print(destination)
  
# This creates a blank space to make the outputs cleaner.
print()

print("Sliced Destinations (Index 1 to Index 3:)")
print(destinations[1:4])

# This creates a blank space to make the outputs cleaner.
print()

place = str(input("Enter a destination: "))

if place in destinations:
  print(f"{place} exists in the list!")
else:
  print(f"{place} does not exist in the list.")
  
# This creates a blank space to make the outputs cleaner.
print()

destinations[2] = "Iloilo"
print("Updated List: ")
print(destinations)
