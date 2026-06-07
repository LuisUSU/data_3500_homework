#Week_4_Activity_5.2

stock_file = open("/workspaces/data_3500_homework/Programming_Activities/Week_4/AAPL.txt")
stock_file_lines = stock_file.readlines()
stock_list = []

for line in stock_file_lines:
    stock_list.append(float(line))

four_day_average = sum(stock_list[-4:]) / 4
print("Four Day Average:  ", four_day_average)

i = 0
buy_buy_buy = 0
total_profit = 0

for price in stock_list:
    if i >=4:
        average = (stock_list[i] + stock_list[i - 1] + stock_list[i - 2] + stock_list[i - 3]) / 4
        if price < average and buy_buy_buy == 0:
            buy_buy_buy = price
            print("Buying at:  ", buy_buy_buy)
        elif price > average and buy_buy_buy != 0:
            trade_profit = price - buy_buy_buy
            print("Selling at:  ", price)
            print("Trade Profit:  ", trade_profit)
            total_profit += trade_profit
            buy_buy_buy = 0
    i+=1

print("Total Profit:  ", total_profit, "  TO THE MOON!!!")