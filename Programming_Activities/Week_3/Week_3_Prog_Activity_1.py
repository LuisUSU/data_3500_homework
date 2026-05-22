#week 3 activity 1
user_number = int(input("Enter a 3 digit number: "))
first_number = user_number // 100
second_number = user_number % 10
if first_number == second_number:
    print("Palindrom!!!!")
else:
    print("not palindrom!")

print(user_number)