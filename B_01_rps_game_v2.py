import random

# check users entered
# valid option
def string_checker(question, valid_ans=("yes", "no")):

    error = f"Please enter a valid option from the following list: {valid_ans}"

    while True:

        # get user response
        user_response = input(question).lower()

        for i in valid_ans:
            # check if item is in list
            if i == user_response:
                return i

            # check if same letter
            # as item on list
            elif user_response == i[0]:
                return i

            # print error
            print(error)
            print()


# displays instructions
def instruction():

    print("""

**** Instructions ****

To begin, choose the number of rounds (or press enter
for infinite mode).

Then play against the computer. You need to choose R (rock)
P (paper) or S (scissors).

The rules are as follows:
-   Paper beats rock
-   Rock beats scissors
-   Scissors beats paper


Good luck!
    """)


# checks for int more than 0 (allows <enter>)
def int_check(question):
    while True:
        error = "Please enter an integer more than 1."

        to_check = input(question)

        # check for inf mode
        if to_check == "":
            return "infinite"

        try:
            response = int(to_check)

            # check if response more than 1
            if response < 1:
                print(error)
            else:
                return response

        except ValueError:
            print(error)

# compares user / comp choices and returns
# result (win, lose, tie,)
def rps_compare(user, comp):

    # user and computer is same, it is a tie
    if user == comp:
        round_result = "tie"

    # there are 3 ways to win
    elif user == "paper" and comp == "rock":
        round_result = "win"
    elif user == "scissors" and comp == "paper":
        round_result = "win"
    elif user == "rock" and comp == "scissors":
        round_result = "win"

    # if not a win or tie, then it's a loss
    else:
        round_result = "lose"

    return round_result


# Main Routine Starts Here

# initialize game variables
mode = "regular"

rounds_played = 0
rounds_tied = 0
rounds_lost = 0

rps_list = ["rock", "paper", "scissors", "xxx"]
game_history = []

print("💎📃✂️ Rock / Paper / Scissors Game ️✂️📃💎")
print()

# ask user if they want instructions
# them if requested
want_instructions = string_checker("Do you want to read the instructions? ")

# check user enters
if want_instructions == "yes":
    instruction()

# ask user for number of rounds / infinite mode
num_rounds = int_check("How many rounds? Or, push <enter> for infinite mode: ")

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5

# game loop starts here
while rounds_played < num_rounds:

    # HEADINGS
    if mode == "infinite":
        rounds_heading = f"\n♾️♾️♾️ Round {rounds_played + 1} (infinite mode) ♾️♾️♾️"
    else:
        rounds_heading = f"\n🎲🎲🎲 Round {rounds_played + 1} of {num_rounds} 🎲🎲🎲"

    print(rounds_heading)

    # randomly choose from rps list
    comp_choice = random.choice(rps_list[:-1])
    print("Computer chose", comp_choice)

    # get user choice
    user_choice = string_checker("Choose: ", rps_list)
    print("you chose", user_choice)

    # if user choice is exit code
    if user_choice == "xxx":
        break

    result = rps_compare(user_choice, comp_choice)

    # adjust game, add results to history
    if result == "tie":
        rounds_tied += 1
        feedback = "👔👔 It's a tie! 👔👔"
    elif result == "lose":
        rounds_lost += 1
        feedback = "😭😭 You lose. 😭😭"
    else:
        feedback = "😎😎 You won. 😎😎"

    # set up round feedback and output it user.
    # add to game history
    round_feedback = f"{user_choice} vs {comp_choice}, {feedback}"
    history_item = f"Round: {rounds_played} - {round_feedback}"

    print(round_feedback)
    game_history.append(history_item)

    # increase number of rounds played
    rounds_played += 1

    # if users in infinite mode, increase number of rounds!
    if mode == "infinite":
        num_rounds += 1

# game loop ends here

# game history / stats area

if rounds_played > 0:
    # calculate stats
    rounds_won = rounds_played - rounds_tied - rounds_lost
    percent_won = rounds_won / rounds_played * 100
    percent_lost = rounds_lost / rounds_played * 100
    percent_tied = 100 - percent_won - percent_lost

    # Output Game Stats
    print("📊📊📊 Game Statistics 📊📊📊")
    print(f"😎 Won: {percent_won:.2f} \t "
          f"😭 Lost: {percent_lost:.2f} \t "
          f"👔 Tied: {percent_tied:,2f}")

    # ask user if they want to see game history
    see_history = string_checker("\nDo you want to see the game history? ")
    if see_history == "yes":
        for i in game_history:
            print(i)

    print()
    print("Thanks for playing!")

else:
    print("🐔🐔🐔 Chicken!!! 🐔🐔🐔")