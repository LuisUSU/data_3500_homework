#Week 5 Programming Activity 4

stringList = ["  I     ", "   Enjoy             ", "               Programming", "   in   ", "Python              "]

stringListNew = [str.strip() for str in stringList]
print("New String List with No Spaces:   ", stringListNew)