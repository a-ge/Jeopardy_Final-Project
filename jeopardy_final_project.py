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
#    amount: (answer, [acceptable responses]...}
categories = (
{"cat": ("PLAY BALL", "PLAY", "BALL"),
"board": [200, 400, 600, 800, 1000],
200: ("The beach version of this has been an Olympic sport since 1996", ["volleyball"]),
400: ("The Brits put 'gridiron' before this sport to refer to the American version", ["football"]),
600: ("You need just a ball & a wall to play this sport with a body part in its name", ["handball"]),
800: ("The ITTF is the International Federation for this ball & racket sport-- that's the 'TT'", ["table tennis"]),
1000: ("It was invented in the winter of 1891 in Springfield, Massachusetts", ["basketball"])
},

{"cat": ("PLURALIZE IT", "PLURALIZE", "IT"),
"board": [200, 400, 600, 800, 1000],
200: ("Ox (4 letters, 4 legs)", ["oxen"]),
400: ("Moose (4 legs, 5 letters)", ["moose"]),
600: ("Cactus (5 letters)", ["cacti"]),
800: ("Stimulus (7 letters)", ["stimuli"]),
1000: ("Forum (4 letters)", ["fora"])
})

import time

def exit_message():
    ''' End program if player enters 'exit' at any point of game. '''

    print("Sorry to see you go, {}. Hope you come back to play again.".format(NAME))
    exit()

def check(categories):
    ''' Determine if game should stay in while loop of the main loop. '''

    for i, cat in enumerate(categories):
        for amts in cat["board"]:
            # Board is cleared if all int's are gone (replaced by str's)
            if type(amts) == int:
                return True

def update_board(category, amount):
    ''' Update board, clear out answers already selected. '''

    # Replaces used amount with blank
    for i, amts in enumerate(category["board"]):
        if amts == amount:
            if amount == 1000:
                category["board"][i] = "    "
            else:
                category["board"][i] = "   "

    # Displays updated board that player can select from
    print('\n============= =============\n')
    print("  {}  | {}".format(categories[0]["cat"][0], categories[1]["cat"][0]))
    print(" ____________|____________")
    print("     {}     |     {}".format(categories[0]["board"][0],categories[1]["board"][0]))
    print("     {}     |     {}".format(categories[0]["board"][1],categories[1]["board"][1]))
    print("     {}     |     {}".format(categories[0]["board"][2],categories[1]["board"][2]))
    print("     {}     |     {}".format(categories[0]["board"][3],categories[1]["board"][3]))
    print("    {}     |    {}".format(categories[0]["board"][4],categories[1]["board"][4]))
    print()

def compare(category, amount, score):
    ''' Ask for response and pull correct response, then compare the two; update then confirm new total. '''

    # Prompt to get player's response
    response = input("> What is... ").lower().strip()
    print()

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

def pull_answer(category, amount):
    ''' Given the category and amount combination selected, retrieve and display answer. '''

    answer = category[amount][0]
    print("[", answer.upper(), "]")
    
def amount_select(category):
    ''' Ask player to select an amount. '''

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
            print('Sorry, invalid amount.\nSelect a different amount in the category')

        # Checks if a valid amount was entered
        else:
            
            # Converts amount from string to integer
            amount = int(amount)
        
            # Checks if amount entered is available
            if amount in category["board"]:
                return amount

            # Error message if invaild amount
            elif amount not in category["board"]:
                print('Sorry, amount entered is not in this category.\nSelect a different amount in the category')


def category_select():
    ''' Ask player to select a category. '''
    
    # Prompt
    print("Select a category")

    while True:
        # Where player enters their category selection
        category = input("> ").strip().upper()
        print()

        # Player can select to end game with "exit"
        if category == "EXIT":
            exit_message()

        # Checks if category entered is acceptable
        for i, cat in enumerate(categories):
            if category in cat["cat"]:
                category_select = categories[i]

                # Checks if that category is empty
                for amts in category_select["board"]:
                    if type(amts) == int:
                        return category_select
                
                print('Sorry, category is now empty.\nSelect another category')
                break
                    
        # Error message if player enters an invalid category
        else:
            print('Sorry, invalid category.\nSelect another category')


def main_loop(categories):
    ''' Run through game until board is cleared. '''

    # Introduction-
    print('\n\n*****************\nThis is Jeopardy!\n*****************\n')
    time.sleep(2)
    print('The quiz game-show, where the answers are revealed and the contestants must guess the questions.\n')
    time.sleep(4)
    print('Note: Spelling counts in this version.\n')
    time.sleep(3)
    print("Let's play.\n")
    time.sleep(1)

    # Asks and saves player's name
    print("Please enter the contestant's name")
    NAME = input("> ").title()
    print()

    print("Welcome {}!".format(NAME))
    time.sleep(1)
    print('Thanks for joining today.\n')
    time.sleep(2)

    # First set of instructions
    print("Now, {}, take a look at the board and make your first selection.".format(NAME))
    print("(You can enter 'exit' at any time to end game)")
    update_board(categories[0], 0)
    time.sleep(1)

    # Player begins with score of zero
    score = 0

    # Will run until there are no more integers on the board
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