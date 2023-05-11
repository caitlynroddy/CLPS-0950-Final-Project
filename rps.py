#Rock Paper Scissors Game#
import random

def game_function():
    print('Welcome to rock, paper, scissors! You get three rounds. The person who wins the most rounds of the three will be player 1 for Connect 4!')
    options = ['rock', 'paper', 'scissors']

    player1_points = 0
    player2_points = 0
    rounds = 0

    while rounds < 3:
        computer_choice = random.choice(options)

        print("Player 1, choose rock, paper, or scissors!")
        player_choice = input().lower()

        print("Player 1 chose:", player_choice)
        print("Computer chose:", computer_choice)

        if player_choice == computer_choice:
            print("It's a tie!")
            rounds = rounds + 1
        elif ((player_choice == "rock" and computer_choice == "scissors") or (player_choice == "paper" and computer_choice == "rock") or (player_choice == "scissors" and computer_choice == "paper")):
            print("You win!")
            rounds = rounds + 1
            player1_points = player1_points + 1
        else:
            print("You lose!")
            rounds = rounds + 1

    rounds = 0

    while rounds < 3:
            computer_choice = random.choice(options)

            print("Player 2, choose rock, paper, or scissors!")
            player_choice = input().lower()

            print("Player 2 chose:", player_choice)
            print("Computer chose:", computer_choice)

            if player_choice == computer_choice:
                print("It's a tie!")
                rounds = rounds + 1
            elif ((player_choice == "rock" and computer_choice == "scissors") or (player_choice == "paper" and computer_choice == "rock") or (player_choice == "scissors" and computer_choice == "paper")):
                print("You win!")
                rounds = rounds + 1
                player2_points = player2_points + 1
            else:
                print("You lose!")
                rounds = rounds + 1

    if player1_points > player2_points:
        print("Player 1, you win!")
    else:
        print("Player 2, you win!")