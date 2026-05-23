#3.4 @ loop

for i in range(2):
    for i in range(7):
        print("@", end="")
    print()

#3.9 Separating the digits an Integer

number = int(input("Enter a number that is 7 to 10 digits:  "))
number_list = []

while number > 0:
    number_list.append(number % 10)
    number = number // 10
number_list.reverse()
for i in number_list:
    print(i)

#3.11:

total_miles_per_gallon = 0
additional_miles_per_gallon = 0
mileage_check = True

while mileage_check:
    gallons_used = float(input("Gallons Used:  "))
    miles_driven = float(input("Miles Driven:  "))
    if gallons_used == 0 and miles_driven == 0:
        break
    miles_per_gallon = miles_driven / gallons_used
    print("The miles per gallon for this tank was: Type 0,0 to quit ", miles_per_gallon)

#3.12 Palindromes

user_number = int(input("Enter a 5 digit number: "))
first_number = user_number // 10000
second_number = user_number // 1000 % 10
third_number = user_number // 100 % 10
fourth_number = user_number // 10 % 10
fifth_number = user_number % 10

#debugging
#print(user_number)
#print(first_number)
#print(second_number)
#print(third_number)
#print(fourth_number)
#print(fifth_number)
if first_number == second_number == third_number == fourth_number == fifth_number:
    print("Palindrom!!!!")
else:
    print("not palindrom!")

#3.14 Approximating Pi

pi = 0
n = 4
d = 1
iteration = 0

for i in range(10000):
    d += 2
    x = i % 2
    pn = 2 * x - 1
    pi += pn * n / d
    iteration += 1
    print("Pi:  ", pi)
    print("Iteration:  ", iteration)
