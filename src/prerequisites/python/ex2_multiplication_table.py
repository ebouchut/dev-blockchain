#!/usr/bin/env python
# -*-coding:utf-8 -*
#
# Use:
# - define and call a function
# - while loop

def multiplication_table(n, max=10):
	  # DocString for this function.
	  # This is a string aimed to describe what this function does and how to call it.
	  # It is surrounded with 3 double quotes (`"""`).
	  #
	  # Use `help(multiplication_table)` to display this help
	  #
    """Print the `max` first entries 
    of the multiplication table for `n`
    """
    print("Multiplication table for ", n)
    i = 1
    while (i <= max):
        print(i, " * ", n, " = ", i*n)
        i += 1

# Display the first 10 entries (default max value) for the 7 multiplication table
multiplication_table(7)

# Display the first 20 entries for the 7 multiplication table
multiplication_table(5, 20)

# Dislay the docString for the `multiplication_table` function 
# help(multiplication_table)