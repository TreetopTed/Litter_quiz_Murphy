def print_dash_line():
    print("---"*15)

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
