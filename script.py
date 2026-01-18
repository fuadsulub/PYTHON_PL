# data types
# 1: integer = whole number without decimal point
# a = 10
# print(a)

# 2: Float is with decimal point
# pi = 3.14
# print(pi)

# 3: Strings is characters
# name = 'fud'
# print(name)

# # 4: boolean is true or false or on/of

# is_valid = False
# print(is_valid)

# is_valid = True
# print(is_valid)

# # Basic operators
# # Arithmetic Operators is mathimetical calculation

# a = 10
# b = 2
# print(a+b)

# print(a*b)

# print(a/b)

# print(a//b)  # round nearest number

# print(a-b)

# print(a % b)


# # Comparison operators
# a = 5
# b = 4
# print(a > b)  # greater than
# print(b > a)
# print(a < b)  # less than
# print(b < a)

# # Logical Operators
# c = False
# d = True
# print(c or d)
# print(c and d)
# print(not d)

# # control flow
# age = 70
# if age < 18:
#     print('minor')
# elif age < 65:
#     print('Adult')
# else:
#     print('sinior')

# # examples

# da = 80
# if da <= 18:
#     print('minor')
# elif da < 65:
#     print('Adult')
# else:
#     print('Very old')

# hoyo = 25
# if hoyo > 30:
#     print('Qangadh')
# elif hoyo > 23:
#     print('wu qangadhay')
# else:
#     print('duq')

# loops are used to execute block of code repeatedly
# for loop
# for i in range(1, 6):
#     print(i)

# for i in range(1, 5):
#     print(i)

# # while loop
# count = 1
# while count < 5:

#     print(count)
#     count += 1

# count = 5
# while count > 0:
#     print(count)
#     count -= 1

# list Comprehensions traditional way
# square = []
# for i in range(10):
#     square.append(i * i)
#     print(square)

# list comprehensions
# squares = [i * i for i in range(10)]
# print(squares)

# jibar = [fuad*fuad for fuad in range(1, 11)]
# print(jibar)

# Data structures

# Data structures allow us to organize and store data in various ways
# 1: lists
# fruites = ["apple", 'banana', 'cherry']
# print(fruites)
# print(fruites[0])
# fruites.append('mango')
# print(fruites)

# vegetables = ['carote', 'cabege', 'tomato']
# print(vegetables)
# vegetables.append('botato')
# print(vegetables)

# 2:tubles is ordered but immutable (can not changeable) collections
# coordinates = (10, 20)
# print(coordinates)

# coordinates = (25, 55, 22)
# print(coordinates[0])

# 3:sets Unordered collections of unique items
# unique_numbers = {1, 2, 3, 4, 5, 4, 5}
# print(unique_numbers)

# 4:Dictionary has key-value pairs
# person = {'name': 'fuad', 'age': '28', 'Birth_day': 1998}
# print(person)
# person['city'] = 'yocale'
# print(person)
# print(person['Birth_day'])

# 5:string manipulation and formating
# greeting = "hello"
# name = 'fuad'
# message = greeting + ' ' + name
# print(message)
# message = f"{greeting}, {name}!"
# print(message)

# salaan = "asc ww"
# magac = 'Hooyo'
# fariin = salaan + ' ' + magac
# print(fariin)
# fariin = f"{salaan}, {magac}!"
# print(fariin)

# 5.1 String method building functions that changs Appearance

# print(message.upper())
# print(message)
# print(fariin.upper())
# print(fariin)
# print(message.lower())
# print(message)

# print(fariin.split(','))
# print(fariin)

# 6: funtions & modeules
# functions are reusable block of code that perform specific task


# from datetime import date
# import math


# def greet(name):
#     return f"Hello, {name}"


# print(greet('fuad'))


# def add(a, b):

#     return a+b


# print(add(4, 5))


# def multiply(a, b):
#     return a*b


# print(multiply(2, 5))


# def square(a):
#     return a*a


# print(square(5))


# def module(a, b):
#     return a % b


# print(module(5, 2))


# def division(a, b):
#     return a//b


# print(division(12, 6))

# # lambda expressions


# def multiply(a, b): return a*b


# print(multiply(3, 4))


# def add(a, b): return a+b


# print(add(2, 8))


# def substraction(a, b): return a-b


# print(substraction(10, 30))

# # 6.1 modules
# print(math.sqrt(26))

# print(math.remainder(6, 6))

# print(date.today())

# 7: file  I/O & exception handling
# 7.1 writting file
# with open('example.txt', 'w') as file:
#     file.write('hello ,file !')

# 7.2: file reading

# with open('example.txt', 'r') as file:
#     content = file.read()
#     print(content)

# 7.3: using try/except block for Roboust error handling
# try:
#     number = int(input('enter a number:'))
#     print(f"You entered {number}")
# except ValueError:
#     print("that's not valid number!")

# number = int(input("enter is number:"))
# print(f"you entered:{number}")

# 8: Object-oriented programming (OOP)
# oop is a progrmming paradigm that organizes code around objects-self-contained.

# 8.1 Abstraction hides complex details while exposing only what is necessary.


# class RemoteControl:

#     def change_channel(self, channel):
#         return f"changing channel to{channel}."

#     def adjust_volume(self, volume):
#         return f"setting volume to {volume}"


# if __name__ == "__main__":
#     remote = RemoteControl()
#     print(remote.change_channel('Al Jazeera'))

#     print(remote.adjust_volume(30))

# class CarStart:

#     def car_start(self, start):
#         return f"car started now {start}."

#     def car_gas(self, gas):
#         return f"car gas is {gas}"


# if __name__ == "__main__":
#     drving = CarStart()
#     print(drving.car_start("going to yocale"))
#     print(drving.car_gas('full'))

# 8.2 Encapsulation hundles data and methods into one class, restricting direct access to some data

class BankAccount:

    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return f"deposit ${amount}. New Balance ${self._balance}"

        return "deposit Amount must be positive "

    def withdraw(self, amount):
        if amount > self._balance:
            return f'Your Balance Insufficient'
        self._balance -= amount
        return f'withdraw ${amount}. new balance: ${self._balance}'

    def get_balance(self):
        return f"{self.owner}'s balance: ${self._balance}"


if __name__ == "__main__":
    account = BankAccount('Your', 1000)
    print(account.deposit(500))
    print(account.withdraw(1000))
    print(account.get_balance())
