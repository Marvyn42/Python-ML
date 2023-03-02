import random


def more_or_less(random_int, compteur):
    compteur += 1
    if (int(answer) == random_int):
        if (random_int == 42):
            print("The answer to the ultimate question of life, \
the universe and everything is 42.")
        print(f"Congratulations! You got it on your first try!")\
            if compteur == 1\
            else print(f"Congratulations, you got it in {compteur} attempts")
        exit(0)
    elif (int(answer) < random_int):
        print("Too low !\n")
    elif (int(answer) > random_int):
        print("Too high !\n")
    return (compteur)


def welcome_message():
    print("""This is an interactive guessing game!
You have to enter a number between 1 and 99 to find out the secret number.
Type 'exit' to end the game.
Good luck!\n""")


if __name__ == "__main__":
    welcome_message()
    random_int = random.randint(1, 99)
    compteur = 0
    print(random_int)

    while True:
        answer = input("What's your guess between 1 and 99?\n>> ")
        if (answer == "exit"):
            print("Goodbye !")
            exit(0)
        if (answer.isdigit() is False):
            print("That's not a number.\n")
            compteur += 1
            continue
        compteur = more_or_less(random_int, compteur)
