#!/usr/bin/env python

# author Ola Ajibode

# This is using Python3.  Python2 is different in some ways.  Search online to find
# the differences

# Installing Python on Windows and Mac OSX/Linux
print("Hello World")

# Variable:  A variable holds a space in memory and can hold a value
# d is the name of the variable, Johnny is the value STORED in 'd'
d = "johnny"

print(d) #prints the value stored in the variable 'd'
print(d.capitalize())

# Multiple declaration of Variables
person_1, person_2, person_3 = "Daniels", "Isaacs", "Peters"
print(person_2)

spray_1 = spray_2 = spray_3 = "Dancing"
print(spray_3)

# Data Types
# String, Integer, Floats(Decimals), Boolean

n = "Timothy Dalton"
print(n[:4])
print(n[0:-1])
print(n[2:7])
print(n[2:])

# Placeholders
print("%s GuruMentor" % ("Hello"))
print("Hello, My name is %s and I am %d years old" %("Tofree", 30))

# Operators
# +, -, /, *, %

print(3 + 4)
print(5 - 7)
print(5 * 5)
print(8/3)
print(8/3.0)

print(9 % 2)


# List data types
# List, Tuples, Dictionary
shopping_list = ["eggs", "chocolate", "sugar", "milk", "cheeries", "apples"]
print(len(shopping_list)) #length of list

print(shopping_list[3])
shopping_list.append("Chocolate")
print(shopping_list)

print(shopping_list.count('Chocolate'))


# Dictionary

global_map = {}
global_map["myKey"] = "myValue"
global_map["Bob"] = 234
global_map["Kattie"] = 36
global_map["language"] = "Python"
print(global_map)
del global_map["myKey"]
print(global_map)

# Properties of Dictionary
# len, del, shopping_list.keys
for k in global_map.keys():
    print(global_map[k])

print(global_map.values())

#Tuples - Immutable!
daysWeek = ("Monday", "Tuesday","Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print(daysWeek)

# daysWeek.append("MineDay") #Fails as you cannot change Tuples!
daysWeek.count("Monday")
print(daysWeek[:4])

for day in daysWeek:
    print(day)


# Define a function

def doSomethignNice():
    print("I can do something nice")

doSomethignNice()


# A function that takes an argument
def sayMyName(name):
    print(name)


sayMyName("Fisibobo")
sayMyName("")#Empty string  #TODO: Add validation to user input

# TODO: Principles of Solution Design (Algorithm template)
'''
Define the problem in simple terms
Write the logical steps (physical steps) you would take to accomplish the task
Do the least amount of work necessary to accomplish the task - Never complicate solutions
If an activity is repeated more than once, write a function
Do not write what you don't need - e.g. what you think 'might' be useful in the future
Test. Test and again Test every step immediately
Refactor what you've done

Example:  Build a  Room booking platform
Problem:  Map room with time and people with no duplication
Steps:
Get a list of all rooms
Get a time frame for room availability
Get a list of users that can book the room
Receive a booking request [room, time]
Check if room is available - check booking status
Process booking status - return Booked or Available
Confirm room status to the user that made the request

'''
