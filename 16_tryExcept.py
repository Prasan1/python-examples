
#!/usr/bin/env python


''' This code handles the error 
    thrown due to the division
    by zero'''


try:
    divident = int(input("Enter a divident:\n"))
    divisor = int(input("Enter a divident:\n"))
    result = divident/divisor
    print("The result is:%d\n"%result)
except ZeroDivisionError:
    print("The divisor can not be zero\n")
    
