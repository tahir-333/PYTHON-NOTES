# name : str = input("What is your name?")                 # Input from user through console/ terminal.
# print(type(name))
# print(f"Welcome Dear {name}!")

# fruits = ["Apple", "Banana", "Cherry", "Apricot", "Mango", "Lichi"]
# print(fruits)
# print("The first three elements in the list are:" [0:3])


# input1 : str(input("What is your name?: "))
# print(input1)

# requested_toppings = ["Mushroom", "Extra Cheese"]
# if "Mushroom" in requested_toppings:
#     print("Adding Mushroom")
# if "Peppironi" in requested_toppings:
#     print("Adding Peppironi")
# if "Extra Cheese" in requested_toppings:
#     print("Adding Extra Cheese")
# print("\nFinished making your pizza!")

# alien_color = "Red"
# if alien_color == "Red":
#     print("You have earned 5 points.")
# elif alien_color == "Green":
#     print("You have earned 10 points.")
# else alien_color == "Blue":
#     print("You have earned 15 points.")

# lists = ["1st, 2nd, 3rd, 4th, 5th, 6th, 7th, 8th, 9th"]
# print(lists)



# age = input("Enter Your Age: ")
# print(age)

# A simple Python function
# def fun():
#     print("Welcome to GFG")

#Program to reverse a string
# gfg = "geeksforgeeks"
# print(gfg[::-1])


# name = "Tahir Abbas", "Usama", "Aqeel", "Amir"
# print(name)
# print(name[0:3])
# name["0"]= Amir

responses = {}
polling_active = True
while polling_active:
    name  = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb one day? ")
    responses[name] = response
    repeat = input("Would you like to let another person respond? (yes/ no)")
    if repeat == "no":
        polling_active = False
print("\n----Poll Result---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")