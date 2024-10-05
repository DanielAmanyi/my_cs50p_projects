<<<<<<< HEAD
# my_cs50p_projects
=======
# Game

## CS50 Problem Set 4 - Game

### Author: [Your Name]

---

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)
- [Credits](HarvardCS50)
- [License](#license)

---

## Description

**Game** is a simple Python-based number guessing game developed as part of [CS50's Problem Set 4](https://cs50.harvard.edu/x/2023/psets/4/). In this game, the user is prompted to select a level that determines the range of the random number to guess. The user then attempts to guess the randomly generated number, receiving feedback on whether their guess is too high, too low, or correct. The game continues until the correct number is guessed.

---

## Features

- **Level Selection**: Choose a difficulty level to set the range of the random number.
- **Input Validation**: Ensures that the user inputs valid positive integers for both level and guesses.
- **Interactive Feedback**: Provides real-time feedback on each guess.
- **Replay Option**: Allows users to play multiple rounds without restarting the program.

---

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/game.git
   cd game
   ```

2. **Ensure Python is Installed**

   Make sure you have Python 3 installed on your system. You can check your Python version with:

   ```bash
   python3 --version
   ```

   If Python is not installed, download it from the [official website](https://www.python.org/downloads/) and follow the installation instructions.

---

## Usage

1. **Run the Program**

   Navigate to the project directory and run the game using Python:

   ```bash
   python3 game.py
   ```

2. **Follow the Prompts**

   - **Enter Level**: Input a positive integer to set the range for the random number (e.g., level 10 means the number is between 1 and 10).
   - **Enter Guess**: Input your guess based on the selected level.
   - **Receive Feedback**: The program will inform you if your guess is too large, too low, or just right.
   - **Replay Option**: After guessing correctly, choose whether to play again or exit.

---

## Example

```
WELCOME TO THE NUMBER GUESSING GAME!

Level: 10
Guess: 5
Too low!
Guess: 8
Too large!
Guess: 7
Just right!

Do you want to play again? (y/n): y

Level: 15
Guess: 10
Too low!
Guess: 12
Too large!
Guess: 11
Just right!

Do you want to play again? (y/n): n

Thanks for playing!
```

---

## Credits

- **CS50**: The original problem set is part of [Harvard's CS50](https://cs50.harvard.edu/x/2023/) course.
- **Amanyi Daniel Sunday**: Implemented the Python version of the Game.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Contact

## For any questions or suggestions, feel free to contact me at [amanyidaniel.io@gmail.com]

**Happy Coding!**
>>>>>>> 1365bd1 (Initial commit)
