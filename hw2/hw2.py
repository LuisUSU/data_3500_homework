#2.3 Fill in the missing code

grade = 91
if grade >= 90:
    print("\nCongratulations! Your grade of", grade, "earns you an A in this course")

#2.4 Arithmetic

#addition
print("\nAddition: 27.4 + 2 =", 27.5 + 2)
#subtraction
print("\nSubtraction: 27.5 - 2 =", 27.5 - 2)
#multiplication
print("\nMultiplication: 27.5 * 2 =", 27.5 * 2)
#division
print("\nDivision: 27.5 / 2 =", 27.5 / 2)
#floor
print("\nFloor: 27.5 // 2 =", 27.5 // 2)
#power
print("\nExponent: 27.5 ** 2 =", 27.5 ** 2)

#2.5 Circle Area, Diameter, and Circumference

pi = 3.14159
r = 2
diameter = 2 * r
circumference = 2 * pi * r
area = pi * r ** 2

print("\nRadius = 2")
print("\nPi = 3.14159")
print("\nDiameter = ", diameter)
print("\nCircumference = ", circumference)
print("\nArea = ", area)

#2.6 Odd or Even

integer = input("\n\nInput an number: ")
integer = eval(integer)
if integer % 2 == 0:
    print("\nThe Number",integer,"is Even")
else:
    print("\nThe Number", integer,"is Odd")

#2.7 Multiples

if 1024 % 4 == 0:
    print("\n\nThe Number 1024 is a multiple of 4")
else:
    print("\nThe Number 1024 is NOT a multiple of 4")

if 2 % 10 == 0:
    print("\nThe number 2 is a multiple of 10")
else:
    print("\nThe Number 2 is NOT a multiple of 10")

#2.8 Table of Squares and Cubes

number = (0,1,2,3,4,5)
square = (0,1,4,9,16,25)
cube = (0,1,8,27,64,125)



