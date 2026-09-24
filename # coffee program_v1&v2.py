# coffee program
# be abke to interact with.
# esme perry
# 23 sept 2026
# version 1

# TODO: check for qnd record an imput
#       check for valid answer (input checker)
#       Ask questions and respnd

#ask the user whether they like coffee or not
like_coffee = input("Do you like coffee?")
print(like_coffee) # checking the input is stored

# input and respond
print(f"Your answer was '{like_coffee}'")
if like_coffee == "Yes":
    print("That is great! I like coffee too.")
if like_coffee == "yes":
    print("That is great! I like coffee too.")
if like_coffee == "No":
    print("You are missing out! Why not give it a try?")
if like_coffee == "no":
    print("You are missing out! Why not give it a try?")


# version 2
# while loop to test the program
keep_going = ""
while keep_going == "":
    like_coffee = input("Do you like coffee? (Yes/No) ")
    print(f"Your answer was '{like_coffee}'")
    if like_coffee.lower() == "yes":
        print("That is great! I like coffee too.")
        
    elif like_coffee.lower() == "no":
        print("You are missing out! Why not give it a try?")

    # Ask the user a question
    keep_going = input("Do you want to answer again? (Press Enter to continue or type 'exit' to quit) ")
    print("Thank you for participating! Goodbye.")
    if keep_going.lower() == "finish":
        break