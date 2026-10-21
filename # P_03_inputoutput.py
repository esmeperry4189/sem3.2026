# P_03_inputoutput.py
# 21/20/2026 octo
# art_wizard

# ask user for their name

"""name = input("What is your name? ")
print (f"Hello {name}!")


# ask the user for their fav number
# double, halve, and square their fav number

fav_num = int(input("What is your favorite number? "))
print(f"Double your favorite number is {fav_num * 2}")
print(f"Half your favorite number is {fav_num / 2}")
print(f"Your favorite number squared is {fav_num ** 2}")



# greet the user

print(f"Hello {name}! Your favorite number is {fav_num}.")

# output the results of the calculations with their number

print(f"Double your favorite number is {fav_num * 2}")
print(f"Half your favorite number is {fav_num / 2}")
print(f"Your favorite number squared is {fav_num ** 2}")

print("Have a nice day!")"""

# error checking
# if the user enters a non-integer value for their favorite number, the program should display an error message and ask them to enter a valid integer.

name = input("What is your name? ")
print (f"Hello {name}!")

while True:
    try:
        fav_num = int(input("What is your favorite number? "))
        break
    except ValueError:
        print("Please enter a valid integer.")
print(f"Double your favorite number is {fav_num * 2}")
print(f"Half your favorite number is {fav_num / 2}")
print(f"Your favorite number squared is {fav_num ** 2}")

print(f"Hello {name}! Your favorite number is {fav_num}.")

print(f"Double your favorite number is {fav_num * 2}")

print(f"Half your favorite number is {fav_num / 2}")

print(f"Your favorite number squared is {fav_num ** 2}")

print("Have a nice day!")