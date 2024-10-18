import random

def hard_guessing_game():

    lower_bound = 1
    upper_bound = 100
    max_attempts = 7

    number_to_guess = random.randint(lower_bound, upper_bound)
    attempts = 0

    print("Welcome to the Hard Guessing Game!")
    print(f"I'm thinking of a number between {lower_bound} and {upper_bound}.")
    print(f"You have {max_attempts} attempts to guess it.")

    while attempts < max_attempts:
        try:

            guess = int(input("Enter your guess: "))
            attempts += 1

            # Provide feedback
            if guess < lower_bound or guess > upper_bound:
                print(f"Please guess a number between {lower_bound} and {upper_bound}.")
            elif guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

    if attempts == max_attempts:
        print(f"Sorry, you've used all your attempts. The number was {number_to_guess}.")


hard_guessing_game()
