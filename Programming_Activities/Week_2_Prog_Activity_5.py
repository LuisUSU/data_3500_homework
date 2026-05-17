user_age = eval(input("How old are you?"))
cur_year = 2026

while user_age >0:
    print("You where alive in year: ", cur_year)
    cur_year -= 1
    user_age -= 1
else:
    print("Your Birth Year is", cur_year)

