import numpy as np #Importing numpy as np to make the code easier to read and understand.#

number_of_rows = 6
number_of_columns = 7

def game_board(): #Game board function defined.#
    play_board = np.zeros((6,7)) #Create a 6 by 7 matrix of zeros as an empty board.#
    return play_board #Return this as play_board.#


def piece_drop(play_board, row, column, piece): #Player's piece being put into the board.#
    play_board[row][column] == piece


def column_check(play_board, column): #This will check if the number input by each player is a plausible column.#
    return [5][column] == 0 #Checks if the selected column of the fifth row (the top row) has any number other than 0. If the column is 0, then the player can put their piece in that column. If the column is not 0, then that slot has already been filled, and the player cannot go there.#


def row_check(): #This will determine which row the player's piece will fall to.#
    for row in range(number_of_rows): 
        if play_board[row][column] == 0: #This is similar to the column-check function. If the slot in the row equals 0, then the slot is open#
            return row
    

play_board = game_board() #Initalize the game board, which is currently a zeros matrix#
game_done = False #Initialize the game_done variable as false. This will change to true when a player wins.#
player_turn = 0 #Intialize the player's turn, which will be useful in separating each turn for player 1 and player 2.#


while not game_done: #Loop is going to run when the game_done variable is false. When a player wins the game (by getting four in a row) the game_done variable will be true.#
    
 #Player 1 Turn#
    if player_turn == 0: #If the player_turn variable equals 0, then the game will ask for player 1 to go.#
        column = int(input('Player One, it is your turn! Choose a number from 0 to 6.')) #Since the player_turn variable equals 0, the game will display this message so that player 1 knows to go. The player will type a number from 0-6 as the column of their move. The int makes sure the command is an integer.#

#Player 2 Turn#
    else:
        column = int(input('Player Two, it is your turn! Choose a number from 0 to 6.')) #Same thing as above, but with player two's turn.#
    
    turn = turn + 1
    turn = turn % 2 #Divides the value of turn by two, which makes it possible to alternate the turns between the two players.#

    