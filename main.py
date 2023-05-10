import numpy as np #Importing numpy as np to make the code easier to read and understand.#
import math
import pygame #Importing pygame for graphics.#
import sys #Importing sys to work with pygame.#

#Rock Paper Scissors Game#
import random

print('Welcome to rock, paper, scissors! You get five rounds. The person who wins the most rounds of the five will be player 1 for Connect 4!')

def game_function():
    options = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(options)

    print("Choose Rock, paper, or scissors!")
    player_choice = input().lower()

    print("Player chose:", player_choice)
    print("Computer chose:", computer_choice)

    if player_choice == computer_choice:
        print("It's a tie!")
    elif ((player_choice == "rock" and computer_choice == "scissors") or (player_choice == "paper" and computer_choice == "rock") or (player_choice == "scissors" and computer_choice == "paper")):
        print("You win!")
    else:
        print("You lose!")

game_function()

#Connect Four Game Continued#

#Variables#
yellow = (255,255,0)
black = (0,0,0)
cyan = (0,255,255)
green = (127,255,0)

number_of_rows = 6
number_of_columns = 7

#Functions#
def game_board(): #Game board function defined.#
    play_board = np.zeros((number_of_rows,number_of_columns)) #Create a 6 by 7 matrix of zeros as an empty board.#
    return play_board #Return this as play_board.#


def piece_drop(play_board, row, column, piece): #Player's piece being put into the board.#
    play_board[row][column] = piece #Setting up the matrix.#


def column_check(play_board, column): #This will check if the number input by each player is a plausible column.#
    return play_board[number_of_rows - 1][column] == 0 #Checks if the selected column of the fifth row (the top row) has any number other than 0. If the column is 0, then the player can put their piece in that column. If the column is not 0, then that slot has already been filled, and the player cannot go there.#


def row_check(play_board, column): #This will determine which row the player's piece will fall to.#
    for r in range(number_of_rows): 
        if play_board[r][column] == 0: #This is similar to the column-check function. If the slot in the row equals 0, then the slot is open#
            return r
    
def change_board(play_board): #Flips the board so that the pieces will go to the bottom row, rather than the top of the row. This will make the game actually look more like the authentic connect four game.#
    print(np.flip(play_board, 0))#Use numpy to flip the matrix over the x-axis.#

def win_check(play_board, piece): #This function is going to check the possible ways of winning in the game.#

 #Checking for a horizontal win#
    for col in range(number_of_columns - 3 ): #Loop iterating through the columns. We subtract 3 because a horizontal win cannot start at the fifth column, it can only start from columns 0 to 4.#
        for r in range(number_of_rows): #Loop through the rows. All the rows can work for a win.#
            if play_board[r][col] == piece and play_board[r][col + 1] == piece and play_board[r][col + 2] == piece  and play_board[r][col + 3] == piece: #We add 1 each time to check the next column to the right.#
                return True 

#Checking for vertical win#
    for col in range(number_of_columns): #Loop iterating through the columns. ALl the columns can work for a win.#
        for r in range(number_of_rows - 3): #Loop through the rows. We subtract 3 because a vertical win cannot start at the top row.#
            if play_board[r][col] == piece and play_board[r + 1][col] == piece and play_board[r + 2][col] == piece  and play_board[r + 3][col] == piece: #We add 1 each time to check the next row.#
                return True  

#Checking for positve-sloped diagonal win#
    for col in range(number_of_columns - 3): #Loop iterating through the columns.#
        for r in range(number_of_rows - 3): #Loop through the rows.#
            if play_board[r][col] == piece and play_board[r + 1][col + 1] == piece and play_board[r + 2][col + 2] == piece  and play_board[r + 3][col + 3] == piece: #We add 1 each time to check for each diagonal in the positive direction.#
                return True

#Checking for negatively-sloped diagonal win#
    for col in range(number_of_columns - 3): #Loop iterating through the columns.#
        for r in range(3, number_of_rows): #Loop through the rows starting at row 3 because the diagonal cannot begin (fit) below row 3.#
            if play_board[r][col] == piece and play_board[r - 1][col + 1] == piece and play_board[r - 2][col + 2] == piece  and play_board[r - 3][col + 3] == piece: #We add 1 each time for the columns, but we subtract 1 each time for the rows because we are moving diagonally in the negative direction.#
                return True

def show_board(play_board): #Drawing the game board graphic.#
    for col in range(number_of_columns):
        for r in range(number_of_rows):
            pygame.draw.rect(screen, yellow, (col*square_pixels, r*square_pixels+square_pixels, square_pixels, square_pixels)) #The screen is the surface. The yellow is the predefined yellow (255,255, 0). We multiply rows times the size of the square (and add the size in order to create the top row where the piece will be), the columns times the size of the square, establish the height and width, to create the rectangle. #
            pygame.draw.circle(screen, black, (int(col*square_pixels + square_pixels/2), int(r*square_pixels+square_pixels+square_pixels/2)), rad)

    for col in range(number_of_columns):
        for r in range(number_of_rows):
            if play_board[r][col] == 1: #Player 1 piece color.#
                pygame.draw.circle(screen, cyan, (int(col*square_pixels + square_pixels/2), screen_length - int(r*square_pixels + square_pixels/2)), rad)
            elif play_board[r][col] == 2: #Player 2 piece color.#
                pygame.draw.circle(screen, green, (int(col*square_pixels + square_pixels/2), screen_length - int(r*square_pixels + square_pixels/2)), rad)
    pygame.display.update()

play_board = game_board() #Initalize the game board, which is currently a zeros matrix.#
change_board(play_board) #Displays the game board so that the players can see it.#
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

myfont = pygame.font.SysFont("helvetica", 60) #Helvetica is the font, and it is size 60.#

while not game_done: #Loop is going to run when the game_done variable is false. When a player wins the game (by getting four in a row) the game_done variable will be true.#
    for event in pygame.event.get(): #Events are actions, such as clicking and mouse motions, that are part of the game.#
        if event.type == pygame.QUIT:
            sys.exit() #Allows game to properlyquit when the x button in the corner of the screen is hit.#

        if event.type == pygame.MOUSEMOTION: #Makes the players able to see their piece before dropping it into the slot. For visual effect.#
            pygame.draw.rect(screen, black, (0,0, screen_width, square_pixels)) #This will draw a rectangle so that there is just one piece being shown.#
            posx = event.pos[0]
            
            if player_turn == 0: #Player 1's turn.#
                pygame.draw.circle(screen, cyan, (posx, int(square_pixels/2)), rad)
            else: #Player 2's turn.#
                pygame.draw.circle(screen, green, (posx, int(square_pixels/2)), rad)
            pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN: #When you click down on the screen, the piece will drop.#
            pygame.draw.rect(screen, black, (0,0,screen_width, square_pixels))
           
        #Player 1 Turn#
            if player_turn == 0:
                posx = event.pos[0] #The position of x is the 0 element.#
                column = int(math.floor(posx/100)) #We divide the position by 100 to simplift it (this way its not something like 600). The floor command is a built in math command.#

                if column_check(play_board, column):
                    next_row = row_check(play_board, column) #Getting the next available row.#
                    piece_drop(play_board, next_row, column, 1) #Putting player 1's piece in their desired slot. Their piece will show up as the number 1.#

                    if win_check(play_board, 1): #Function to check if player 1 wins.#
                        label = myfont.render("Player One, you win!",1, cyan) #The text that will be displayed when player one wins.#
                        screen.blit(label, (40,10)) #The location where the font will be displayed.#
                        game_done = True #Game will be over.#


        #Player 2 Turn#
            else:
                posx = event.pos[0] #The position of x is the 0 element.#
                column = int(math.floor(posx/100)) #We divide the position by 100 to simplift it (this way its not something like 600). The floor command is a built in math command.#

                if column_check(play_board, column):
                     next_row = row_check(play_board, column) #Getting the next available row.#
                     piece_drop(play_board, next_row, column, 2) #Putting player 2's piece in their desired slot. Their piece will show up as the number 2.#
                    
                if win_check(play_board, 2): #Function to check if player 2 wins.#
                        label = myfont.render("Player Two, you win!",1, green) #Displays winning message to player 2 if they win.#
                        screen.blit(label, (40,10))
                        game_done = True #Game will be over.#

            change_board(play_board) #Calls the change_board function, so that we can see the game board after the players have taken their turns.#
            show_board(play_board)

            player_turn = player_turn + 1 #Adds to the turn each time.#
            player_turn = player_turn % 2 #Divides the value of turn by two, which makes it possible to alternate the turns between the two players.#

            if game_done:
                pygame.time.wait(5000) #Waits 5000 milliseconds after win.#
    