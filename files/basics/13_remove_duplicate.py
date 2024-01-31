
#!/usr/bin/env python

''' This program removes duplicate items from a list.
    Here lst1 has duplicate items. So we create another
    list called lst2 which will not contain duplicate
    items.'''


lst1 = [1,3,1,5,6,9,5,10,20,3,33,10]
lst2 = []

for x in lst1:
    if x not in lst2:
        lst2.append(x)

for i in lst2:
    print(i)
