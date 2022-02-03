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
    
class Contact: # this is for defining a class that takes on  contacts
    def __init__(self, first_name, last_name, number, email):

      # docstring removed for simplicity

        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = number
        self.email = email
