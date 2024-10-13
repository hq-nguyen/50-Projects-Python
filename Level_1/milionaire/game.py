from utils import format_question, get_valid_input, display_correct_answer_feedback, display_incorrect_answer_feedback, end_game_message

class Game:
    def __init__(self, player, question_manager):
        self.player = player
        self.question_manager = question_manager
        self.round = 1

    def start(self):
        print(f"Welcome {self.player.name} to 'Who Wants to be a Millionaire!'")
        while self.round <= 15:
            question = self.question_manager.get_random_question()
            self.ask_question(question)

            if not self.prompt_next():
                break

            self.round += 1

        end_game_message(self.player)

    def ask_question(self, question):
        format_question(question.question, question.options)
        answer = get_valid_input("Your choice (1-4): ", ['1', '2', '3', '4'])

        if question.options[int(answer) - 1] == question.correct_answer:
            display_correct_answer_feedback()
            self.player.increment_score()
        else:
            display_incorrect_answer_feedback(question.explanation)
            end_game_message(self.player)
            exit()

    def prompt_next(self):
        choice = get_valid_input("Do you want to continue? (y/n): ", ['y', 'n'])
        return choice == 'y'
