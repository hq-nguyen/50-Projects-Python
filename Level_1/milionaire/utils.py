import time

def format_question(question, options):
    """Formats and prints the question and its options."""
    print(f"Question: {question}")
    for idx, option in enumerate(options):
        print(f"{idx + 1}. {option}")

def get_valid_input(prompt, valid_options):
    """
    Ensures that the player's input is one of the valid options.
    If the input is invalid, it prompts the player again.
    """
    while True:
        choice = input(prompt).strip()
        if choice in valid_options:
            return choice
        else:
            print(f"Invalid choice. Please choose from {', '.join(valid_options)}.")

def measure_time_to_answer():
    """Measures how long the player takes to answer the question."""
    start_time = time.time()
    input("Press Enter to submit your answer: ")
    elapsed_time = time.time() - start_time
    return elapsed_time

def display_correct_answer_feedback():
    """Displays feedback for a correct answer."""
    print("Correct! Well done.")

def display_incorrect_answer_feedback(explanation):
    """Displays feedback for an incorrect answer and shows an explanation."""
    print("Incorrect.")
    print(f"Explanation: {explanation}")

def end_game_message(player):
    """Displays the final score and ends the game."""
    print(f"Game Over! {player.name}, your final score is: {player.score}")
