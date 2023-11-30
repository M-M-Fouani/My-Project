import random

while True:
    print("\nWelcome to Guess the Number!")
    print("I'm thinking of a number between 1 and 100.")

    secret_number = random.randint(1, 100)

    attempts = 0

    while True:

        guess = int(input("\nYour guess: "))
        attempts += 1

        if guess == secret_number:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break
        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

    play_again = input("\nDo you want to play again? (yes/no): ")
    if play_again.lower() != 'yes':
        print("\nThanks for playing! Goodbye.\n")
        break