"""Calculator game."""

import random
import operator


def generate_question():
    """Generate a random math expression."""
    operations = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul
    }
    
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    operation = random.choice(list(operations.keys()))
    
    return f"{num1} {operation} {num2}"


def get_correct_answer(question):
    """Calculate the correct answer for the math expression."""
    num1, op, num2 = question.split()
    num1 = int(num1)
    num2 = int(num2)
    
    operations = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul
    }
    
    return operations[op](num1, num2)


def main():
    """Main function for calculator game."""
    from VD_games.engine import game_engine
    description = "What is the result of the expression?"
    import sys
    current_module = sys.modules[__name__]
    game_engine.run_game(current_module, description)


if __name__ == "__main__":
    main()
