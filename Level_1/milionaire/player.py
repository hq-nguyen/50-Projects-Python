class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.current_question = None

    def increment_score(self):
        self.score += 1

    def reset_score(self):
        self.score = 0
