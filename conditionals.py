# author Ola Ajibode

# Making Decisions: Conditionals

if 4 < 6:
    print "My name is Jack!"


if 5 < 3:
    print "How can that be?"

else:
    print "We already know that"

# Logical Operators, Relationals Operators

# Relational Operators: Helps to compare ro contrast values.  Always results in TRUE of FALSE
# Operator Catalogue: >, <, >=, <=, ==, !=

# Mention ERRORS: e.g. Syntax error - if 5 = 5: will generate this sort of error

# Nested Ifs:  Decisions in Decisions

age = 12
name = "James"
if age < 12:
    if name == 'James':
        print "You are almost a teenager"
    else:
        print "We only accept James as Chief Coder"
elif age == 13:
    print "You are just a year older than our Chief Coder"
else:
    print "You are now officially invited tot he next level"


# Logical Operators: AND OR
print "Logical Operators list"
if age > 13 and name != "James":
    print "You are a new brand of species!"

if age > 13 or name == "Lynda":
    print "We will support you"


# LOOPS - Runs the code until a condition is FALSE
# Loop Types: For and While
ls = ["London","Paris","Budapest","Geneva","Berlin"]
for i in ls:
    print i

length_of_list = len(ls)

for r in range(200,0,-10):
	print r

# while Loop:  Keeps checking for a condition until that condition becomes FALSE

counter = 0
while counter < 8:
    print "I'm Alive!"
    counter = counter + 1
    if counter == 8:
        print "Ready to kill process!"


# Prime Number Generator
for n in range(2,37):
    s = 2
    counter = 0
    while s < n:
        if n % s == 0:
            counter = 1
            s = s + 1
        else:
            s = s + 1
    if counter == 0:
        print str(n) + " is a prime number"
    else:
        counter = 0

# Loop Control Statements
# Break, Continue, Pass
counter = 0
while counter < 100:
    if counter == 4:
        break
    else:
        pass
    print str(counter)
    counter += 1


for a in "Program":
    if a == "o":
        continue
    print a.upper()


# TRY and ACCEPT
