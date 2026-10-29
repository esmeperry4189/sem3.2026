# fence cost calculator
# 28 october 2026
# art_wizard (esmeperry)

# greet the user 

print("Greetings human, I am the fence cost calculator. Give me your numbers!!!")


# Calculate the cost of fencing for a rectangular area. All measurements
# are in meters.


def number_check(question):
    while True:
        try:
            number = float(input(question))
            if number > 0:
                return number
            print("Value must be greater than zero. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def calculate_rectangle_properties(width, height):
    area = width * height
    perimeter = 2 * (width + height)
    return area, perimeter


while True:
    width = number_check("Please enter a width greater than zero, human: ")
    print(f"You entered a valid width: {width}")

    height = number_check("Please enter a height greater than zero, human: ")
    print(f"You entered a valid height: {height}")

    fence_cost_per_meter = number_check(
        "Please enter the cost of fencing per meter, human: "
    )

    area, perimeter = calculate_rectangle_properties(width, height)
    print(f"Perimeter: {perimeter} meter units")
    total_cost = perimeter * fence_cost_per_meter
    print(f"Human, your total fencing cost is: {total_cost:.2f}")

    another = input(
        "Do you want to calculate more fence costs per meters, human? (yes/no): "
    ).strip().lower()
    if another == "no":
        print("Thank you for using the fencing cost calculator, human. Goodbye!")
        break
    elif another != "yes":
        print("Invalid input. Please enter 'yes' or 'no'.")

