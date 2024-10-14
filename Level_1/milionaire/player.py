class Player:
    def __init__(self, name):
        self.name = name
        self.money = 0

    def add_money(self, amount):
        self.money += amount

    def get_money(self):
        return self.money