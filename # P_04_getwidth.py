# P_04_getwidth.py
# art_wizard
# 21/20/2026 octo
# v1.0.0

# ask user for width and height and loop until they
# enter a number that is more than zero


'''while True:
    width = input("Please enter a width greater than zero: ")
    try:
        width = float(width)
        if width > 0:
            break
        else:
            print("Width must be greater than zero. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

print(f"You entered a valid width: {width}")'''


# number checker P_05_numchecker.py
# 23/20/2026 octo
# finished version 1.0.1

while True:
    width = input("Please enter a width greater than zero: ")
    try:
        width = float(width)
        if width > 0:
            break
        else:
            print("Width must be greater than zero. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

print(f"You entered a valid width: {width}")

def number_check(question):
    while True:
        user_input = input(question)
        try:
            number = float(user_input)
            return number
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

while True:
    height = input("Please enter a height greater than zero: ")
    try:
        height = float(height)
        if height > 0:
            break
        else:
            print("Height must be greater than zero. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

print(f"You entered a valid height: {height}")

# make a function that finds the area and preimeter of a rectangle given the width and height

def calculate_rectangle_properties(width, height):
    area = width * height
    perimeter = 2 * (width + height)
    return area, perimeter

area, perimeter = calculate_rectangle_properties(width, height)
print(f"Area: {area} square units, Perimeter: {perimeter} units")

# ask the user if they want to calculate the area and perimeter of another rectangle
while True:
    another = input("Do you want to calculate the area and perimeter of another rectangle? (yes/no): ").strip().lower()
    if another == 'yes':
        width = number_check("Please enter a width greater than zero: ")
        height = number_check("Please enter a height greater than zero: ")
        area, perimeter = calculate_rectangle_properties(width, height)
        print(f"Area: {area} square units, Perimeter: {perimeter} units")
    elif another == 'no':
        print("Thank you for using the rectangle calculator. Goodbye!")
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
