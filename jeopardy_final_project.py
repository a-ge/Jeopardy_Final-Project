# ~ 1 player
# ~ multi-category, multi-amount each
# ~ player selects a category then an amount available on board
# ~ display answer associated with player's selection
# ~ player enters their response
# ~ compare player response to correct response, update player's total
# ~ display updated board where previously selected answers are no longer available
# ~ repeats until board is completely empty or if player enters "exit"



# Stores all data for each category
# {category: (acceptable categories),
#     board: [board for available amounts]
#    amount: (answer, [correct response]...}
categories = (
{"cat": ("PLAY BALL", "PLAY", "BALL"),
"board": [200, 400],
200: ("The beach version of this has been an Olympic sport since 1996", ["volleyball"]),
400: ("The Brits put 'gridiron' before this sport to refer to the American version", ["football"])
},

{"cat": ("CAREER DAY", "CAREER", "DAY"),
"board": [200, 400],
200: ("This doctor specializes in children & their diseases", ["pediatrician"]),
400: ("Not the automated kind but the human kind, it's a clerk at a bank window", ["teller"])
})



import time

# Introduction-
print()
print()
print("*****************")
print("This is Jeopardy!")
print("*****************")
print()
time.sleep(2)
print("The quiz game-show, where the answers are revealed and the contestants must guess the questions.")
print()
time.sleep(4)
print("Note: Spelling counts in this version.")
print()
time.sleep(3)
print("Let's play.")
print()
time.sleep(1)

# Asks and saves player's name
print("Please enter the contestant's name")
NAME = input("> ").title().strip()
print()

print("Welcome {}!".format(NAME))
time.sleep(1)
print("Thanks for joining today.")
print()
time.sleep(2)

# First set of instructions
print("Now, {}, take a look at the board and make your first selection.".format(NAME))
print("(You can enter 'exit' at any time to end game)")
print()
print("============ ============")
print(" {}  | {}".format(categories[0]["cat"][0], categories[1]["cat"][0]))
print(" ___________|___________")
print("    {}     |    {}".format(categories[0]["board"][0],categories[1]["board"][0]))
print("    {}     |    {}".format(categories[0]["board"][1],categories[1]["board"][1]))
print()
time.sleep(1)



# Ends program if player enters 'exit' at any point of game
def exit_message():
    print("Sorry to see you go, {}. Hope you come back to play again.".format(NAME))
    exit()

# Determines if game should stay in while loop of the main loop
def check(categories):

    for cat in categories:
        for i, amts in enumerate(cat["board"]):
            if amts != "   ":
                return True

# Updates board, cleared out answers already selected
def update_board(category, amount):

    # Replaces used amount with blank
    for i, available in enumerate(category["board"]):
        if available == amount:
            category["board"][i] = "   "

    # Displays updated board that player can select from
    print()
    print("============ ============")
    print(" {}  | {}".format(categories[0]["cat"][0], categories[1]["cat"][0]))
    print(" ___________|___________")
    print("    {}     |    {}".format(categories[0]["board"][0],categories[1]["board"][0]))
    print("    {}     |    {}".format(categories[0]["board"][1],categories[1]["board"][1]))
    print()

# Asks for response and pulls correct response, then compares the two; updates then confirms new total
def compare(category, amount, score):

    # Prompt to get player's response
    response = input("> What is... ").lower().strip()
    print()

    # In case player adds "a_" and/or question mark to response
    if response.endswith("?"):
        response = response[:-1]
    if response.startswith("a "):
        response = response[2:]

    # Retrieves list of acceptable correct responses to be compared
    correct_resp = category[amount][1]

    # Player can select to end game with "exit"
    if response == "exit":
        exit_message()

    # If player response matches correct response
    elif response in correct_resp:

        # Updates score
        total = score + amount

        # Confirms correct response and new total to player
        if total < 0:
            print("{} is correct. Your total is now -${}.".format(correct_resp[0].title(), abs(total)))
            print()
            time.sleep(2)

        else:
            print("{} is correct. Your total is now ${}.".format(correct_resp[0].title(), total))
            print()
            time.sleep(2)

    # If response does not match, display correct response and confirm player's new total
    elif not (response in  correct_resp):

        # Updates score
        total = score - amount

        # Shows player's response, confirms correct response, and confirms new total to player
        if total < 0:
            print("{} is incorrect. We're looking for {}. Your total is now -${}.".format(response.title(), correct_resp[0].lower(), abs(total)))
            print()
            time.sleep(2)

        else:
            print("{} is incorrect. We're looking for {}. Your total is now ${}.".format(response.title(), correct_resp[0].lower(), total))
            print()
            time.sleep(2)

    return total

# Given the category and amount combination selected, retrieves and displays answer
def pull_answer(category, amount):

    answer = category[amount][0]
    print("[", answer.upper(), "]")
    
# Asks player to select an amount
def amount_select(category):
    
    # Prompt
    print("and the amount")

    while True:
        # Where player enters their amount selection
        amount = input("> ").strip()
        print()

        # Player can select to end game with "exit"
        if "exit" in amount:
            exit_message()

        # Error message if not an integer
        elif not amount.isdigit():
            print("Sorry, invalid amount.")
            print("Select a different amount in the category")

        # Checks if a valid amount was entered
        else:
            
            # Converts amount from string to integer
            amount = int(amount)
        
            # Checks if amount entered is available
            if amount in category["board"]:
                return amount

            # Error message if invaild amount
            elif amount not in category["board"]:
                print("Sorry, amount entered is not in this category.")
                print("Select a different amount in the category")

# Asks player to select a category
def category_select():

    # Prompt
    print("Select a category")

    while True:
        # Where player enters their category selection
        category = input("> ").upper().strip()
        print()

        # Player can select to end game with "exit"
        if category == "EXIT":
            exit_message()

        # Checks if category entered is acceptable
        for i, cat in enumerate(categories):
            if category in cat["cat"]:

                # Checks if that category is empty
                for amts in categories[i]["board"]:
                    if amts != "   ":
                        category_select = categories[i]
                        return category_select

                print("Sorry, category is now empty.")
                print("Select another category")
                break
                    
        # Error message if player enters an invalid category
        else:
            print("Sorry, invalid category.")
            print("Select another category")

# Runs through game until board is cleared
def main_loop(categories):

    # Player begins with score of zero
    score = 0

    while check(categories):
        category = category_select()
        amount = amount_select(category)
        pull_answer(category, amount)
        score = compare(category, amount, score)
        update_board(category, amount)
    
    # End of game salutations
    if score > 0:
        print("Congratulations {}, you've won ${}.".format(NAME, score))
        print("Don't spend it all in one place. Thanks for playing.")

    elif score < 0:
        print("Sorry, {}. Unfortunately you ended with -${} and will be walking away with nothing today.".format(NAME, abs(score)))
        print("Thanks for playing.")

    elif score == 0:
        print("{}, your final total is ${}.".format(NAME, score))
        print("No harm done. Thanks for playing.")



# Begin game-
main_loop(categories)