# ~ 1 player
# ~ multi-category, multi-amount each
# ~ player selects a category then an amount available on board
# ~ display answer associated with player's selection
# ~ player enters their response
# ~ compare player response to correct response, update player's total
# ~ display updated board where previously selected answers are no longer available
# ~ repeats until board is completely empty or if player enters "exit"



# Data structures for each category
# dictionary = {amount: (answer, correct response)}
ball = {
    200: ("The beach version of this has been an Olympic sport since 1996", ["volleyball"]),
    400: ("The Brits put 'gridiron' before this sport to refer to the American version", ["football"])
}

career = {
    200: ("This doctor specializes in children & their diseases", ["pediatrician", "a pediatrician"]),
    400: ("Not the automated kind but the human kind, it's a clerk at a bank window", ["teller", "a teller"])
}

# Displays full board
# board = [[ball], [career]]
board = [[200,400],[200,400]]

# Lists acceptable strings for each category player may be trying to select
cat_1 = ["PLAY", "BALL", "PLAY BALL"]
cat_2 = ["CAREER", "DAY", "CAREER DAY"]

# Player begins with total of 0
scoreboard = []



import time

# Introduction-
print("*****************")
print("This is Jeopardy!")
print("*****************")
print()
time.sleep(2)
print("The quiz game-show, where the answers are revealed and the contestants must guess the questions.")
print()
time.sleep(5)
print("Note: Spelling counts in this version.")
print()
time.sleep(3)
print("Let's play.")
print()
time.sleep(1)

# Asks and saves player's name
print("Please enter the contestant's name")
NAME = input("> ").title()
print()

print("Welcome {}!".format(NAME))
time.sleep(1)
print("Thanks for joining today.")
print()
time.sleep(2)

# First set of instructions
print("Now, {}, take a look at the board and make your first selection.".format(NAME))
print('(You can enter "exit" at any time to end game)')
print()
time.sleep(3)

print("===========")
print("PLAY BALL:  {}".format(board[0]))
print("CAREER DAY: {}".format(board[1]))
print()
time.sleep(1)



# Ends program if player enters "exit" at any point of game
def exit_message():
    print("Sorry to see you go, {}. Hope you come back to play again.".format(NAME))
    exit()

# Determines if game should stay in while loop of the main loop
def check(board):

    if (board[0] == [] and board[1] == []):
        return True
    
# Updates board, cleared out answers already selected
def update_board(category, amount):

    # Set index
    i = 0

    # Knowing which dictionary, find amount and remove from that board
    if category == ball:
        for i, available in enumerate(board[0]):
            if available == amount:
                # Removes amount from board
                board[0].pop(i)

    # Knowing which dictionary, find amount and remove from that board
    if category == career:
        for i, available in enumerate(board[1]):
            if available == amount:
                #Removes amount from board
                board[1].pop(i)

    # Displays updated board to select from
    print()
    print("===========")
    print("PLAY BALL:  {}".format(board[0]))
    print("CAREER DAY: {}".format(board[1]))
    print()

    return board

# Asks for response and pulls correct response, then compares the two; also updates then confirms new total
def compare(correct_resp, amount, scoreboard):

    # Prompt
    response = input("> What is... ").lower().strip()
    print()

    # Player can select to end game with "exit"
    if response == "exit":
        exit_message()

    # If player response matches correct response
    elif response in correct_resp:

        # Updates score
        scoreboard.append(amount)
        score = sum(scoreboard)
 
        # Confirms correct response and new total to player
        if score < 0:
            print("{} is correct. Your total is now -${}.".format(correct_resp[0].title(), abs(score)))
            print()
            time.sleep(2)

        else:
            print("{} is correct. Your total is now ${}.".format(correct_resp[0].title(), score))
            print()
            time.sleep(2)

    # If response does not match, display correct response and confirm player's new total
    elif not (response in  correct_resp):

        # Updates score
        amount = -amount
        scoreboard.append(amount)
        score = sum(scoreboard)

        # Shows player's response, confirms correct response, and confirms new total to player
        if score < 0:
            print("{} is incorrect. We're looking for {}. Your total is now -${}.".format(response.title(), correct_resp[0].lower(), abs(score)))
            print()
            time.sleep(2)

        else:
            print("{} is incorrect. We're looking for {}. Your total is now ${}.".format(response.title(), correct_resp[0].lower(), score))
            print()
            time.sleep(2)

    return score

# Retrieves correct response to be compared
def pull_correct_resp(category, amount):
    
    # Knowing which dictionary, search for correct response
    if category == ball:
        correct_resp = ball[amount][1]
        return correct_resp

    # Knowing which dictionary, search for correct response
    elif category == career:
        correct_resp = career[amount][1]
        return correct_resp

# Given the category and amount combination selected, retrieves and displays answer
def pull_answer(category, amount):

    # Prints answer specific to dictionary and key selected
    if category == ball:
        answer = ball[amount][0]
        print("[", answer.upper(), "]")
        return answer
            
    # Prints answer specific to dictionary and key selected
    elif category == career:
        answer = career[amount][0]
        print("[", answer.upper(), "]")
        return answer
    
# Asks player to select an amount
def amount_select(category, board):
    
    # Prompt
    print("and the amount")

    while True:

        amount = input("> ").strip()
        print()

        # Player can select to end game with "exit"
        if "exit" in amount:
            exit_message()

        # Error message if not an integer
        elif not amount.isdigit():
            print("Sorry, invalid amount.")
            print("Select a different amount in the category")

        # Checks if valid amount entered
        else:
            
            # Converts amount from string to integer
            amount = int(amount)
        
            # Knowing which dictionary, search within that dictionary
            if category == ball:
                # If amount is still a key within dictionary
                if amount in board[0]:
                    return amount

                elif amount not in board[0]:
                    print("Sorry, amount entered is not in this category.")
                    print("Select a different amount in the category")

            # Knowing which dictionary, search within that dictionary
            if category == career:
                # If amount is still a key within dictionary
                if amount in board[1]:
                    return amount

                elif amount not in board[1]:
                    print("Sorry, amount entered is not in this category.")
                    print("Select a different amount in the category")

# Asks player to select a category
def category_select():

    # Prompt
    print("Select a category")

    while True:

        category = input("> ").upper()
        print()

        # Player can select to end game with "exit"
        if category == "EXIT":
            exit_message()
        
        elif category in cat_1:

            # Error message if category is now empty
            if board[0] == []:
                print("Sorry, category is now empty.")
                print("Select another category")

            else:
                # To know which dictionary to search in
                category_select = ball

                return category_select

        elif category in cat_2:

            # Error message if category is now empty
            if board[1] == []:
                print("Sorry, category is now empty.")
                print("Select another category")

            else:
                # To know which dictionary to search in
                category_select = career

                return category_select              

        else:
            # Error message if player enters an invalid category
            print("Sorry, invalid category.")
            print("Select another category")

# Runs through game until board is cleared
def main_loop(board):

    while not check(board):

        category = category_select()
        amount = amount_select(category, board)
        correct_resp = pull_correct_resp(category, amount)
        pull_answer(category, amount)
        total = compare(correct_resp, amount, scoreboard)
        board = update_board(category, amount)
    
    # If player amount is in the positive
    if total > 0:
        print("Congratulations {}, you've won ${}.".format(NAME, total))
        print("Don't spend it all in one place. Thanks for playing.")

    # If player amount is in the negative
    elif total < 0:
        print("Sorry, {}. Unfortunately you ended with -${} and will be walking away with nothing today.".format(NAME, abs(total)))
        print("Thanks for playing.")

    # If player amount is zero
    elif total == 0:
        print("{}, your final total is ${}.".format(NAME, abs(total)))
        print("No harm done. Thanks for playing.")



# Begin game-
main_loop(board)