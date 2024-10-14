import random
from player import Player
from question import QuestionManager

class Game:

    def __init__(self, player,  question_file):
        self.player = player
        self.question_manager = question_file
        # Prize structure for each question
        self.prize_money = [100, 200, 300, 500, 1000, 2000, 4000, 8000, 16000, 32000, 64000, 125000, 250000, 500000, 1000000]
        # Milestones where players cannot lose their money once reached
        self.milestones = [1000, 32000]
        self.current_question_index = 0
        self.game_over = False

    def ask_question(self, question):
        """Asks the player a question and handles their response."""
        print(f"Question {self.current_question_index + 1}: {question.question}")
        for i, option in enumerate(question.options):
            print(f"{i+1}. {option}")

        # make sure the player enters a valid answer
        while True:
            try:
                answer = int(input("Enter the number of your answer: ")) - 1
                if answer in range(4):
                    if question.options[answer] == question.correct_answer:
                        self.correct_answer()
                        break
                    else:
                        self.incorrect_answer()
                        break
                else:
                    print("Please enter a valid option (1-4).")
            except (ValueError, IndexError):
                print("Invalid input! Please select a valid option.")
                continue

    def correct_answer(self):
        """Handles the player answering correctly."""
        prize = self.prize_money[self.current_question_index]
        print(f"Correct! You've won ${prize}!\n")
        self.player.add_money(prize)
        self.current_question_index += 1

        # Check if the player has won the game
        if self.current_question_index < len(self.prize_money):
            print(f"You're now playing for ${self.prize_money[self.current_question_index]}.\n")
        else:
            print("Congratulations! You've won $1,000,000!")
            self.game_over = True

    def incorrect_answer(self):
        """Handles the player answering incorrectly."""
        if self.current_question_index == 0:
            print("Sorry, you didn't win anything. You leave with $0.")
        else:
            # Player keeps their milestone prize
            last_milestone = max([m for m in self.milestones if self.player.get_money() >= m], default=0)
            print(f"Sorry, that's incorrect. You leave with ${last_milestone}.")
        self.game_over = True

    def play(self):
        """Main game loop."""
        print(f"Welcome {self.player.name} to 'Who Wants to be a Millionaire!'")

        while not self.game_over:
            question = self.question_manager.get_random_question()
            self.ask_question(question)