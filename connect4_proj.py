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
    
    def move_along_board(self):
        #x = int(input("Enter x value: "))
        #y = int(input("Enter y value: "))
        return (int(input("Enter x value: ")), int(input("Enter y value: ")))
    
#some testing object initiation 

#player1 = Player("koffi", 'human')
#player2 = Player("omaue", 'human')

#print(player1, "\n", player2)


#will have to reorder all this



#Test move_along_board method
#move1 = player1.move_along_board()


## test Game implementation


#gameplay_tracker.append(move1)
#print (gameplay_tracker)



## loop trial 
# I) board constraints 6 x 7 (m x n )
   ## no -x or - y if origin is (0,0)
   ## x cannot be greater than 7 
   ## y cannot be greater than 6


# II) tracking moves of game and players
gameplay_tracker = []
player_1_tracker = []
player_2_tracker = []

# III) define win functions

def win_check_vertical(a_list, i, j):
    '''
    Summary: the function is given a player list and 
    it checks if the list has the following
    horizontal win within constraints
    vertical win within constraints
    diagonal win within constraints
    
    [(i, j), (i, j), (i, j), (i, j), ...] --> list
    (i, j)  sub element
    if 

    '''
    win = False
    for element in a_list:
            # becomes a matter of indexing
            if a_list[0] == (i, j) and a_list[1] == (i, j+1) and a_list[2] == (i, j+2) and a_list[3] ==(i, j+3):
                win = True
    return win

def win_check_horizontal(a_list, i, j):
    win = False
    for element in a_list:
            # becomes a matter of indexing
            if a_list[0] == (i, j) and a_list[1] == (i+1, j) and a_list[2] == (i+2, j) and a_list[3] ==(i+3, j):
                win = True
    return win



def win_check_diagonal1(a_list, i, j):
    win = False
    for element in a_list:
            # becomes a matter of indexing
            if a_list[0] == (i, j) and a_list[1] == (i+1, j+1) and a_list[2] == (i+2, j+2) and a_list[3] ==(i+3, j+3):
                win = True
    return win

def win_check_diagonal2(a_list, i, j):
    win = False
    for element in a_list:
            # becomes a matter of indexing
            if a_list[0] == (i+3, j+3) and a_list[1] == (i+2, j+2) and a_list[2] == (i+1, j+1) and a_list[3] ==(i, j):
                win = True
    return win

#################################################3

#IV) Start game code

print("Welcome to game")

player1 = Player("koffi", 'human')
player2 = Player("omaue", 'human')

game_counter = 0

while game_counter < 42:        #42 because 6 * 7
    
    #first player makes move
    print("player1 make your move")
    move1 = player1.move_along_board()
    #Board Constraints
    for element in move1:
        if move1[0] < 0 or move1[1] < 0:
            print("Cannot enter negative coordinates: ")
            move1 = player1.move_along_board()
        if move1[0] > 7 or move1[1] > 6:
            print("Cannot exceed constraints of board: ")
            move1 = player1.move_along_board()
    #Gameplay Constraints
    if move1 in gameplay_tracker:
        print("can't put pick there, already occupied")
        #replay
        move1 = player1.move_along_board()
    #enter the move in the game_play tracker and player 1 tracker
    ##if the constraints don't apply
    gameplay_tracker.append(move1)
    player_1_tracker.append(move1)
    
    
    
    #increase the game counter
    game_counter += 1
    
    
    
    #second player makes move
    print("player2 make your move")
    move2 = player2.move_along_board()
    #Board constraints
    for element in move2:
        if move2[0] < 0 or move2[1] < 0:
            print("Cannot enter negative coordinates: ")
            move2 = player2.move_along_board()
        if move2[0] > 7 or move2[1] > 6:
            print("Cannot exceed constraints of board: ")
            move2 = player2.move_along_board()
    #Gameplay constraints
    if move2 in gameplay_tracker:
        print("can't put pick there, already occupied")
        #replay
        move2 = player2.move_along_board()
    #enter the move in the game_play tracker and player 1 tracker
    ##if the constraints don't apply
    gameplay_tracker.append(move2)
    player_2_tracker.append(move2)
    
    
    #check for win for players
    #check for win for player 1
    if game_counter > 14:
        win_check_vertical(player_1_tracker, move1[0], move1[1])
        win_check_horizontal(player_1_tracker,move1[0], move1[1])
        win_check_diagonal1(player_1_tracker,move1[0], move1[1])
        win_check_diagonal2(player_1_tracker,move1[0], move1[1])
        win_check_vertical(player_2_tracker, move2[0], move2[1])
        win_check_horizontal(player_2_tracker, move2[0], move2[1])
        win_check_diagonal1(player_2_tracker,move2[0], move2[1])
        win_check_diagonal2(player_2_tracker, move2[0], move2[1])
   
    get_out = int(input("Enter 99 to exit game: "))
    if get_out == 99:
        break