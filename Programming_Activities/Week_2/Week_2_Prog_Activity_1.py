apple_price = input("Enter the price of an apple: ")
apple_price = eval(apple_price)
number_purchased = input("Enter how many apples you purchased: ")
number_purchased = eval(number_purchased)
tax = 1.07
total_bill = apple_price * number_purchased * tax
format_total_bill = f"{total_bill:.2f}"
if total_bill == 0:
    print("Check your inputs")
print("You Purchased",number_purchased, "apples.\nThe price of the total bill is: $", format_total_bill)
