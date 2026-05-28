#Week_2_Activity_2
user_age = input("How old are you? ")
user_age = eval(user_age)
user_pref_age = input("What age would you like to live to? ")
user_pref_age = eval(user_pref_age)
user_age_left = user_pref_age - user_age
print("You have", user_age_left, "years left to live! :)")