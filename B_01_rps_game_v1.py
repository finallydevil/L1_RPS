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


# Main Routine Starts Here

# initialize game variables
mode = "regular"
rounds_played = 0

rps_list = ["rock", "paper", "scissors", "xxx"]

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
    print()

    # get user choice
    user_choice = string_checker("Choose: ", rps_list)
    print("you chose", user_choice)

    if user_choice == "xxx":
        break

    rounds_played += 1

    # if users in infinite mode, increase number of rounds!
    if mode == "infinite":
        num_rounds += 1


# game loop ends here

# game history / stats area

# auto testing
to_test = [
    ('xlii', 'invalid'),
    ('0.5', 'invalid'),
    ('0', 'invalid'),
    (1, 1),
    (2, 2),
    ('', 'infinite'),
]

# run test
for i in to_test:
    # retrieve test case
    case = i[0]
    expected = i[1]

    #  get actual value
    actual = int_check(case)

    # comparing
    if actual == expected:
        print(f"✅✅✅ Passed! Case: {case}, expected: {expected}, received: {actual} ✅✅✅")
    else:
        print(f"❌❌❌ Failed! Case: {case}, expected: {expected}, received: {actual} ❌❌❌")
