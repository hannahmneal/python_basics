# Importing the module "sys" is how we can stop our program from running (after 3 attempts)
import sys

# While loops ("while this is true, continue to iterate")

# using all-caps is a naming convention for constants:
MASTER_PASSWORD = 'pass'

password = input("Please enter password: ")
attempt_count = 1
while password != MASTER_PASSWORD:
    if attempt_count > 3:
        # Any value passed to sys.exit will be considered an error
        sys.exit("Too many attempts")
    # As long as the condition above is met (i.e., the user does not enter 'pass' as their input, the code below will run)
    password = input("Invalid password, try again: ")
    attempt_count += 1
print("Welcome to the website!")


# For loops

message = "Your Father Smelled of Elderberries"
for letter in message: # The only requirement for the right side of an "in" statement is that the right side be 'iterable'.
    print(letter.upper())
    #This will print:
    #Y
    #O
    #U
    #R
    # etc.
    # Each time through the loop, the letter variable is set. For each letter in the "message" side of the "in", a new variable is created on the "letter" side of the "in".
