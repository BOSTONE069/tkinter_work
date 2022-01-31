import random

random_number = random.randint(0,1000) #This is to generate random numbers within the program between 0 to 100

pie = (2 * 3.14)

C = (pie * random_number)

print(C)

greeting = "Hello"
school = "Moringa"

print(greeting + ", " + school + "!")

print('Enter the integer value for the calculation of the area')
radius = int(input())

area = (pie * radius)

print(area)

height = 40  # inches
if height > 70:
    print("You are really tall")
elif height > 60:
    print("You are of average height")

else:
    print("You are really short")


numbers = [1, 2, 3, 4, 5]

for number in numbers:
    print(number)
    
for i in range(0, 7):
    print("I would love " + str(i) + " cookies")
