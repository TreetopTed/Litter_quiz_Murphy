def intro():
    print("Welcome to the quiz")
    name = input("What is your name?:  ")
    start = input("Would you like to begin the quiz {}? Y or N?:".format(name))
    if start == "yes" or start == "Yes" or start == "Y" or start == "y":
        print(passkey_gen())
    elif start == "no" or start == "No" or start == "N" or start == "n":
        print("Thank you for your time")
        print(print_dash_line())
        exit()
    else:
        print("Unknown Input")
        print(intro())

# def passkey_gen is used to generate a random passkey that the user
# types in to initiate the quiz.


def passkey_gen():
    import random
    import string
    digits = string.digits
    letter_digit_list = list(string.digits + string.ascii_letters)

    random.shuffle(letter_digit_list)

    # first generates 4 random digits
    sample_str = ''.join((random.choice(digits) for i in range(4)))

    # Now creates random string of length
    # 5 which is a combination of letters and digits
    # Next, concatenate it with sample_str
    sample_str += ''.join((random.choice(letter_digit_list) for i in range(5)))
    a_list = list(sample_str)
    random.shuffle(a_list)

    final_str = ''.join(a_list)
    print("Your Passkey:", final_str)
    passkey_input = input("Please enter your passkey: ")
    if passkey_input == final_str:
        print("Then lets begin!")
        print(print_dash_line())
        print(main_quiz_program())
    else:
        print("Incorrect Passkey")
        print(passkey_gen())
