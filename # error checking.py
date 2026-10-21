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
'''done = True
while done:
    try:
        num = float(input("Please enter a number: \n"))
        done = False
        print(f"The number you entered is: {num}")
    except ValueError:
        print("That is not a valid input. Please enter a number. /nUse a fullstop for decimal numbers.")


print("Thank you for entering a valid number.")'''

# check for valid input and recyling code with a function (v1.2)
# create a function to call every time i ask a user
#  for a number. A function is a chink of code that does
# something.
# Functions can be used over and over again.
# to use a function (call it), write out its name with
# parentheses at the end.
# to create a function, start with the word def
'''def test_float_num():
    while True:
        try:
            num = float(input("Please enter a number: "))
            break
            done = False
            return num
        except ValueError:
            print("That is not a valid input. Please enter a number.")'''

# v1.3 valid input checke
# use p in the function
# more p
'''def input_checker(question):
    while True:
        error = "that is not a valid number."
        print(question)
        try:
            num = float(input())
            break
        except ValueError:
            print(error)

    return(num) # gives back the value of num
                # so i can use it outside of
                # the function

# main routine
num1 = input_checker("please enter your first number: ")
print(f"the number you stored is {num1}")

num2 = input_checker("please enter your second number: ")
print(f"the second number you stored is {num2}")

sun = num1 + num2
print(f"the sum of your two numbers is {sun}")'''

# v1.4 checking for valid input using a try/except method
# using parameters to help make the code more pythonic
# function that asks user to enter a number from a range.


def valid_num(question, low, high):
   error = (f"Whoops, that is not a valid number. Please enter a number between {low} and {high}.")
   while True:
       try:
           response = int(input(question))
           if low <= response <= high:
               break # stop the loop
           
           else:
               print(f"{error}\n")

       except ValueError:
            print(error)
   return response # this makes the response available 
                    # to be used outside of the function

# main routine
if __name__ == "__main__":
    num1 = valid_num("Please enter a number between 1 and 10: ", 1, 10)
    print(f"The number you stored is {num1}")

    num2 = valid_num("Please enter a number between 10 and 15: ", 10, 15)
    print(f"The second number you stored is {num2}")

    num3 = valid_num("Please enter a number between 70 and 90: ", 70, 90)
    print(f"The third number you stored is {num3}")

    # mulitply the results of num1, num2 and num3
    sum = num1 + num2 + num3
    print(f"The sum of your three numbers is {sum}")