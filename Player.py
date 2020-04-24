class Player:

    health = 0
    dead = False
    food = 0
    name = ""

    def __init__(self, health, name, food):
        self.health = health
        self.name = name
        self.food = food

    def getHealth(self):
        return self.health
    def isDead(self):
        return self.dead
    def getFood(self):
        return self.food
    def getName(self):
        return self.name
