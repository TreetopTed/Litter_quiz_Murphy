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


# dictionary of questions of quiz. Questions are multiple
# choice with three options.


questions = {
    "What is recyclable out of the items above?":
        ["Plastic Bottles", "Tin Foil", "Nylon"],
    "Where is there more litter?":
        ["Auckland", "Wellington", "Dunedin"],
    "What is the most littered item in Auckland?":
        ["Cigarettes", "Plastic Bottles", "Gum"]
    }

#  ----------main----------
print(intro())
