#Week_4_Activity_4
import random

random_num_list = []

for i in range(10):
    random_num_list.append(random.randint(1,1000))
    print(random_num_list)
    
i=0

for num in random_num_list:
    if i >= 0:
        print(random_num_list[i])
        print(random_num_list[i-1])
        if random_num_list[i] % 2 == 0 and random_num_list[i-1] % 2 == 0:
            print("Both ", random_num_list[i], " and ", random_num_list[i-1]," are even")
    i += 1
       
    
    