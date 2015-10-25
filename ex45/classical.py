#!/usr/bin/env python
#!coding:utf-8
from random import randint, uniform
from sys import exit

class Fighter(object):
    def __init__(self, name):
        self.name = name
        self.atk = randint(1,10)
        self.maxHp = randint(1,100)
        self.curHp = self.maxHp
        self.luck = 1
        self.gold = self.maxHp +self.atk
    def describe(self):
        return 'My name is %s.\nMy attack is %d.\nMy max hp is %d\nNow I have %d hp' \
        % (self.name, self.atk, self.maxHp, self.curHp)
    def attack(self, enemy):
        if not self.is_dead():
            value = (self.atk+(self.atk*(self.luck+uniform(-2,2)))*0.1)
            enemy.change_hp(-value)
            return '%s attacked %s, %dhp reduced. %dhp remains' % (self.name, enemy.name, value, enemy.curHp)
    def change_hp(self, value):
        self.curHp += value
        if self.curHp>self.maxHp:
            self.curHp = self.maxHp
        if self.is_dead():  #detect death
            return 'died'
    def is_dead(self):
        if self.curHp <= 0:
            print "%s died." % self.name
            return True

    def hack(self):
        self.atk = 10
        self.maxHp = 100
        print 'maxiumed your attr'

class Scene(object):
    def enter(self, player):
        print 'not yet'
        return 'game_over'

class Battle(Scene):
    def create_enemy(self):
        return Fighter('enemy')
    def battle(self, player, enemy):
        while True:
            print"""
            choose your action:
                1.attack
                2.flee
                3.skill
            """
            choice = raw_input('> ')
            if choice not in ['1', '2']:
                continue
            if choice == '1':
                if player.is_dead():
                    return 'lose'
                else:
                    print player.attack(enemy)
            elif choice == '2':
                return 'flee'
            if enemy.is_dead():
                return 'win'
            if player.is_dead():
                return 'lose'
            else:
                print enemy.attack(player)
            raw_input()

    def enter(self,player):
        enemy = self.create_enemy()
        print enemy.describe()
        result = self.battle(player, enemy)
        if result == 'win':
            print "you won"
        elif result == 'lose':
            print "you lost in a battle and you died"
            return 'geme_over'
        elif result == 'flee':
            print "you ran away, coward"
        return 'main_menu'

class Save(Scene):
    pass
class MainMenu(Scene):
    def show_menu(self,player):
        print 'Hello', player.name+':'
        print """
        Choose your action
        1.Search for enemies
        2.Look for items
        3.Have a rest
        4.Status
        5.Save
        0.Exit
        """
    def choose(self,player):

        choice = raw_input("> ")
        if choice not in ['1','2','3','4','5','0','hack']:
            print "Wrong input, try again"
            return 'main_menu' 
            
        if choice == '1':
            return 'battle'
        if choice == '2':
            return 'item'
        if choice == '3':
            return 'rest'
        if choice == '4':
            return 'status'
        if choice == '5':
            return 'save'
        if choice == '0':
            return 'exit'
        if choice == 'hack':
            player.hack()
            return 'main_menu'

    
    def enter(self, player):
        self.show_menu(player)
        return self.choose(player)

class Status(Scene):
    def enter(self, player):
        print player.describe()
        return 'main_menu'
    pass
class Item(Scene):
    pass
class Rest(Scene):
    def enter(self, player):
        player.curHp = player.maxHp
        print 'You had fully rested'
        return 'main_menu'
    pass
class Save(Scene):
    pass
class GameOver(Scene):
    def enter(self, player):
        print 'Game Over'
        return 'exit'       
class Exit(Scene):
    def enter(self, player):
        print 'See you'
        exit(0)
class Control(object):
    scene = {
        'battle':Battle(),
        'item':Item(),
        'main_menu':MainMenu(),
        'game_over':GameOver(),
        'status':Status(),
        'rest':Rest(),
        'save':Save(),
        'exit':Exit()
    }
    def __init__(self, start_scene):
        self.openning_scene = start_scene
    def next_scene(self, scene_name):
        return Control.scene.get(scene_name)
    def start_scene(self):
        return self.next_scene(self.openning_scene)

class Engine(object):
    def __init__(self, control):
        self.scene_control = control 
        self.player = create_player()
    def play(self):
        current_scene = self.scene_control.start_scene() 
        last_scene = self.scene_control.next_scene('exit')
        while current_scene != last_scene:
            next_scene = current_scene.enter(self.player)
            current_scene = self.scene_control.next_scene(next_scene)
        current_scene.enter(self.player)

        pass


def create_player():
    name = raw_input('tell me your name\n')
    return Fighter(name)

if __name__ == '__main__':
    control = Control('main_menu')
    mainEngine = Engine(control)    
    mainEngine.play()
