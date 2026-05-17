num1 = input("Input 1st Number: ")
num1 = int(float(num1))
num2 = input("Input 2nd Number: ")
num2 = int(float(num2))
num3 = input("Input 3rd Number: ")
num3 = int(float(num3))
minnum = min(num1,num2,num3)
maxnum = max(num1,num2,num3)

print("\nThe smallest number is: ", minnum,"\nThe Largest Number is: ", maxnum)

if maxnum % 2 == 0:
    print("The Range is: ")
    for i in range(maxnum):
        print(i, end=",")
else:
    if minnum < 11:
        if minnum > -1:
            print("\n", minnum,"is Within the range of 0 to 10")
    if minnum > 10:
            print("\n", minnum,"is not between the range of 0 and 10")
    if minnum < 0:
            print("\n", minnum,"is not between the range of 0 and 10")



    


