# Number Guessing Game
import random

num = random.randint(1, 100)

while True:
    guess = int(input("Guess the number between 1 and 100: "))

    if guess < num:
        print("Too low! Try again.")
    elif guess > num:
        print("Too high! Try again.")
    else:
        print("Correct! You guessed the number.")
        break
