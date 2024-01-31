# This program uses if/else statement in python
# The program ask for user input and checks if the
# the input number is within 1 to 10 inclusive.


# Ask for user input

num = input("Please enter a number between 1 and 10 (inclusive): \n")

#checks if the number is within the range 1 to 10
if num > 0 and num<=10:
	print("Your entered %s\n" %num)
else:
        print("Your number is out of range")

