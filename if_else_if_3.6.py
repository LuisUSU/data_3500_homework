# if else
status = "doing great!!!!"
if status == "struggling":
    print("Ask for help, and you will get help!")
else:
    print("Glad you are doing well!")

# if elif else
num_grade = 85
if num_grade >= 90:
    print("You got an A")
elif num_grade >= 80:
    print("You got an B")
elif num_grade >= 70:
    print("You got an C")
elif num_grade >= 60:
    print("You got an D")
else:
    print("You got an F")

#multiple if statements

bozo_bucket = eval(input("What is the highest bucket you got to?"))
if bozo_bucket >= 1:
    print("you win a candy bar")
if bozo_bucket >= 2:
    print("you win a card game")
if bozo_bucket >= 3:
    print("you win a toy doll")
if bozo_bucket >= 4:
    print("you win a kite")
if bozo_bucket >= 5:
    print("you win a bicycle")
if bozo_bucket >= 6:
    print("you win a 50 dollar bill!!!!")
else:
    print("sorry")