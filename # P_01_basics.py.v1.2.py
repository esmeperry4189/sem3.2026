# P_01_basics.py
# art_wizard
# 21/20/2026 octo

# variables can be a string 

"""greeting = "hello world"
print(greeting) 

# varibles can be a number
fav_num = 13
num_string = 5
print(f"My favorite number is {fav_num}")
print(f"My favorite number is {fav_num * 2}")
print(f"My favorite number is {num_string * 5}") 
# this will print the string 5 five times

# varibles can be boolean (true / false)
is_coding_fun = True
print(f"Is coding fun? {is_coding_fun}")"""

# V 1.2
# error checking
# tell the user to enter a number, if they enter a string, tell them to enter a number

try:
    fav_num = int(input("What is your favorite number? "))
    print(f"Double your favorite number is {fav_num * 2}")
    print(f"Half your favorite number is {fav_num / 2}")
    print(f"Your favorite number squared is {fav_num ** 2}")
except ValueError:
    print("Please enter a valid number.")

    try:
        fav_num = int(input("What is your favorite number? "))
        print(f"Double your favorite number is {fav_num * 2}")
        print(f"Half your favorite number is {fav_num / 2}")
        print(f"Your favorite number squared is {fav_num ** 2}")
    except ValueError:
        print("Please enter a valid number.")
