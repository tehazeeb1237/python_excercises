def has_duplicates(lst):
    unique_elements=set(lst)
    if len(lst)>len(unique_elements):
        return True
    else:
        return False
    
print(has_duplicates([1,2,3,2,4,3]))