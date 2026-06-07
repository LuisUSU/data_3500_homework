#Week 5 Programming Activity 1

name=input("What is your name?   ") + "\n"
color=input("What is your favorite color?   ") + "\n"

with open("favcolor.txt","w") as favcolorfile:
    favcolorfile.write(name)
    favcolorfile.write(color)

favcolorfile_open = open("favcolor.txt", "r")
print(favcolorfile_open.readlines())