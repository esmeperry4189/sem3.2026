# P_04_getwidth.py
# art_wizard
# 21/20/2026 octo
# v1.0.0

# ask user for width and loop until they
# enter a number that is more than zero


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
