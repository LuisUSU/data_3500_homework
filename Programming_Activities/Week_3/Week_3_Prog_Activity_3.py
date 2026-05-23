#Week 3 Activity 3
can_ride_in_front = False
check_age_and_weight = True
child_age = int(input("What is the childs age?  "))
child_weight = int(input("What is the childs weight?  "))
if child_age >= 12:
    can_ride_in_front = True
elif child_age == 11 and child_weight >= 90:
    can_ride_in_front = True
elif child_age < 11 and child_weight >= 100:
    can_ride_in_front = True
else:
    can_ride_in_front = False
while check_age_and_weight:
    if can_ride_in_front:
        print("Can ride in front passenger seat")
        break
    else:
        print("Can not ride in front passenger seat")
        break