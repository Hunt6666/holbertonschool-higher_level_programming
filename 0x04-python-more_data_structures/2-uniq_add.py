#!/usr/bin/python3
def uniq_add(my_list=[]):
    ans = 0
    for i in range(0, len(my_list)):
        flag = 0
        for j in range(i, len(my_list)):
            if (my_list[i] == my_list[j]) and (i != j):
                flag = 1
        if flag == 0:
            ans += my_list[i]
    return ans
