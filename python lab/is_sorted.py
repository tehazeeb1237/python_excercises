def is_sorted(list_1):
    sorted_list=sorted(list_1)
    if list_1==sorted_list:
        return True
    else:
        return False
    
result1=is_sorted([1,2,3,4,5])

print("result1 is",result1)
