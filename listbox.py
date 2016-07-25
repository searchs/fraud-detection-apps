#!/usr/bin/env python

#Using Python3
from pprint import pprint as pretty_print

from copy import copy, deepcopy

nums = [2,4,3,5,6,8,7,9]
names = ["Carlos", "Liz", "Remy", "Frank", "Claire", "Underwood"]
bloc = [
    [2,4,6,8,10],
    [1,3,5,7,9],
    [1,3,5,7,11,13]
]
names.append("Jack")
print(names)
names = names + ["Santi"]
print(names)
n_index = names.index("Jack")
print(str(n_index))
print(bloc)
pretty_print(bloc)

l = list(range(0,23))
print(l)
pretty_print(l[1:5])
# get every second element
print(l[0:26:2])
# reverses the array
print(l[::-1])

char_count = {'a': 5, 'b':7, 'A': 5, 't':8, 'B': 10}

char_freq = dict();
for key,value in char_count.items():
    if key.lower() in char_freq:
        char_freq[key.lower()] += value
    else:
        char_freq[key.lower()] = value

print(char_freq)

#  List Comprehension 
squared = []

for n in range(11):
    squared.append(n**2)

print(squared)

# Template:
print("Using Comprehension")
sqd = [n**2 for n in range(11)]
print(sqd)

# More computation
sqd_1 = [n**2 for n in range(11) if n % 2 is 0]
print(sqd_1)

# Dictionary Comprehension
# Template
# var_name = {
#     key: value
#     for loop_var in collection
# }

char_freqc =  {
    key.lower(): char_count.get(key.lower(),0) +  char_count.get(key.upper(),0)

for key in char_count.keys()
}

print(char_freqc)

# Maps in Python
# Template

def sq2(r):
    return (r*2)**2

print(list(map(sq2, range(8))))


# Filters in Python

def grabs(e):
    return  (e + abs(e))**3

print(list(map(grabs, range(-5,6))))

def strip_neg(q):
    return q > 0

print("Print filtered list")
print(list(filter(strip_neg, range(-5,6))))

print("Filter with in-built function")
print(list(map(grabs, filter(strip_neg,range(-5,6)))))

