# error checking
# 10 DGT26
# 14 octo 2026

# code that tests whether a valid input was given (v1)
'''done = True # boolean varible set to True
while True:
    num = int(input("Please enter your value as an integer: "))
    done = False

    print(f"The number you for entered is:", {num})'''

# my working solution
# using a try and except method to check for valid input (v1.1)
# use try and accept method to catch errors
# this method tries for a valid input
'''done = True
while done:
    try:
        num = int(input("Please enter your value as an integer: "))
        done = False
        print(f"The number you entered is:", {num})
    except ValueError:
        print("That is not a valid input. Please enter an integer.")'''

# teacher's solution
# using a try and except method to check for valid input (v1.2)
# use try and accept method to catch errors
# this method tries for a valid input
done = True
while done:
    try:
        num = float(input("Please enter a number: \n"))
        done = False
        print(f"The number you entered is: {num}")
    except ValueError:
        print("That is not a valid input. Please enter a number. /nUse a fullstop for decimal numbers.")


print("Thank you for entering a valid number.")

