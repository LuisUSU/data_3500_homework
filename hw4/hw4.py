#Homework 4 - Stock Market
stockNums = open("/workspaces/data_3500_homework/hw4/TSLA.txt")
lines = stockNums.readlines()
stockPrice = []
for line in lines:
    stockPrice.append(float(line))