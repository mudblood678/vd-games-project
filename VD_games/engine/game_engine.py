"""Game engine for all VD games."""

import prompt


def run_game(generate_func, answer_func, description):
    """
    Run a game with common logic.

    Args:
        generate_func: Function that generates questions
        answer_func: Function that calculates correct answers
        description: Game description for the user
    """
    print("Welcome to the VD Games!")

    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")

    print(description)

    correct_answers_needed = 3
    correct_answers_count = 0

    while correct_answers_count < correct_answers_needed:
        question = generate_func()
        print(f"Question: {question}")

        user_answer = prompt.string("Your answer: ")
        correct_answer = str(answer_func(question))

        if user_answer == correct_answer:
            print("Correct!")
            correct_answers_count += 1
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")
