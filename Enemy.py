class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.hp = 50
        self.max_hp = 50
        self.attack = 8
        self.defense = 3
        
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
