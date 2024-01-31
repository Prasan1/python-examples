

#!/usr/bin/env python
import random;

'''This program simulates the number guessing game'''

# Generate a random number between 1 and 20

machine_number = random.randrange(1,21)

# Ask user to enter a number between 1 and 20

print("---------------------------------------------------------------------\n")
print("I am thinking of a number between 1 and 20. Can you guess what it is?\n")
print("----------------------------------------------------------------------\n")

guess = int(input("Enter a number \n"))

# limit the number of times the user makes guesses

number_of_guesses =1 



while guess != machine_number and number_of_guesses < 3:
    if guess > machine_number:
        print("Your guess is high. Take a guess again.\n")
    if guess < machine_number:
        print("Your guess is low. Guess again.\n") 
    guess = int(input("\n"))     
    number_of_guesses = number_of_guesses+1;  

if guess == machine_number:
    print("congratulation! you won.\n")

if guess != machine_number:
    print("The number was %d. Try next time\n"%machine_number)
