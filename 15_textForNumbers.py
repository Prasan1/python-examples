
#!/usr/bin/env python

'''This is another assignment from Mosh's tutorial
   of python. This program writes a textual representation
   of numeric value.'''

number = int(input("Enter a number:\n"))
num_mapping = {1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",0:"zero"}

print(num_mapping.get(number))

