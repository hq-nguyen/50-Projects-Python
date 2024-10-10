# Program: Rock Paper Scissor
class Participant:
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.choice = ""
    def choose(self):
        while True:
            try:
                self.choice=input(f"{self.name} choose paper, rock or scissor? ").strip().lower()
                if self.choice in ["rock", "paper", "scissor", "r", "p", "s"]:
                    print(f"{self.name} selects {self.choice}")
                    break
                else:
                    print("Invalid input. Please type 'rock', 'paper' or 'scissor'.")
            except ValueError as e:
                print(e)
                

    # Convert choice to numerical value
    def toNumericalChoice(self):
        switcher = {
            "r": 0,
            "p": 1,     
            "s": 2,
            "rock": 0,
            "paper": 1,
            "scissor": 2
        }
        return switcher[self.choice]

    def incrementPoint(self):
        self.points += 1

class GameRound:
    def __init__(self, p1, p2):
        self.rules = [
            [0, -1, 1],
            [1, 0, -1],
            [-1, 1, 0]
        ]

        p1.choose()
        p2.choose()
        result = self.compareChoices(p1,p2)
        print("Round resulted in a {result}".format(result = self.getResultAsString(result) ))

        if result > 0:
           p1.incrementPoint()
        elif result < 0:
           p2.incrementPoint()

    def compareChooses(self):
        print("imp")
    def awardPoints(self):
        print("imp")

    def compareChoices(self, p1, p2):
        return self.rules[p1.toNumericalChoice()][p2.toNumericalChoice()]

    def getResultAsString(self, result):
        res = {
            0: "draw",
            1: "win",
            -1: "loss"
        }
        return res[result]



class Game:
    def __init__(self):
        self.endGame=False
        self.participant = Participant("Ivan")
        self.second_participant=Participant("Harry")

    def start(self):
        while not self.endGame:
            GameRound(self.participant, self.second_participant)
            self.checkEndCondition()

    def checkEndCondition(self):
        answer = input("Continue game y/n: ")
        if answer == 'y':
            GameRound(self.participant, self.second_participant)
            self.checkEndCondition()
        else:
            print("Game ended, {p1name} has {p1points}, and {p2name} has {p2points}".format(p1name = self.participant.name, p1points= self.participant.points, p2name=self.second_participant.name, p2points=self.second_participant.points))
            self.determineWinner()
            self.endGame = True

    def determineWinner(self):
        resultString = "It's a Draw"
        if self.participant.points > self.second_participant.points:
            resultString = "Winner is {name}".format(name=self.participant.name)
        elif self.participant.points < self.second_participant.points:
            resultString = "Winner is {name}".format(name=self.second_participant.name)
        print(resultString)

game = Game()
game.start()
