"""Arithmetic progression game."""

import random


def generate_question():
    """Generate arithmetic progression with hidden element."""
    start = random.randint(1, 20)
    step = random.randint(1, 10)
    length = random.randint(5, 10)

    # Generate progression
    progression = []
    for i in range(length):
        progression.append(str(start + i * step))

    # Hide random element
    hidden_index = random.randint(0, length - 1)
    correct_answer = progression[hidden_index]
    progression[hidden_index] = ".."

    return " ".join(progression)


def get_correct_answer(question):
    """Calculate hidden number in progression."""
    numbers = question.split()

    # Find the position of hidden element
    hidden_index = numbers.index("..")

    if hidden_index == 0:
        # First element is hidden
        step = int(numbers[2]) - int(numbers[1])
        return int(numbers[1]) - step
    elif hidden_index == len(numbers) - 1:
        # Last element is hidden
        step = int(numbers[1]) - int(numbers[0])
        return int(numbers[hidden_index - 1]) + step
    else:
        # Middle element is hidden
        if hidden_index == 1:
            step = int(numbers[3]) - int(numbers[2])
        else:
            step = int(numbers[hidden_index + 1]) - int(numbers[hidden_index - 1]) // 2
        return int(numbers[hidden_index - 1]) + step


def main():
    """Main function for progression game."""
    from VD_games.engine import game_engine

    description = "What number is missing in the progression?"
    game_engine.run_game(generate_question, get_correct_answer, description)


if __name__ == "__main__":
    main()
