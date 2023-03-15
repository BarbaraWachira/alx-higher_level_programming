#!/usr/bin/python3
def uniq_add(my_list=[]):
    _sum = 0
    my_list = sorted(my_list)
    for i in range(len(my_list)):
        if i == 0:
            _sum += my_list[i]
            continue
        if not my_list[i] <= my_list[i - 1]:
            _sum += my_list[i]
    return _sum
