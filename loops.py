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

# responses = {}
# polling_active = True
# while polling_active:
#     name  = input("\nWhat is your name? ")
#     response = input("Which mountain would you like to climb one day? ")
#     responses[name] = response
#     repeat = input("Would you like to let another person respond? (yes/ no)")
#     if repeat == "no":
#         polling_active = False
# print("\n----Poll Result---")
# for name, response in responses.items():
#     print(f"{name} would like to climb {response}.")


# from typing import Callable

# def my_decorator(func: Callable[[], None])-> Callable[[], None]:
#     def wrapper():
#         print("Something is happening before the function is called")
#         func()
#         print("Something is happening after the function is called")
#         return wrapper
    
#     @my_decorator
#     def say_hello():
#         print("Hello")
        
#     say_hello(hello)
    
    
    
# from typing import Callable

# def my_decorator(func: Callable[[int], None])-> Callable[[int], None]:
#     def wrapper(num1: int)->None:
#         print("Something before the function is called.")
#         func(num1)
# #         print("Something is happening after the function is called.")
# #         return wrapper
# # @my_decorator
# # def say_hello(num1: int)-> None:
# #     print(num1)
    
# # say_hello(100)


# class ToyCar:
#     def __init__(self):
#         self.speed = 10
#         self.fuel = 100
        
#     def move(self):
#         if self.fuel > 0:
#             self.speed +=10
#             self.fuel -=10
#             print("The Car is Moving")
#         else:
#             print("Out Of Fuel")
            
#         def stop(self):
            
#             self.speed = 0
#             print("The Car has Stopped")
            
            


# class Account:
#     def __init__(self, acc_no, acc_pass):
#         self.acc_no = acc_no
#         self.acc_pass = acc_pass
        
#     def reset_pass(self):
#         print(self.__reset_pass)
        
# acc1 = Account("12345", "abcd")
# print(acc1.acc_no)
# print(acc1.__reset_pass())


# with open("abc1.txt", "w")as f:
#     data = f.write("We love Programming")
#     print(data)
# class Car:

#     def __init__(self, type):
#         self.type = type
        
# @staticmethod
# def start():
#     print("Car Started.")
    
# @staticmethod
# def end():
#     print("Car Stopped.")
    
    
# class ToyotaCar(Car):
#     def __init__(self, name):
#         super().__init__(type)
#         self.name = name
#         super().start()
        
# car1 = ToyotaCar("Prius", "Electric")
# print(car1.type)
    

# print(5/2)

# x = 5
# y = 2
# print(x // y)

# fruits = ["Apple", "Banana", "Cherry"]
# for index, fruit in enumerate(fruits):
#     print(index, fruit)


# my_list = [1, 2, 3, 4, 5]
# print(7 in my_list)
    
print(type([]) == list)