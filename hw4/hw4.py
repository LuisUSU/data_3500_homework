#Homework 4 - Stock Market
stockNums = open("/workspaces/data_3500_homework/hw4/TSLA.txt")
lines = stockNums.readlines()
stockPrice = []
fiveDayAve = []

for line in lines:
    stockPrice = [float(line) for line in lines]
    fiveDayAve = [float(line) for line in lines[5]]
print(fiveDayAve)