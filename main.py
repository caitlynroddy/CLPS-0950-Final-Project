import numpy as np #Importing numpy as np to make the code easier to read and understand.#

def game_board(): #Game board function defined.#
    empty_board = np.zeros((6,7)) #Create a 6 by 7 matrix of zeros as an empty board.#
    return empty_board #Return this as empty_board.#

empty_board = game_board() #Initalize the game board, which is currently a zeros matrix#
game_done = False #Initialize the game_done variable as false. This will change to true when a player wins.#
player_turn = 0 #Intialize the player's turn, which will be useful in separating each turn for player 1 and player 2.#

while not game_done: #Loop is going to run when the game_done variable is false. When a player wins the game (by getting four in a row) the game_done variable will be true.#
    
 #Player 1 Turn#
    if player_turn == 0: #If the player_turn variable equals 0, then the game will ask for player 1 to go.#
        turn = int(input('Player One, it is your turn! Choose a number from 1 to 6.')) #Since the player_turn variable equals 0, the game will display this message so that player 1 knows to go. The player will type a number from 1-6 as their move. The int makes sure the command is an integer.#
    else:
        turn = int(input('Player Two, it is your turn! Choose a number from 1 to 6.')) #Same thing as above, but with player two's turn.#
    
    turn = turn + 1
    turn = turn % 2 #Divides the value of turn by two, which makes it possible to alternate the turns between the two players.#

    