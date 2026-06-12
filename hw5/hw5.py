#Homework 4 - Stock Market
#opens stock number document
stockNums = open("/workspaces/data_3500_homework/hw4/TSLA.txt")
lines = stockNums.readlines()

#my variables
buyingFirstTime = [True,True,True,True,True,True,True,True,True,True] #checks to see if it's the first time buying, the first time it goes through the loop I set it to false to keep first number
stockPrices = []
buyNowPrice = 0
profit = 0
totalProfit = 0
totalProfitPer = 0
currentPrice = 0
CalFiveDayAve = 0
fiveDayAve = 0
buyNowFirstPrice = 0
buyNowTotal = 0
sellNowTotal = 0
totalShares = 0
lastBought = 0

fiveDayAveLst = []
stockPriceLst = []
def meanReversionStrategy(prices[]):
for i in lines(10):#Create a list for all 10 stocks
    for j in lines(10):#Create a list within the 10 lists, and append all the prices into it
        stockPrice = float(i)
        stock

for line in lines: #adds numbers into a list and rounds them, as well as sets the current price to the last in the list for calculations
    stockPrice = float(line)
    stockPrice = round(stockPrice, 2)
    stockPriceLst.append(stockPrice)
    fiveDayAveLst.append(stockPrice)
    currentPrice = stockPriceLst[-1]
    buyNowPrice = currentPrice
    sellNowPrice = currentPrice
    #check five day averages, saves buy it now price and sell now prices calculates the profit and saves it to a variable
    if len(fiveDayAveLst) > 5:
        CalFiveDayAve = (fiveDayAveLst[0]+fiveDayAveLst[1]+fiveDayAveLst[2]+fiveDayAveLst[3]+fiveDayAveLst[4]+fiveDayAveLst[5]) / 5
        fiveDayAve = CalFiveDayAve
        fiveDayAveLst.clear()
    elif len(fiveDayAveLst) < 5:#if the average has less than 5 items then continue running loop until it reaches 5 items
        continue
    if currentPrice < fiveDayAve * .98:
        buyNowTotal += buyNowPrice
        buyNowTotal = round(buyNowTotal, 2)
        lastBought = buyNowPrice
        totalShares += 1
        print("Buying at:  ", buyNowPrice)
        if buyingFirstTime == True:
            buyNowFirstPrice = currentPrice
            buyingFirstTime = False
    elif currentPrice > fiveDayAve * 1.02:
        sellNowTotal += sellNowPrice
        print("Selling at:  ", sellNowPrice)
        profit = sellNowPrice - lastBought
        totalProfit += profit
        totalProfit = round(totalProfit, 2)
        print("Profit:  ", profit)

totalProfitPer = (totalProfit / buyNowFirstPrice) * 100
print("First Buy Price:  ", buyNowFirstPrice)
print("Total Profit:  ", totalProfit)
print("Total Profit Percentage:  ", float(round(totalProfitPer,2)),"%")

print(-13 // 4)
numbers = [2, 3, 5, 7, 11, 13, 17, 19]
numbers2 = numbers[2:6]
print(numbers2)