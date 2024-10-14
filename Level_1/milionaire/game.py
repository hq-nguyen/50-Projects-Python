import random
from question import QuestionManager
from player import Player

class Game:
    def __init__(self, question_file):
        self.player = Player()
        self.question_manager = QuestionManager(question_file)
        self.prize_money = [100, 200, 300, 500, 1000, 2000, 4000, 8000, 16000, 32000, 64000, 125000, 250000, 500000, 1000000]
        self.milestones = [1000, 32000]
        self.current_question = 0
        self.game_over = False

    def ask_question(self, question):
        print(f"Question {self.current_question + 1}: {question.question}")
        for i, option in enumerate(question.options):
            print(f"{i+1}. {option}")
        
        try:
            answer = int(input("Enter the number of your answer: ")) - 1
            if question.options[answer] == question.correct_answer:
                self.player_money()
            else:
                self.incorrect_answer()
        except (ValueError, IndexError):
            print("Invalid answer. Please choose a valid option.")
            self.incorrect_answer()

    def player_money(self):
        """Handles the player getting a correct answer."""
        prize = self.prize_money[self.current_question]
        print(f"Correct! You've won ${prize}!")
        self.player.add_money(prize)
        self.current_question += 1

        if self.current_question < len(self.prize_money):
            print(f"You're now playing for ${self.prize_money[self.current_question]}.\n")
        else:
            print("Congratulations! You've won $1,000,000!")
            self.game_over = True

    def incorrect_answer(self):
        """Handles the player getting an incorrect answer."""
        if self.current_question == 0:
            print("Sorry, that's incorrect. You leave with $0.")
        else:
            # Player falls back to last milestone they've reached
            last_milestone = max([m for m in self.milestones if self.player.money >= m], default=0)
            print(f"Sorry, that's incorrect. You leave with ${last_milestone}.")
        self.game_over = True

    def play(self):
        """Main game loop."""
        while not self.game_over:
            question = self.question_manager.get_random_question()
            self.ask_question(question)

# Example of running the game
if __name__ == '__main__':
    game = Game('questions.txt')
    game.play()
