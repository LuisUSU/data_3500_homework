#Homework 5

import json #imports json library 

#storing all the directories for each data set to open in a for loop individually and lists

fileNames = ["/workspaces/data_3500_homework/hw5/AAPL.txt","/workspaces/data_3500_homework/hw5/ADBE.txt","/workspaces/data_3500_homework/hw5/AMD.txt","/workspaces/data_3500_homework/hw5/AMZN.txt","/workspaces/data_3500_homework/hw5/ETSY.txt","/workspaces/data_3500_homework/hw5/GOOG.txt","/workspaces/data_3500_homework/hw5/META.txt","/workspaces/data_3500_homework/hw5/MSFT.txt","/workspaces/data_3500_homework/hw5/MU.txt","/workspaces/data_3500_homework/hw5/NVDA.txt",]
stockName = ["AAPL","ADBE","AMD","AMZN","ETSY","GOOG","META","MSFT","MU","NVDA"]
currentStockName = ""
openFiles = []
stockNums = []
stockLines = []

#variables for organizing and adding stock prices to dictionaries and lists
stockIndexes = -1
mrStockReturn = 0
mrStockProfit = 0
smaStockReturn = 0
smaStockProfit = 0

#arithmetic variables and lists
stockPrices = []
stockPriceLst = []
stockPrice = 0
stockAve = 0
stockFiveDayAve = 0
calFiveDayAve = 0
stockFiveDayAveLst = []
currentPrice = 0
buyNowFirstPrice = 0
sellNowTotal = 0
buyNowTotal = 0
lastBought = 0
buyNowFirstPrice = True
stockTotalAverage = 0
#old variables
buyNowPrice = 0
profit = 0
totalProfit = 0
totalProfitPer = 0
currentPrice = 0

#simple moving average strategy function

def simpleMovingAverageStrategy(stockPrice,stockAve):
    if stockPrice > stockAve:
        print("buy at: ", stockPrice)
        smaStockProfit = stockAve
    elif stockPrice < stockAve:
        print("sell at: ", stockPrice)
        smaStockReturn = smaStockPrices
    else:
        pass

    smaStockProfit = 0
    smaStockReturn = 0

    return smaStockProfit,smaStockReturn

#mean reversion strategy function

def meanReversionStrategy(stockPrice):
    stockAve
    for m in stockPrice:
        if m < stockAve * .98:
            print("buy at: ", stockPrice)
            buyNowTotal += buyNowPrice
            buyNowTotal = round(buyNowTotal, 2)
            lastBought = buyNowPrice
            if buyingFirstTime == True:
                buyNowFirstPrice = currentPrice
                buyingFirstTime = False
        elif stockPrice > stockAve * 1.02:
            print("sell at: ", stockPrice)
            mrStockProfit = sellNowPrice - lastBought
            sellNowTotal 
        else:
            pass

    mrStockProfit = 0
    mrStockReturn = 0

    return mrStockProfit, mrStockReturn

#save results function
def saveResults(stockIndex,stockPrices,smaStockProfits,smaStockReturns,mrStockProfits,mrStockReturns):
    results = {}
    newResults = {}
    currentStockName = str(f"{stockName[stockIndex]}") #sets name to the name in the list based on number of loops ran
    #adds new keys with the name of the stock the type of data and the data afterwards
    newResults.update(dict.fromkeys([str(f"{currentStockName}_prices")], stockPrices))
    newResults.update(dict.fromkeys([str(f"{currentStockName}_sma_profits")], smaStockProfits))
    newResults.update(dict.fromkeys([str(f"{currentStockName}_sma_returns")], smaStockReturns))
    newResults.update(dict.fromkeys([str(f"{currentStockName}_mr_profits")], mrStockProfits))
    newResults.update(dict.fromkeys([str(f"{currentStockName}_mr_returns")], mrStockReturns))

    results.update(newResults)
    newResults.clear()
    print(results, end="\n")
    return results
#adding data from .txt files into result ticker dictionary

for fileName in fileNames:
    #these lines add the stock name to the dictionary key
    stockIndexes +=1
    #these lines open the file, float the string, and round the data
    openFiles = open(fileName, "r") #opens an individual file each cycle
    stockPrices += [openFiles.readlines()] #reads through each file
    stockPrices = [[round(float(item),2) for item in stockLst] for stockLst in stockPrices] #changes data from a string to a float and rounds it

    stockPricesLst.append(stockPrices)
    stockFiveDayAveLst.append(stockPrices)
    currentPrice = stockPriceLst[-1]
    stockPrice = currentPrice
    buyNowPrice = currentPrice
    sellNowPrice = currentPrice

    if len(stockFiveDayAveLst) > 5:
        calFiveDayAve = (stockFiveDayAveLst[0]+stockFiveDayAveLst[1]+stockFiveDayAveLst[2]+stockFiveDayAveLst[3]+stockFiveDayAveLst[4]+stockFiveDayAveLst[5]) / 5
        stockFiveDayAve = calFiveDayAve
        meanReversionStrategy(stockPrices,stockFiveDayAve)
        simpleMovingAverageStrategy(stockPrices,stockFiveDayAve)
        stockFiveDayAveLst.clear()
    elif len(fiveDayAveLst) < 5:#if the average has less than 5 items then continue running loop until it reaches 5 items
        continue

    #save results into a new dictionary entry containing these 5 variables
    saveResults(stockIndexes,stockPrices,mrStockProfit,mrStockReturn,smaStockProfit,smaStockReturn)

with open("results.json", "w") as file:
    json.dump(results, file)

#print(results)