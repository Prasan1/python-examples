#!/usr/bin/env

'''This program converts entered weight 
   to pound or kilogram unit'''

# Take an user input and store it as weight
weight = float(input("Please enter your weight: \n"))

# Take unit either K or L for conversion. This will be our check point
# for the logic
unit =input("K(ilo) or L(bs)? please enter the first letter only \n")

if unit.upper() =="L":
    converted_weight = weight *0.45
    print(f"Your weight is {converted_weight} kilos. Thank you.\n")
else:
    converted_weight = weight/0.45
    print(f"Your weight is {converted_weight} lbs. Thank you.\n")
