"""Greatest Common Divisor game."""

import random
import math


def generate_question():
    """Generate two random numbers."""
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    return f"{num1} {num2}"


def get_correct_answer(question):
    """Calculate GCD of two numbers."""
    num1, num2 = map(int, question.split())
    return math.gcd(num1, num2)


def main():
    """Main function for GCD game."""
    from VD_games.engine import game_engine
    description = "Find the greatest common divisor of given numbers."
    import sys
    current_module = sys.modules[__name__]
    game_engine.run_game(current_module, description)


if __name__ == "__main__":
    main()
