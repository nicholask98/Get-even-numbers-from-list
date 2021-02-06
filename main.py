import random

# Base Challenge with given list

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

b = [num for num in a if num % 2 == 0]

print(a)
print(b)

# Self-induced dilema: create a random list assigned to 
# a variable and get only the odd numbered list items

list_length = random.randint(5, 20)

c = []

count = 0

while count <= list_length:
    c.append(random.randint(0, 200))
    count += 1

d = [num for num in c if num % 2 == 1]

print(c)
print(d)



