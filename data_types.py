# Data Types in Python

## Strings

# Place this in the console to see what happens:
subject_template = "Thanks for playing {} with me {}!"
subject_template.format("Muse", "Brenda")
subject_template.format("Ticket to Ride", "Brian")

# Raising Exceptions:

def myTotal(odd_num, even_num):
    if (odd_num % 2 == 0) or (even_num % 2 > 0):
        raise ValueError("The first number must be odd and the second must be even.")
        # As soon as the "raise" line runs (or, is triggered), the function exits and the exception is "bubbled up" to the caller. It the exception is handled at the caller, the exception code will run, otherwise, the program ends and you will see the traceback.
    return(odd_num + even_num)

try:
    user_odd_num = int(input("What's the first number?"))
    # If this number is 8, meaning, it does not meet the requirement of an odd number, the Traceback and ValueError ("One of your inputs does not meet requirements") is bubbled up.
    user_even_num = int(input("What's the second number?"))
    total_number = myTotal(user_odd_num, user_even_num)
except ValueError as err:
    # err is a new variable that is created and assigned the exception that was thrown.
    print("Whoops! One of your numbers does not meet the requirements")
    # By assigning ValueError to "err", we can achieve both messages, the one directly after the "if" statement and the one here when the exception is thrown.
    print("({})".format(err))
else:
    print("The sum of your entries is {}".format(total_number))
