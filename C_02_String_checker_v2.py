# check users entered
# valid option
def string_checker(user_responce, valid_ans):
    while True:

        # get user responce
        user_responce = user_responce.lower()

        for i in valid_ans:
            # check if item is in list
            if i == user_responce:
                return i

            # check if same letter
            # as item on list
            elif user_responce == i[0]:
                return i

        return "invalid"


# auto testing
to_test = [
    ("Rock", "rock"),
    ("PAPER", "paper"),
    ("scissors", "scissors"),
    ("R", "rock"),
    ("P", "paper"),
    ("S", "scissors"),
    ("XXX", "xxx"),
    ("x", "xxx"),
    ("random", "invalid"),

]

# run test
for i in to_test:
    # retrieve test case
    case = i[0]
    expected = i[1]

    #  get actual value
    actual = string_checker(case, ["rock", "paper", "scissors", "xxx"])

    # comparing
    if actual == expected:
        print(f"✅✅✅ Passed! Case: {case}, expected: {expected}, received: {actual} ✅✅✅")
    else:
        print(f"❌❌❌ Failed! Case: {case}, expected: {expected}, received: {actual} ❌❌❌")
