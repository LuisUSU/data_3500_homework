#Week 5 Activity 3 & 4
num1 = input("Please input first number:  ")
num2 = input("Please input second number:  ")
num1 = int(num1)#changes number to integer so that the arithmetic may occur
num2 = int(num2)
twoDimList = []

for num in range(num1):
    twoDimList.append([])#adds lists to list

for num in range(1, num1+1):
    for nums in range(1, num2+1):
        twoDimList[num-1].append(num * nums)#populates list with the multiplied inputed numbers

for num in range(num1):
    for nums in range(num2):
        print(twoDimList[num][nums], end="  ")#prints the multiplication tables
    print()

dictionary = {}
dictionary["Favorite Color"] = input("What is your favorite color?")
dictionary["age"] = input("How old are you?")
dictionary["Multiplication Table"] = twoDimList

for key in dictionary.keys():
    print(key, ":", dictionary[key])