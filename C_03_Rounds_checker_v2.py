# checks for int more than 0 (allows <enter>)
def int_check(to_check):
    while True:
        error = "Please enter an integer more than 1."

        # check for inf mode
        if to_check == "":
            return "infinite"

        try:
            response = int(to_check)

            # check if response more than 1
            if response < 1:
                print(error)
                return "invalid"
            else:
                return response

        except ValueError:
            print(error)
            return "invalid"


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
