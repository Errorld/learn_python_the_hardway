from random import randint
class Fighter(object):
    def __init__(self, name):
        self.name = name
        self.atk = randint(1,10)
        self.maxHp = randint(1,100)
        self.curHp = self.maxHp
        self.luck = 1
    pass

class Engine(object):
    def play(self):
        
        player = Fighter(name)
        pass
        
    pass
