import os
import random

play_coord = '' # placeholder for the player coordinates
plays = {} # placeholder for the grid initialization
players = ['X', 'O'] # defines players' marks
score = [0, 0]
winning_combinations = [['a1', 'b1', 'c1'], ['a2', 'b2', 'c2'], ['a3', 'b3', 'c3'],
                        ['a1', 'a2', 'a3'], ['b1', 'b2', 'b3'], ['c1', 'c2', 'c3'],
                        ['a1', 'b2', 'c3'], ['a3', 'b2', 'c1']]
play_x = []  # records player X coordinates
play_y = []  # records player Y coordinates

# clear screen after each participant plays
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def initialize_game():
        ''' Resets the grid '''
        global plays, player_turn, play_x, play_y
        plays = {'a1': ' ', 'a2': ' ', 'a3': ' ', 'b1': ' ', 'b2': ' ', 'b3': ' ', 'c1': ' ', 'c2': ' ',
                 'c3': ' '}
        player_turn = random.randint(0, 1)
        play_x = []
        play_y = []


def test_winner() -> str:
        ''' test if current player's coordinates are among winning_combinations
        and returns string: winning (w), draw (d), or continue (c)'''

        if player_turn == 0:
                check_play = play_x
        else:
                check_play = play_y
        for item in winning_combinations:
                if set(item).issubset(set(check_play)):
                        return 'w'
                elif len(play_x) + len(play_y) == 9:
                        return 'd'
        return 'c'

def update_grid():
        '''This function initializes and updates the grid with the players coordinates at every turn'''
        cls()
        grid = [['     ',' ', ' ', ' ', 'A', ' ', ' ', ' ', ' ', ' ', 'B', ' ', ' ', ' ', ' ', ' ', ' C', ' ', ' '],
                ['     ', ' ', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
                ['     ', '|', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', '|'],
                ['  1  ', '|', ' ', ' ', plays['a1'], ' ', ' ', '|', ' ', ' ', plays['b1'], ' ', ' ', '|', ' ', ' ', plays['c1'], ' ', ' ', '|'],
                ['     ', '|', '_', '_', '_', '_', '_', '|', '_', '_', '_', '_', '_', '|', '_', '_', '_', '_', '_', '|'],
                ['     ', '|', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', '|'],
                ['  2  ', '|', ' ', ' ', plays['a2'], ' ', ' ', '|', ' ', ' ', plays['b2'], ' ', ' ', '|', ' ', ' ', plays['c2'], ' ', ' ', '|'],
                ['     ', '|', '_', '_', '_', '_', '_', '|', '_', '_', '_', '_', '_', '|', '_', '_', '_', '_', '_', '|'],
                ['     ', '|', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', '|'],
                ['  3  ', '|', ' ', ' ', plays['a3'], ' ', ' ', '|', ' ', ' ', plays['b3'], ' ', ' ', '|', ' ', ' ', plays['c3'], ' ', ' ', '|'],
                ['     ', '|', '_', '_', '_', '_', '_', '|', '_', '_', '_', '_', '_', '|', '_', '_', '_', '_', '_', '|']]
        for line in grid:
            print(''.join(line))


initialize_game()
print('Welcome to Tic-Tac_Toe game! Player 1 mark is \'X\', player 2 mark is \'O\' ')
print(f'Player \'{players[player_turn]}\' starts. \n')
game_on = True
print(f'Score: Player \'X\' = {score[0]} vs Player \'O\' = {score[1]}')
while game_on:
        # ask for player input and test if it is a valid option
        valid = False
        update_grid()
        while not valid:
                play_coord = input(f'Player \'{players[player_turn]}\', please chose the coordinates of your play! (for example: B2, C1, ...:  ').lower()
                if play_coord not in plays:
                        print('\nPlease enter a valid coordinate.\n')
                elif plays[play_coord] != ' ':
                        print('\nThis position is not valid as it is already taken.')
                else:
                        valid = True
        # assigns player choice to a list of player choices and modifies the grid accordingly
        if players[player_turn] == 'X':
                play_x.append(play_coord)
                plays[play_coord] = 'X'
        elif players[player_turn] == 'O':
                play_y.append(play_coord)
                plays[play_coord] = 'O'

        # this function tests if the recent play was a winner
        test = test_winner()
        if test == 'w':
                score[player_turn] += 1
                cls()
                update_grid()
                print(f'Congratulations player \'{players[player_turn]}\', you won. The updated score is: '
                          f'Player \'X\' = {score[0]} vs Player \'O\' = {score[1]}')
                x = input(' Would you like to play again( Y / N ?').lower()
                if x == 'y':
                        initialize_game()
                else:
                        print('Thank you for playing, bye bye!')
                        game_on = False
        elif test == 'd':
                x = input('Good job guys, this is a draw, try again?').lower()
                if x == 'y':
                        initialize_game()
                else:
                        print('Thank you for playing, bye bye!')
                        game_on = False
        elif test == 'c':
                # switch player turn
                player_turn = abs(player_turn - 1)






