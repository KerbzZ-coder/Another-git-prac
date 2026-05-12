import random

secret_number = random.randint(1,10)
guess = 0

while guess != secret_number:
    guess = int(input("Guess the secret number from (1-10): ").strip())
    if guess != secret_number:
        print("Wrong! Try again")

print("You got it right!!")