num = 2
how_many_loops = 0
for sum in range(1, 1001):
    sum += 1/num
    num *=2
    how_many_loops += 1
print("Sum: ", sum)
print("Loops: ", how_many_loops)
