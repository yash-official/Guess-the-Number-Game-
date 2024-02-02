import random

def guess_the_number():
    # Get the player's name
    player_name = input("Enter your name: ")

    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    attempts = 0
    max_attempts = 5
    
    print("Welcome to Guess the Number Game! presented by Yash Srivastava")
    print("I'm thinking of a number between 1 and 100.")
    print("You'll get max to max 5 attempts only,so think before you guess.")

    while attempts < max_attempts:
        try:
            # Get the player's guess
            guess = int(input("Guess the number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        attempts += 1

        if guess < secret_number:
            print("Try again. The number is higher.")
        elif guess > secret_number:
            print("Try again. The number is lower.")
        else:
            print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
            break

    if attempts >= max_attempts:
        print(f"Sorry, you've reached the maximum number of attempts. The secret number was {secret_number}.")

if __name__ == "__main__":
    guess_the_number()
