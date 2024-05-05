import random

choices = ["r", "p", "s"]

choice_meaning = {"r": "Rock", "p": "Paper", "s": "Scissors"}

user_score = 0
ai_score = 0
set_score = int(input("Set score: "))

while True:

    user_choice = input("Select from Rock, Paper, Scissors: (r, p,s) ")

    ai_choice = random.choice(choices)

    if user_choice in choices:
        print(
            f"Your choice is {choice_meaning[user_choice]}. AI choice is {choice_meaning[ai_choice]}."
        )
        # r > s - p > r - s > p
        if user_choice == ai_choice:
            print("Tie!")
        elif user_choice == "s" and ai_choice == "p":
            print("User + 1")
            user_score += 1
        elif user_choice == "r" and ai_choice == "s":
            print("User + 1")
            user_score += 1
        elif user_choice == "p" and ai_choice == "r":
            print("User + 1")
            user_score += 1
        else:
            print("AI + 1")
            ai_score += 1
    elif user_choice == "exit":
        print("Exit")
        exit(0)

    else:
        print("Invalid command")

    print(f"User score is = {user_score} / Ai score is = {ai_score}")

    if user_score == set_score or ai_score == set_score:
        break

    print("\n ", "-" * 10, "\n")

if user_score == set_score:
    print(f"User won with score: {user_score}")
else:
    print(f"Ai won with score: {ai_score}")
