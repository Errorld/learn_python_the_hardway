#!/usr/bin/env python
#!coding:utf-8
from random import randint, uniform

class fighter(object):
    def __init__(self, name):
        self.name = name
        self.atk = randint(1,10)
        self.maxHp = randint(1,100)
        self.curHp = self.maxHp
        self.luck = 1
    def describe(self):
        return 'My name is %s.\nMy attack is %d.\nMy max hp is %d\nNow I have %d hp' % (self.name, self.atk, self.maxHp, self.curHp)
    def attack(self, enemy):
        if not self.die():
            enemy.curHp -= (self.atk+(self.atk*(self.luck+uniform(-2,2)))*0.1)
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
                    4.Status
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
                    continue
                elif result == 'lose':
                    print "you lost"
                    continue
                elif result == 'flee':
                    print "you ran away, coward"
                    continue
            if choice == '2':
                print 'You found nothing'
            if choice == '3':
                player.curHp = player.maxHp
            if choice == '4':
                print player.describe()
                
                    
    pass

def create_player():
    name = raw_input('tell me your name\n')
    return fighter(name)

def create_enemy():
    return fighter("enemy")

def battle(player, enemy):
    while True:
        print """
        choose your action:
            1.attack
            2.flee
        """
        choice = raw_input('> ')
        if choice not in ['1', '2']:
            continue
        if choice == '1':
            player.attack(enemy)
            print player.describe()
        if choice == '2':
            return 'flee'
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



