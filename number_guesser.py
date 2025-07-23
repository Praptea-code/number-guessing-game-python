import random

# Generate a random number
def generate_random_number():
    return random.randint(1, 100)

# Take the user's guess and give hints
def user_guess(secret_number):
    while True:
        try:
            guess = int(input("Guess a number between 1 and 100: "))
            if guess < secret_number:
                print("Too low, try again!")
            elif guess > secret_number:
                print("Too high, try again!")
            else:
                print("You guessed the number correctly, YAYY!!")
                break
        except:
            print("Please enter a valid number.")

# Game function
def game():
    while True:
        secret_number = generate_random_number()
        user_guess(secret_number)
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break

# Start the game
game()


