
# 1

range1 = eval(input("Minimum number in range: "))
range2 = eval(input("Max number in range: "))

print("Prime Numbers: ")
for num in range(range1, range2 + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num, end=" ")

#2

num2 = int(input("please give a three digit number: "))
revnum = 0
for i in range(3):
    digit = num2 % 10
    revnum = revnum * 10 + digit
    num2 //= 10
print("Reversed Number: ", revnum)