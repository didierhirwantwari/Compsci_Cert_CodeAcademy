# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

Project connect 4 compsci certificate
"""

class Player: 
    '''
    To create a player, give them a name, a type
    (human or computer), and give them a score. A
    starting match is going to be zero for 
    each game and it increases as the game goes
    one. A match of 4 implies a connect  of 4 
    which implies a win.  
    '''
    def __init__(self, name, type, match = 0):
        self.name = name
        self.type = type
        self.match = match
        
    
    def __repr__(self):
        '''
        Printing a player, will tell you their name
        their type and their match
        
        
        '''
        return "Player {name} has {match} inline matches\n. \
               They are a {type} Player".format(name = self.name, 
                   type = self.type, match = self.match)
    
    def move_along_board(self, x, y):
        x = int(input("Enter x value: "))
        y = int(input("Enter y value: "))
        return (x, y)
    
#some testing 
player1 = Player("koffi", 'human')
player2 = Player("omaue", 'human')



player1
player2

       