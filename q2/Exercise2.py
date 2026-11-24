# Exercise 2: Travel Destination Manager

# This creates a list named "destinations" with Cebu, Manila, Davao, Baguio, and Palawan in it.
# Cebu = index 0, Manila = index 1, Davao = index 2, Baguio = index 3, Palawan = index 4
destinations = ["Cebu", "Manila", "Davao", "Baguio", "Palawan"]

# This displays a heading before listing the travel destinations.
print("All Travel Destinations:")
# This starts a for loop where for every destination (destination is a variable name) in the list destinations, each destination will be displayed.
for destination in destinations:
# This prints each destination.
    print(destination)
  
# This creates a blank space to make the outputs cleaner.
print()

# This displays a heading before displaying the sliced destinations.
print("Sliced Destinations (Index 1 to Index 3:)")
# This displays each destination from index 1 (Manila) to index 4 (Palawan) but index 4 isn't included.
# So, index 1 to index 3 will be displayed. Which are Manila, Davao, and Baguio respectively.
print(destinations[1:4])

# This creates a blank space to make the outputs cleaner.
print()

# This asks the user to enter a destination.
travel_destination = str(input("Enter a destination: "))

# This checks if the user's input (travel_destination) is in the list "destinations"
if travel_destination in destinations:
# This displays that travel_destination exists in the list.
  print(f"{travel_destination} exists in the list!")
# This will run if travel_destination isn't in destination
else:
# This displays that travel_destination does not exist in the list.
  print(f"{travel_destination} does not exist in the list.")
  
# This creates a blank space to make the outputs cleaner.
print()

# This updates the list "destinations" by replacing Davao, which is in index 2, with Iloilo.
destinations[2] = "Iloilo"
# This displays a heading before displaying the updated list.
print("Updated List: ")
# This displays the updated list.
print(destinations)
