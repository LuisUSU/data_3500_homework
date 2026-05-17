#grades

grades = [50.0, 45.0, 48.0, 49.0]

#adding grades

total = 0.0
num_grades = 0

for grad in grades:
    total += grad
    num_grades += 1

#finding average

ave = total/num_grades
print("Average grade is: ", ave)