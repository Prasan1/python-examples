
#!/usr/bin/env python

''' This method demonstrates a simple class 
    in python '''


class Person():
    def __init__(self,name):
        self.name = name

    def talk(self):
        print("The %s is talking.\n"%self.name)



#create an object

person = Person("Tom")

#call the method talk()

person.talk()
