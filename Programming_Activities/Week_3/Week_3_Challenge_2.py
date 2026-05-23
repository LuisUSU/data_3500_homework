#Week 3 Challenge 1
print("The password must be at least 8 characters long.")
print("The password must contain at least one uppercase letter.")
print("The password must contain at least one lowercase letter.")
print("The password must contain at least one digit.")
print("The password may contain special characters (e.g., !, @, #, $, etc.), but it is not required.")
new_password = input("Please type your new password:  ")
new_password_length = len(new_password)
new_password_uppercase = any(char.isupper() for char in new_password)
new_password_lowercase = any(char.islower() for char in new_password)
new_password_digit = any(char.isdigit() for char in new_password)
password_length_approved = False
password_check = True

while password_check:
    if new_password_length >= 8:
        password_length_approved = True
        print("Your password is at least 8 characters long")
    else:
        print("Your password is not at least 8 characters long")
    if new_password_uppercase :
        print("Your password contains a Upper Case Letter")
    else:
        print("Your password does not have any Upper Case Letters")
    if new_password_lowercase:
        print("Your password contains a Lower Case Letter")
    else:
        print("Your password does not have any Lower Case Letters")
    if new_password_digit:
        print("Your password contains a number")
    else:
        print("Your password does not contain a Number")
    if password_length_approved and new_password_uppercase and new_password_lowercase and new_password_digit:
        print("Password is strong!")
        password_check = False
        break
    else:
        new_password = input("Password is weak! It does not meet the criteria, please input a new password:  ")
        new_password_length = len(new_password)
        new_password_uppercase = any(char.isupper() for char in new_password)
        new_password_lowercase = any(char.islower() for char in new_password)
        new_password_digit = any(char.isdigit() for char in new_password)
    continue
