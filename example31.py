# WAP find sum and avg of 10 , 3-digit random numbers

import random

def get_3digit_rand_nums(size):
    rand_nums = []
    #for i in range(size):
    i = 0
    while i<size:
        num = random.randrange(100, 999)
        rand_nums.append(num)
        i = i+1 # i+=1 # No operators -->++ --
    return rand_nums

def get_sum_avg(list_seq):
    s = 0
    for e in list_seq:
        s = s+e
    return s, s/len(list_seq)

r_nums = get_3digit_rand_nums(10)
total, avg = get_sum_avg(r_nums)  
print("Total : {} and Avg: {}".format(total, avg))



output = get_sum_avg(r_nums)
print(output, type(output))
print("Total : {} and Avg: {}".format(output[0], output[1]))



