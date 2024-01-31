

#!/usr/bin/env python

''' This program creates an F pattern 
    on the console using nested for loop. 
    
    XXXXX
    XX
    XXXXX
    XX
    XX


'''


for n in range(3):
    if n !=2:
        print("XXXXX")
    for m in range(1):
        print("XX")
