from player import Player
from game import Game
from question import QuestionManager

def main():
    player_name = input("Enter your name: ")
    player = Player(player_name)
    question_manager = QuestionManager('./Level_1/milionaire/questions.txt')
    
    game = Game(player, question_manager)
    game.play()

if __name__ == "__main__":
    main()
