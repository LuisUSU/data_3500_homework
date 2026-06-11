#Week 5 Activity 6
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
divisor = 0
try:
    divisor = num1/num2
    print(num1, "/", num2, "=", int(divisor))
except:
    print("Cannot divide by zero")