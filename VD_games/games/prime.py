"""Prime number game."""

import random


def is_prime(number):
    """Check if number is prime."""
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


def generate_question():
    """Generate a random number."""
    return str(random.randint(1, 100))


def get_correct_answer(question):
    """Check if number is prime."""
    number = int(question)
    return "yes" if is_prime(number) else "no"


def main():
    """Main function for prime game."""
    from VD_games.engine import game_engine

    description = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    game_engine.run_game(generate_question, get_correct_answer, description)


if __name__ == "__main__":
    main()
