import numpy as np #Importing numpy as np to make the code easier to read and understand.#
import math
import pygame #Importing pygame for graphics.#
import sys #Importing sys to work with pygame.#

#Variables#
yellow = (255,255,0)
black = (0,0,0)
cyan = (0,255,255)
purple = (127,255,0)

number_of_rows = 6
number_of_columns = 7

#Functions#
def game_board(): #Game board function defined.#
    play_board = np.zeros((number_of_rows,number_of_columns)) #Create a 6 by 7 matrix of zeros as an empty board.#
    return play_board #Return this as play_board.#


def piece_drop(play_board, row, column, piece): #Player's piece being put into the board.#
    play_board[row][column] = piece #Setting up the matrix.#


def column_check(play_board, column): #This will check if the number input by each player is a plausible column.#
    return [number_of_rows - 1][column] == 0 #Checks if the selected column of the fifth row (the top row) has any number other than 0. If the column is 0, then the player can put their piece in that column. If the column is not 0, then that slot has already been filled, and the player cannot go there.#


def row_check(): #This will determine which row the player's piece will fall to.#
    for row in range(number_of_rows): 
        if play_board[row][column] == 0: #This is similar to the column-check function. If the slot in the row equals 0, then the slot is open#
            return row
    
def change_board(play_board): #Flips the board so that the pieces will go to the bottom row, rather than the top of the row. This will make the game actually look more like the authentic connect four game.#
    print(np.flip(play_board, 0))#Use numpy to flip the matrix over the x-axis.#

def win_check(play_board, piece): #This function is going to check the possible ways of winning in the game.#

 #Checking for a horizontal win#
    for col in range(number_of_columns - 3 ): #Loop iterating through the columns. We subtract 3 because a horizontal win cannot start at the fifth column, it can only start from columns 0 to 4.#
        for row in range(number_of_rows): #Loop through the rows. All the rows can work for a win.#
            if play_board[row][col] == piece and play_board[row][col + 1] == piece and play_board[row][col + 2] == piece  and play_board[row][col + 3] == piece: #We add 1 each time to check the next column to the right.#
                return True 

#Checking for vertical win#
    for col in range(number_of_columns): #Loop iterating through the columns. ALl the columns can work for a win.#
        for row in range(number_of_rows - 3): #Loop through the rows. We subtract 3 because a vertical win cannot start at the top row.#
            if play_board[row][col] == piece and play_board[row + 1][col] == piece and play_board[row + 2][col] == piece  and play_board[row + 3][col] == piece: #We add 1 each time to check the next row.#
                return True  

#Checking for positve-sloped diagonal win#
    for col in range(number_of_columns - 3): #Loop iterating through the columns.#
        for row in range(number_of_rows - 3): #Loop through the rows.#
            if play_board[row][col] == piece and play_board[row + 1][col + 1] == piece and play_board[row + 2][col + 2] == piece  and play_board[row + 3][col + 3] == piece: #We add 1 each time to check for each diagonal in the positive direction.#
                return True

#Checking for negatively-sloped diagonal win#
    for col in range(number_of_columns - 3): #Loop iterating through the columns.#
        for row in range(3, number_of_rows - 3): #Loop through the rows starting at row 3 because the diagonal cannot begin (fit) below row 3.#
            if play_board[row][col] == piece and play_board[row - 1][col + 1] == piece and play_board[row - 2][col + 2] == piece  and play_board[row - 3][col + 3] == piece: #We add 1 each time for the columns, but we subtract 1 each time for the rows because we are moving diagonally in the negative direction.#
                return True

def show_board(play_board): #Drawing the game board graphic.#
    for col in range(number_of_columns):
        for row in range(number_of_rows):
            pygame.draw.rect(screen, yellow, (col*square_pixels, row*square_pixels+square_pixels, square_pixels, square_pixels), ) #The screen is the surface. The yellow is the predefined yellow (255,255, 0). We multiply rows times the size of the square (and add the size in order to create the top row where the piece will be), the columns times the size of the square, establish the height and width, to create the rectangle. #
            pygame.draw.circle(screen, black, (int(col*square_pixels + square_pixels/2), int(row*square_pixels+square_pixels/2)), rad)

    for col in range(number_of_columns):
        for row in range(number_of_rows):
            if play_board[row][col] == 1: #Player 1 piece color.#
                pygame.draw.circle(screen, cyan, (int(col*square_pixels + square_pixels/2), screen_length - int(row*square_pixels + square_pixels/2)), rad)
            elif play_board[row][col] == 2: #Player 2 piece color.#
                pygame.draw.circle(screen, purple, (int(col*square_pixels + square_pixels/2), screen_length - int(row*square_pixels + square_pixels/2)), rad)
    pygame.display.update()

play_board = game_board() #Initalize the game board, which is currently a zeros matrix.#
print(play_board) #Displays the game board so that the players can see it.#
game_done = False #Initialize the game_done variable as false. This will change to true when a player wins.#
player_turn = 0 #Intialize the player's turn, which will be useful in separating each turn for player 1 and player 2.#

pygame.init() #Initialize pygame.#

square_pixels = 100 #Setting the board to be 100 pixels.#
screen_width = number_of_columns * square_pixels #Setting the horizontal screen size for the game.#
screen_length = (number_of_rows + 1) * square_pixels #Setting the vertical screen size for the game. Add 1 to the number of rows so that we can show the game piece above the game board. This is just for visual purposes.#
size = (screen_width,screen_length)

rad = int(square_pixels/2 - 5)

screen = pygame.display.set_mode(size) #Function within pygame that shows the board/game.#
show_board(play_board)
pygame.display.update()

myfont = pygame.font.SysFont("Helvetica", 60) #Helvetica is the font, and it is size 60.#

while not game_done: #Loop is going to run when the game_done variable is false. When a player wins the game (by getting four in a row) the game_done variable will be true.#
    for event in pygame.event.get(): #Events are actions, such as clicking and mouse motions, that are part of the game.#
        if event.type == pygame.QUIT:
            sys.exit() #Allows game to properlyquit when the x button in the corner of the screen is hit.#

        if event.type == pygame.MOUSEMOTION: #Makes the players able to see their piece before dropping it into the slot. For visual effect.#
            pygame.draw.rect(screen, black, (0,0,screen_width, square_pixels)) #This will draw a rectangle so that there is just one piece being shown.#
            posx = event.pos[0]
            if player_turn == 0: #Player 1's turn.#
                pygame.draw.circle(screen, cyan, (posx, int(square_pixels/2)), rad)
            else: #Player 2's turn.#
                pygame.draw.circle(screen, purple, (posx, int(square_pixels/2)), rad)
            pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN: #When you click down on the screen, the piece will drop.#
            pygame.draw.rect(screen, black, (0,0,screen_width, square_pixels))
            if player_turn == 0:
                posx = event.pos[0] #The position of x is the 0 element.#
                column = int(math.floor(posx/100)) #We divide the position by 100 to simplift it (this way its not something like 600). The floor command is a built in math command.#

        #Player 1 Turn#
            if player_turn == 0: #If the player_turn variable equals 0, then the game will ask for player 1 to go.#
                column = int(input('Player One, it is your turn! Choose a number from 0 to 6.')) #Since the player_turn variable equals 0, the game will display this message so that player 1 knows to go. The player will type a number from 0-6 as the column of their move. The int makes sure the command is an integer.#

                if column_check(play_board, column):
                    next_row = row_check(play_board, column) #Getting the next available row.#
                    piece_drop(play_board, next_row, column, 1) #Putting player 1's piece in their desired slot. Their piece will show up as the number 1.#

                    if win_check(play_board, 1): #Function to check if player 1 wins.#
                        label = myfont.render("Player One, you win!",1, cyan) #The text that will be displayed when player one wins.#
                        screen.blit(label, (40,10)) #The location where the font will be displayed.#
                        game_done = True #Game will be over.#


        # #Player 2 Turn#
            else:
                column = int(input('Player Two, it is your turn! Choose a number from 0 to 6.')) #Same thing as above, but with player two's turn.#
                posx = event.pos[0] #The position of x is the 0 element.#
                column = int(math.floor(posx/100)) #We divide the position by 100 to simplift it (this way its not something like 600). The floor command is a built in math command.#

                if column_check(play_board, column):
                     next_row = row_check(play_board, column) #Getting the next available row.#
                     piece_drop(play_board, next_row, column, 2) #Putting player 2's piece in their desired slot. Their piece will show up as the number 2.#
                    
                if win_check(play_board, 2): #Function to check if player 2 wins.#
                        label = myfont.render("Player Two, you win!",1, purple) #Displays winning message to player 2 if they win.#
                        screen.blit(label, (40,10))
                        game_done = True #Game will be over.#

            change_board(play_board) #Calls the change_board function, so that we can see the game board after the players have taken their turns.#
            show_board(play_board)

            player_turn = player_turn + 1 #Adds to the turn each time.#
            player_turn = player_turn % 2 #Divides the value of turn by two, which makes it possible to alternate the turns between the two players.#

            if game_done:
                pygame.time.wait(5000) #Waits 5000 milliseconds after win.#
    