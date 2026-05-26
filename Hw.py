import random

secret = random.choice([1,2,3,4,5])
guess = 0

while guess != secret:
    guess = int(input("guess(1 to 5): "))

    if guess < secret:
        print("Too low")
    elif guess > secret:
        print("Too high")

    print("You win! ")