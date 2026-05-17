#input function, getting input from user
response = input("Please enter your name: ")
print("Hello", response)

#input a string
print(type(response))

#input a number: integer or float
age = input("Enter your age: ")
age = int(age)
print(type(age))

print("In one year you will be", age + 1)

pi = input("Enter pi: ")
pi = float(pi)
print(type(pi))

#eval function
pi2 = input("Enter pi again: ")
pi2 = eval(pi2)
print(type(pi2))