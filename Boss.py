class Boss:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.hp = 200
        self.max_hp = 200
        self.attack = 20
        self.defense = 10
        
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
