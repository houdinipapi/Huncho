"""
- Implement a program that:
    Prompts the user for a level.
    If the user does not input 1, 2, or 3, the program should prompt again.
- Randomly generates ten (10) math problems formatted as X + Y = ,
wherein each of X and Y is a non-negative integer with digits.
- No need to support operations other than addition (+).
- Prompts the user to solve each of those problems.
- If an answer is not correct (or not even a number),
the program should output EEE and prompt the user again,
allowing the user up to three tries in total for that problem.
- If the user has still not answered correctly after three tries,
the program should output the correct answer.
- The program should ultimately output the user’s score:
    the number of correct answers out of 10.
- Structure your program as follows,
    wherein get_level prompts (and, if need be, re-prompts)
    the user for a level and returns 1, 2, or 3, and
    generate_integer returns a randomly generated non-negative integer
    with level digits or raises a ValueError if level is not 1, 2, or 3:
"""

import random


def main():
    level = get_level()
    score = 0
    for _ in range(10):
        x, y = generate_integer(level)
        problem = f"{x} + {y} = "
        correct_answer = x + y
        attempts = 0
        while attempts < 3:
            user_answer = input(problem)
            try:
                user_answer = int(user_answer)
                if user_answer == correct_answer:
                    score += 1
                    break
                else:
                    print("EEE")
                    attempts += 1
            except ValueError:
                print("EEE")
                attempts += 1

        else:
            print(f"{problem} {correct_answer}")
    print(f"Score: {score}")


def get_level():
    while True:
        level = input("Level: ")
        if level in ['1', '2', '3']:
            return int(level)


def generate_integer(level):
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
    elif level == 3:
        x = random.randint(100, 999)
        y = random.randint(100, 999)

    return x, y


if __name__ == "__main__":
    main()
