'''This program creates a function and calls that function
to display the result. This program is the exact replication 
of the program that we saw in 02_square.py. Here we have put
all the logic inside a function'''


def square():
    # Take input from user
    num = input("Enter a num: \n")

    # declare variable ans and give it a value 0
    ans = 0

    # User input returns a str so do not 
    # forget to cast it to int type
    itr_left = int(num)


    while(itr_left !=0):
        ans = ans + int(num)
        itr_left = itr_left-1
    print(f"The square of {num} is: {ans}")


if __name__=='__main__':
    square()