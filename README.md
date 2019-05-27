# python_basics

Never stop learning.

## Notes

### Basic Intro and Variables

Snake case uses underscores where spaces should be.

To declare a variable in Python, simply type the name of the variable, supply an equals sign and the value of the variable:

`my_cat = "Clove"`


To collect user input, type `input()` in the terminal. Here's an example of how you might use it:

`current_binge = input("What are you streaming today?")`

You may also choose to supply a `print()` function after the user's input.


### Numeric/Data Types

Floats (floating point integers) are decimals and used for greater precision: `4.1`.

We can also round numbers: `round(_)` will round `4.1` to `4`. The underscore is a shortcut to supply the last answer as the starting item in the terminal (like pressing the up arrow in the terminal).

The order of operations matters in the same way as in javascript.

### Strings

Strings are immutable (unchangeable). That is, a string assigned to a variable always belongs in that variable. Here's an example:

`my_spell = "Accio"`

If we want to create a new string and concatenate more onto `my_spell`, we could use

`my_spell = my_spell + "Wand!"`

Since strings are immutable, the variable `my_spell` didn't change (its value is still "Accio") but more was appended to it and stored in a brand new variable of the same name. Now, the value of the new `my_spell` is "Accio Wand!". The shorthand version for concatenating strings in this way is by using `+=` . To use the same example, instead of typing `my_spell = my_spell + "Wand!"`, type `my_spell += "Wand!"`.

You can also multiply a string a number of times like this:

`"!" * 20`

It will print out twenty exclamation points.

To use a special character, use an escape sequence: backslash `\` . For instance: "can\'t" will print "can't".

To find out how many characters are in a string, use `len()`:

```
len("Accio")
>>>  5
```

#### String methods

To view a list of string methods, you can type `help(str)` in your terminal. (Magic methods are the ones that begin with two underscores.)

You can change the case of a string to upper or lower using `upper()` or `lower()` on a string. Similarly, to change the first letter of every word from lower to uppercase, use `title()`.

To turn an object into its string form, you can use `str()`.

String formatting creates a template that can be populated with data.

To see if one string is inside another, use `in`: `"stream" in "streaming"` will return True.


### Booleans

"It's all ones and zeroes."

A double-equals is used for comparing two things in the same was as in javascript.

To create an if statement in python,

```
my_cat = input("What is this cat's name?")
if my_cat == "Clove":
    print(my_cat, "is pwecious.")
elif my_cat == "Sage":
    print("This is my husband's cat.")
else:
    print("This is someone else's cat.")
```
The `elif` operator supplies another exact condition be met and offers the opportunity to provide a specific condition for that other instance.




## References
[Teamtreehouse](https://teamtreehouse.com)