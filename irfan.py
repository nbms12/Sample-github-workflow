
import random

print("🎮 WELCOME TO NUMBER GUESSING GAME!")
print("I am thinking of a number between 1 and 20.")

secret_number = random.randint(1, 20)
attempts = 0

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("🎉 Congratulations! You won!")
        print("Number of attempts:", attempts)
        break

print("Thanks for playing!")
