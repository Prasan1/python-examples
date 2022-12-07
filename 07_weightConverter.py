#!/usr/bin/env

'''This program converts the weight 
   from pound to kilogram unit and 
   vice varsa'''


weight = int(input("Please enter your weight: \n"))
unit =input("K(ilo) or L(bs)? please enter the first letter only \n")
if unit.upper() =="L":
    converted_weight = weight *0.45
    print("Your weight is %d kilos. Thank you.\n" %converted_weight)
else:
    converted_weight = weight/0.45
    print("Your weight is %d lbs. Thank you.\n" %converted_weight)
