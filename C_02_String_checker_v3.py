# check users entered
# valid option
def string_checker(question, valid_ans=["yes", "no"]):

    error = f"Please enter a valid option from the following list: {valid_ans}"

    while True:

        # get user responce
        user_responce = input(question).lower()

        for i in valid_ans:
            # check if item is in list
            if i == user_responce:
                return i

            # check if same letter
            # as item on list
            elif user_responce == i[0]:
                return i

            # print error
            print(error)
            print()


# main routine goes here

rps_list = ["rock", "paper", "scissors"]

want_instructions = string_checker("Do you want to see the instructions? ",)

print("You chose: ", want_instructions)

user_choice = string_checker("Choose: ", rps_list)
print("You chose: ", user_choice)