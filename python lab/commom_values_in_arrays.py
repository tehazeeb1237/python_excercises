import numpy as np 
list1=[1,4,2,3,5]
tup1=[2,5,4,6,3]
array1=np.array(list1)
sorted_array1=array1.sort()         #[1,2,3,4,5]
array2=np.array(tup1)              
sorted_array2=array2.sort()         #[2,3,4,5,6]
print("The common values are:")
for i in array1:
    for j in array2:
        if i==j:
            print(i,end=" ")


