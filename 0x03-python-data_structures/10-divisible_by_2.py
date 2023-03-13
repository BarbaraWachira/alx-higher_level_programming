#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new = []
    k = 0
    for i in my_list:
        if i % 2 == 0:
            new.append(True)
        else:
            new.append(False)
        k += 0
    return (new)
