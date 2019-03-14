
#!/usr/bin/env python

'''This program simulates a car engine.
   This is a part of work assignment in Mosh python tutorial.
   You can visit his website below: 
   https://codewithmosh.com/p/python-programming-course-beginners/?product_id=866084&coupon_code=YOUTUBE&preview=logged_out
   To watch his youtube video please follow the following link:
   https://www.youtube.com/watch?v=_uQrJ0TkZlc
'''

# user input

command =""
startCond = False
while command !="quit":
    command = input("> ").lower().strip()
    if command =="help":
        print('''
        start- to start the car
        stop- to stop the car
        quit- to exit.''')
    elif command == "start":
        if startCond is True:
            print("Human error. The car has already started\n")
        else:
            startCond = True
            print("Starting the car...\n")
    elif command == "stop":
        if startCond is False:
            print("Oh o! The car has stopped already!\n")
        else:
            startCond = False
            print("stopping the car<<\n")
    elif command =="quit":
        break
    else:
        print("Sorry I didn't understand %s command\n"%command)
