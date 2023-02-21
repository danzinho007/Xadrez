class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.hp = 100
        self.max_hp = 100
        self.attack = 10
        self.defense = 5
        
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
