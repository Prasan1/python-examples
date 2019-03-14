

#!/usr/bin/env python

''' This program find the max and min number in a list'''


lst = [1,3,6,2,9,21,4,11,20,7]

max = lst[0]
min = lst[0]

for x in range(len(lst)):
    if lst[x] < min:
        min = lst[x]
    if lst[x] > max:
        max = lst[x]

print("Min value is %d\n"%min)
print("Max value is: %d\n" %max)
