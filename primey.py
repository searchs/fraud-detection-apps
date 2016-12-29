def is_prime(x):
    if x < 0 or x < 2:
        return False
    elif x == 2:
        return True
    elif x > 2:
        status_true = 0
        status_false = 0
        for n in range(2,x):
            if(x % n == 0):
                status_false += 1
            else:
                status_true += 1

        if status_false == 0:
            return True
        else:
            return False



# Testing
falsy = []
truthy = []

for p in range(0,100001):
    if is_prime(p):
        print(p)
        truthy.append(p)
    else:
        falsy.append(p)


print("Count of Prime Numbers:", len(truthy))
print("Count of Non-Prime Numbers:", len(falsy))
print(truthy)
