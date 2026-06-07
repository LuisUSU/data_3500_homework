#Week_4_Activity_5

stock_file = open("/workspaces/data_3500_homework/Programming_Activities/Week_4/AAPL.txt")
stock_file_lines = stock_file.readlines()
stock_list = []

for line in stock_file_lines:
    stock_list.append(float(line))
total_average = sum(stock_list) / len(stock_list)
print("Total Average:  ", total_average)

five_day_average = (stock_list[0]+stock_list[1]+stock_list[2]+stock_list[3]+stock_list[4]+stock_list[5]) / 5
print("Five Day Average:  ", five_day_average)