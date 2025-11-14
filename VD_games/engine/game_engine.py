"""Game engine for all VD games."""

import prompt
import importlib


def run_game(game_module, description):
    """
    Run a game with common logic.
    
    Args:
        game_module: Module containing generate_question and get_correct_answer
        description: Game description for the user
    """
    print("Welcome to the VD Games!")
    
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    
    print(description)
    
    correct_answers_needed = 3
    correct_answers_count = 0
    
    while correct_answers_count < correct_answers_needed:
        question = game_module.generate_question()
        print(f"Question: {question}")
        
        user_answer = prompt.string("Your answer: ")
        correct_answer = str(game_module.get_correct_answer(question))
        
        if user_answer == correct_answer:
            print("Correct!")
            correct_answers_count += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    
    print(f"Congratulations, {name}!")
