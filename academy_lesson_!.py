#!/usr/bin/env python

# author Ola Ajibode

# Installing Python on Windows and Mac OSX/Linux
print("Hello World")

# Variable:  A variable holds a space in memory and can hold a value
# d is the name of the variable, Johnny is the value STORED in 'd'
d = "Johnny"

print(d) #prints the value stored in the variable 'd'

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
