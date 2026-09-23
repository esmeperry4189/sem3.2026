# test
# This is a comment. A # starts a comment
# Semester 2 Year 10DGT 2026 Demo code
# Author: Esme Perry
# Verson: 1


# Demonstration of how a while loop works
# and how indenting affects the code
keep_going = ""
while keep_going == "":
    print("looping")
    print("still looping")

keep_going = input("Do you want to keep going?")
while keep_going == "":
    keep_going = input("Do you want to keep going?")
# demonstrating error catching
try:
    response = int(input("Number: "))
    print("You entered an interger.")

except ValueError:
    print("Yikes! That is not an interger. Please try again.")

