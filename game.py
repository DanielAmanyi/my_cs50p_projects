import random

# Function to get a valid number from the user
def get_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass  # Continue prompting if input is invalid

# Main program
level = get_number("Level: ")
random_number = random.randint(1, level)

while True:
    guess = get_number("Guess: ")
    if guess > random_number:
        print("Too large!")
    elif guess < random_number:
        print("Too low!")
    else:
        print("Just right!")
        break
