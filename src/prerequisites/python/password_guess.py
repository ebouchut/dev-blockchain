#!/usr/bin/env python
#
# Use while loop and break keyword

# Regular while Loop
correct_password = "123"
found = False

print( "Guess what is the first password")
while not found:
    password = input("Password? ")
    found =  password == correct_password
    if found:
        print("You found it!")
    else: 
        print("This is not the password, try again...")

# This time use an infinite loop 
#   and use the break keyword to get out the loop.
print( "Guess what is the second password")
correct_password = "456"

while 1:  # inifinite loop
    password = input("Password? ")
    
    if password == correct_password:
        print("You found it!")
        break  # Get out of the loop
    else: 
        print("This is not the password, try again...")
