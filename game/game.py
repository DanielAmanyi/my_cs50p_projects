import random


def get_level():
    level = 0
    while level < 1:
        try:
            level = int(input("Level: "))
            continue
        except ValueError:
            continue
    return level

def get_guess():
    guess = 0
    while guess < 1:
        try:
            guess = int(input("Guess: "))
            continue
        except ValueError:
            continue
    return guess



level = get_level()
# guess = get_guess()

x = random.randint(1,level)
# print("random:",x)
while True:
    guess = get_guess()
    if guess > x:
        print("Too large!")
    elif guess < x:
        print("Too small!")
    else:
        print("Just right!")
        break

