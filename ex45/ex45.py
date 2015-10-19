#!/usr/bin/env python
#!coding:utf-8
from random import randint

class fighter(object):
    def __init__(self, name):
        self.name = name
        self.atk = randint(1,10)
        self.maxHp = randint(1,100)
        self.curHp = self.maxHp
    def describe(self):
        return 'My name is %s.\nMy attack is %d.\nMy max hp is %d\nNow I have %d hp' % (self.name, self.atk, self.maxHp, self.curHp)
    def attack(self, enemy):
        if not self.die():
            enemy.curHp -= self.atk
    def die(self):
        if self.curHp <= 0:
            print "%s died." % self.name
            return True
    pass

class engine(object):
    def start(self):
        player = create_player()
        print player.describe()
        while True:
            print """
                Choose your action:
                    1.Search for enemies
                    2.Look for items
                    3.Have a rest
                    4.Do nothing
                """
            choice = raw_input("> ")
            if choice not in ['1','2','3','4']:
                print "Wrong input, try again"
                continue
            
            if choice == '1':
                enemy = create_enemy()
                print enemy.describe()
                result = battle(player, enemy)
                if result == 'win':
                    print "you won"
                    break
                elif result == 'lose':
                    print "you lost"
                    break
                
                    
    pass

def create_player():
    name = raw_input('tell me your name\n')
    return fighter(name)

def create_enemy():
    return fighter("enemy")

def battle(player, enemy):
    while True:
        player.attack(enemy)
        print player.describe()
        enemy.attack(player)
        print enemy.describe()
        raw_input()
        if enemy.die():
            return 'win'
        if player.die():
            return 'lose'
    pass
    

if __name__ == '__main__':
    mainEngine = engine()    
    mainEngine.start()



