def display_board(board):									#prints the board
	print('\n'*100)
	print('   |   |   ')
	print(' '+board[0]+' | '+board[1]+' | '+board[2]+' ')
	print('   |   |   ')
	print('-----------')
	print('   |   |   ')
	print(' '+board[3]+' | '+board[4]+' | '+board[5]+' ')
	print('   |   |   ')
	print('-----------')
	print('   |   |   ')
	print(' '+board[6]+' | '+board[7]+' | '+board[8]+' ')
	print('   |   |   ')



def update_board(board, position, marker):					#visally allot marker to the board
	if (board[position-1] != 'X' and board[position-1] !='O'):
		board[(position-1)] = marker
		display_board(board)
	else:
		print('Position is Already Occupied')
	return board

def avail_check(board, position):									#checks if entered position is vacant

	return board[position-1] in ['1','2','3','4','5','6','7','8','9'] 

def full_board_check(board):
    for i in range(1,10):
        if avail_check(board, i):
            return False
    return True

def marker_allot():											#allots X and O to the player
	p1mark = ''
	while not (p1mark == 'X' or p1mark == 'O'):
		p1mark = input('Player 1 Choose your Marker (X or O)').upper()
	if p1mark == 'X':
		return ('X','O')
	else: 
		return ('O','X')


def win_check(board,marker):								#check for a victory
    
    return ((board[6] == marker and board[7] == marker and board[8] == marker) or # across the top
    (board[3] == marker and board[4] == marker and board[5] == marker) or # across the middle
    (board[1] == marker and board[2] == marker and board[0] == marker) or # across the bottom
    (board[6] == marker and board[3] == marker and board[0] == marker) or # down the left side
    (board[7] == marker and board[4] == marker and board[1] == marker) or # down the middle
    (board[8] == marker and board[5] == marker and board[2] == marker) or # down the right side
    (board[6] == marker and board[4] == marker and board[2] == marker) or # diagonal
    (board[8] == marker and board[4] == marker and board[0] == marker)) # diagonal


def replay():

    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')

import random

def choose_first():										#to allot first turn randomly
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

def player_pick(board):									#register player's move
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not avail_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
        
    return position

#________________________________________________________________________________________________________________


print('Welcome to Noughts and Crosses')
print('Developped by the-juggernaut')

while True:
	board = ['1','2','3','4','5','6','7','8','9']
    
	p1, p2 = marker_allot()

	print(f'Player one is {p1} and Player two is {p2}')
    
	turn = choose_first()
	print(turn+' will play first this game')

	play_game = input('Are you ready to play? Enter Yes or No.')

	if play_game.lower()[0] == 'y':

		game_on = True
	else:
		game_on = False

	if game_on == False:
		break


	while game_on:

		if turn == 'Player 1':
        	
			display_board(board)
			print('Player 1: ')
			position = player_pick(board)
			update_board(board, position, p1)

			if win_check(board, p1):
				print('Player 1 Wins')
				game_on = False
			else:
				if full_board_check(board):
					display_board(board)
					print('The Game is a Draw')
					break
				else:
					turn = 'Player 2'

		else:
			
			display_board(board)
			print('Player 2: ')
			position = player_pick(board)
			update_board(board, position, p2)

			if win_check(board, p2):
				print('Player 2 Wins')
				game_on = False
			else:
				if full_board_check(board):
					display_board(board)
					print('The Game is a Draw')
					break
				else:
					turn = 'Player 1'

	if not replay():
		break