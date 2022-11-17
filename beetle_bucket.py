"""Beetle Bucket Choose Your Own Adventure Game."""

__author__ = "730389910"

BEETLE: str = "\U0001FAB2"
points: int = 0
player: str = ""
prompt: int = 0

from random import randint

def main() -> None:
    """Beetle Bucket Entry Point"""
    global points
    greet()
    prompt: int = int(input("If this is your first time playing, or you would like to play again, enter 1. If you would like to exit, enter 2. "))
    if prompt == 1:
        while prompt == 1:
            mode: str = input(("Choose a difficulty by typing either Easy or Hard. If you would like to exit, enter Leave. "))
            if mode == "Easy":
                beetle_bucket_easy()
                print(f"Your beetle total is {points}.")
            elif mode == "Hard":
                print(f"Your beetle total is {beetle_bucket_hard(points)}.")
            elif mode == "Leave":
                prompt = prompt + 1
                leave()
    else:
        leave()


def greet() -> None:
    """Greets the user"""
    global BEETLE
    print("Welcome to Beetle Bucket! Guess which bucket the beetle is in, and see how many you can find!")
    player: str = (input("To start the game, enter your name: "))
    print(f"Welcome, {player}! I hope you catch lots of beetles! {BEETLE}")


def beetle_bucket_easy() -> None:
    """The user picks between 3 buckets"""
    global points
    bucket: int = randint(1, 3)
    guess: int = int(input("Which bucket is the beetle in? Choose a bucket by entering 1, 2, or 3: "))
    if bucket == guess:
        points = points + 1
        print("Congrats! You found a beetle!")
    else:
        print("better luck next time!")


def beetle_bucket_hard(points: int) -> int:
    """The user picks between 10 buckets"""
    bucket: int = 1
    hard_guess: int = int(input("Which bucket is the beetle in? Choose a bucket by entering a number between 1 and 10: "))
    if bucket == hard_guess:
        points = points + 1
        print("Congrats! You found a beetle!")
    else:
        print("better luck next time!")
    return points


def leave() -> None:
    """Exits the program"""
    global prompt
    global BEETLE
    print(f"I hope you enjoyed your game! {BEETLE}")
    prompt = prompt + 1


if __name__ == "__main__":
    main() 
