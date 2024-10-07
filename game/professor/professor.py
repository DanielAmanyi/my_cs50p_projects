import random

# Function to generate random integers based on the level
def generate_integer(level):
    lower, upper = 1, 10  # Default range
    if level == 1:
        lower, upper = 0, 9  # Easy level
    elif level == 2:
        lower, upper = 10, 99  # Medium level
    elif level == 3:
        lower, upper = 100, 1000  # Hard level
    return random.randint(lower, upper)

# Main function to control the game flow
def main():
    count = 0  # Counter for how many questions have been asked
    total = 0  # Score tracker
    level = get_level()  # Get the level from the user

    # Outer loop to ask 10 questions
    while count < 10:
        x = generate_integer(level)
        y = generate_integer(level)
        z = x + y

        # Function to get input from the user inside main
        def get_input():
            try:
                return int(input(f"{x} + {y} = "))
            except ValueError:
                return None  # Return None if input is invalid

        i = 0  # Attempt counter for each question
        correct_on_first_attempt = True

        while i < 3:
            sum_input = get_input()

            if sum_input == z:
                if correct_on_first_attempt:  # Award point only on first attempt
                    total += 1
                break  # Move to the next question if correct
            else:
                print("EEE")
                correct_on_first_attempt = False
                i += 1
                if i == 3:
                    print(f"{x} + {y} = {z}")

        count += 1  # Increment the question count

    # End game after 10 questions
    print(f'{total}')  # Display the total score

# Function to get the game level from the user
def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            continue  # Ignore invalid input and ask again

# Call the main function to run the game
if __name__ == "__main__":
    main()
