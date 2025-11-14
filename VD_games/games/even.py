"""Even number game."""

import random


def generate_question():
    """Generate a random number."""
    return str(random.randint(1, 100))


def get_correct_answer(question):
    """Check if number is even."""
    number = int(question)
    return "yes" if number % 2 == 0 else "no"


def main():
    """Main function for even number game."""
    from VD_games.engine import game_engine
    description = 'Answer "yes" if the number is even, otherwise answer "no".'
    import sys
    current_module = sys.modules[__name__]
    game_engine.run_game(current_module, description)


if __name__ == "__main__":
    main()
