course = 'Python for Beginners'
print(course.upper())
print(course.find('y'))
print(course.replace('for', '4'))

print('Python' in course)
# // Strings //#

# //Arithmetic Operators// #

print(10 // 3)
# interger

print(10 / 3)
# float

print(10 % 3)

print(2 ** 2)
# power

x = 10
x = x + 3
x += 3
x -= 3
# anythigs work here

x = 3 > 2
print(x)

z = 3 != 2
print(z)

y = 3 == 2
print(y)
# comparison operators
# >,>=,<,<=,==,!=

price = 25
print(price > 10 and price < 30)

price = 5
print(price > 10 or price < 30)

price = 5
print(not price > 10)
# invert true to false || false to true

temp = 25

if temp > 30:
    print("It's a hot day for sure")
    print("Drink plenty of water is good for your health")
elif temp > 20:  # (20,30)
    print("It's a nice day isn't it ?")
elif temp > 10:
    print("It's a bit cold today")
else:
    print("It's cold")
print("Done")
# if statement with python

# //Exercise//#
weight = float(input('Weight :'))
unit = input("(K)g or (L)bs: ")
pepe = int

if unit.upper() == "K":
    pepe = weight / 0.45
    print("Weight in Kgs: " + str(pepe))
elif unit == "L" or unit == "l":
    pepe = weight * 0.45
    print("Weight in Lbs: " + str(pepe))

