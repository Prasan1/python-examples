
#!/usr/bin/env python

'''This program simulates a car engine.
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
