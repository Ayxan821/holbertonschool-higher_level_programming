#!/usr/bin/python3

def max_integer(my_list=[]):
    if not my_list:  # siyahı boşdursa
        return None

    max_val = my_list[0]  # ilk elementi ən böyük kimi qəbul et
    for num in my_list:
        if num > max_val:
            max_val = num

    return max_val
