# ----------defs----------

# prints 15 "---" in a line. I will use it to separate the different sections
# of the program, like the intro and the main program.


def print_dash_line():
    print("---"*15)

# def intro() prints the intro, which asks for the user's name,
# and whether they want to start the quiz.
# Presents a yes/no option with multiple alternatives.
# when I print the intro in main, all I will have to put is print(intro())


def intro():
    print("Welcome to the quiz")
    name = input("What is your name?:  ")
    start = input("Would you like to begin the quiz {}? Y or N?:".format(name))
    if start == "yes" or start == "Yes" or start == "Y" or start == "y":
        print(main_quiz_program())
    elif start == "no" or start == "No" or start == "N" or start == "n":
        print("Thank you for your time")
        print(print_dash_line())
        exit()
    else:
        print("Unknown Input")
        print(intro())

# def passkey_gen is used to generate a random passkey that the user
# types in to initiate the quiz.


def main_quiz_program():
    while True:
        for question, alternatives in questions.items():
            correct_answer = alternatives[0]
            sorted_alternatives = sorted(alternatives)
            for label, alternative in enumerate(sorted_alternatives):
                print(f"   {label}) {alternative}")

            answer_label = int(input(f"{question}: "))
            answer = sorted_alternatives[answer_label]
            if answer == correct_answer:
                print("Correct!")
            else:
                print(f"The answer is {correct_answer!r}, not {answer!r}")

# play_again option. Gives user option to replay the quiz.
# If "y" or "Y" is inputted, quiz replays.
# If "n" or "N" is inputted, program terminates with exit message.
# If anything else is inputted,
# an error message appears and the program terminates.
        play_again = input("Play again? (Y/N): ")
        if play_again == "n" or play_again == "N":
            print("Thank you for your time")
            print(print_dash_line())
            exit()
        elif play_again == "y" or play_again == "Y":
            print("Let's go again!")
            print(main_quiz_program())
        else:
            print("Unknown Input")
            break

# dictionary of questions of quiz. Questions are multiple
# choice with three options.


questions = {
    "What is recyclable out of the items above?":
        ["Plastic Bottles", "Tin Foil", "Nylon"],
    "Where is there more litter?":
        ["Auckland", "Wellington", "Dunedin"],
    "What is the most littered item in Auckland?":
        ["Cigarettes", "Plastic Bottles", "Gum"],
    "What is the maximum fine for littering in New Zealand?":
        ["$1000", "$800", "$1200"],
    "What is the minimum fine for littering in New Zealand?":
        ["$100-$400", "$425-$500", "$550-$800"],
    "What is non-recyclable out og the items above?":
        ["Plastic Bags", "Aluminium Cans", "Milk Cartons", "Plastic Bottles"]
    }

#  ----------main----------
print(intro())