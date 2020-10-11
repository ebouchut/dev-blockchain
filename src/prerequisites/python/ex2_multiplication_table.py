#!/usr/bin/env python
#
# Use:
# - define and call a function
# - while loop

# Print the `max` first entries of the multiplication table for `n`
#
def table_multiplication(n, max=10):
    print("Table de multiplication de ", n)
    i = 1
    while (i <= max):
        print(i, " * ", n, " = ", i*n)
        i += 1

table_multiplication(5, 20)
table_multiplication(7)