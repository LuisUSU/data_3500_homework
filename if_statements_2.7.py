#if stmt
if 5 > 10: #false
    print("5 is greater")
if 10 > 5: #true
    print("10 is greater")
    # if statement line of code
    # if statement line of code
#this line is outside of my if statement and will execute
#regardless of it

print(10 < 5)
print(10 > 5)
print(10 <= 5)
print(10 >= 5)
print(10 == 5)
print(10 != 5)

age = 25

your_age = input("Enter your age: ")
print(type(your_age))
your_age = eval(your_age)
if your_age < age:
    print("Your are younger than Chelsea")

if your_age > age:
    print("Your age is older than Chelsea")