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

        self.end_game()

    def ask_question(self, question):
        print(f"Round {self.round}: {question.question}")
        for idx, option in enumerate(question.options):
            print(f"{idx + 1}. {option}")
        answer = input("Your choice (1-4): ").strip()

        if question.options[int(answer) - 1] == question.correct_answer:
            print("Correct!")
            self.player.increment_score()
        else:
            print("Incorrect!")
            print(f"Explanation: {question.explanation}")
            self.end_game()

    def prompt_next(self):
        choice = input("Do you want to continue? (y/n): ").lower()
        return choice == 'y'

    def end_game(self):
        print(f"Game Over! Your final score: {self.player.score}")
        exit()
