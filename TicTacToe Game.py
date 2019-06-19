import numpy as np
import copy
import random
import os

def main_header():
	print("""
========================

	TIC TAC TOE

========================
		""")

# def loop_game(moves_list,board):
# 	repeat=True
# 	while repeat==True:
# 		play_game(moves_list,board)
# 		inp=raw_input("Do you want to play again? (Y/N)")
# 		if inp.lower() in ['y','yes']:
# 			moves_list,board=board_reset(moves_list,board)
# 			repeat=True
# 		elif inp.lower() in ['n','no']:
# 			repeat=False
# 			print("Thanks for playing")
# 		else:
# 			print("You didnt enter Yes or No (Y/N)")
# 			break

def environment():
	print('      |      |   ')
	print('   '+board[0]+'  |   '+board[1]+'  |   '+board[2])
	print('      |      |   ')
	print('---------------------')
	print('      |      |   ')
	print('   '+board[3]+'  |   '+board[4]+'  |   '+board[5])
	print('      |      |   ')
	print('---------------------')
	print('      |      |   ')
	print('   '+board[6]+'  |   '+board[7]+'  |   '+board[8])
	print('      |      |   ')

def envi_copy():
	print('      |      |   ')
	print('   '+'1'+'  |   '+'2'+'  |   '+'3')
	print('      |      |   ')
	print('---------------------')
	print('      |      |   ')
	print('   '+'4'+'  |   '+'5'+'  |   '+'6')
	print('      |      |   ')
	print('---------------------')
	print('      |      |   ')
	print('   '+'7'+'  |   '+'8'+'  |   '+'9')
	print('      |      |   ')

def board_reset(moves_list,board):
	board=np.array([' ']*9)
	moves_list=[1,2,3,4,5,6,7,8,9]
	return moves_list, board

def choose_turn():
	inp = raw_input("Do you want to play as X or as O? ")
	player1=1
	player2=2
	if inp.lower() =='x':	
		player_list=[player1,player2]
		print("You are player 1")
		return player_list
	else:
		player_list=[player2,player1]
		print("You are player 2")
		return player_list


def player_move(board,player_list,moves_list,environment):
	if player_list[0]==1:
		move =int(raw_input("Where do you want to place the X (1-9)"))
		if move in moves_list:
			board[move-1] = 'X'
			moves_list.remove(move)
			print("PLAYER MOVE")
			environment()
		else:
			print("Move Invalid")
			print("List of possible moves", moves_list)
			player_move(board,player_list,moves_list,environment)
	else:
		move = int(raw_input("Where do you want to place the O (1-9)"))
		if move in moves_list:
			board[move-1] = 'O'
			moves_list.remove(move)
			print("PLAYER MOVE")
			environment()
		else:
			print("Move Invalid")
			print("List of possible moves", moves_list)
			player_move(board,player_list,moves_list,environment)

def random_computer_move(board,player_list,moves_list,environment):
	if player_list[0]==1:
		move=random.choice(moves_list)
		board[move-1] = 'O'
		moves_list.remove(move)
		environment()
	else:
		move=random.choice(moves_list)
		board[move-1] = 'X'
		moves_list.remove(move)
		environment()

def check_winner(board,player_list,environment,winner,moves_list):
#VERTICAL VICTORY
	if (board[0] =='X' and board[1] =='X' and board[2] == 'X'):
		return True
	elif (board[3]=='X' and board[4] =='X' and board[5] == 'X') or (board[3]=='O' and board[4]=='O' and board[5] == 'O'):
		return True
	elif (board[6]=='X' and board[7]=='X' and board[8] == 'X') or (board[6]=='O' and board[7]=='O' and board[8] == 'O'):
		return True
#HORIZONTAL VICTORY
	elif (board[0]=='X' and board[3]=='X' and board[6] == 'X') or (board[0]=='O' and board[3]=='O' and board[6] == 'O'):
		return True
	elif (board[1]=='X' and board[4]=='X' and board[7] == 'X') or (board[1]=='O' and board[4]=='O' and board[7] == 'O'):
		return True
	elif (board[2]=='X' and board[5]=='X' and board[8] == 'X') or (board[2]=='O' and board[5]=='O' and board[8] == 'O'):
		return True
#DIAGONAL VICTORY
	elif (board[0]=='X' and board[4]=='X' and board[8] == 'X') or (board[0]=='O' and board[4]=='O' and board[8] == 'O'):
		return True
	elif (board[2]=='X' and board[4]=='X' and board[6] == 'X') or (board[2]=='O' and board[4]=='O' and board[6] == 'O'):
		return True

def play_game(moves_list,board):
	envi_copy()
	player_list=choose_turn()
	winner=0
	while winner==0:
		print("List of possible moves", moves_list)
		if player_list[0]==1:
			player_move(board,player_list,moves_list,environment)
			winner1=check_winner(board,player_list,environment,winner,moves_list)
			if winner1:
				print("Player Wins")
				break
			
			if moves_list==[]:
				print("Its a draw")
				break

			print("COMPUTER MOVE")
			random_computer_move(board,player_list,moves_list,environment)
			winner2=check_winner(board,player_list,environment,winner,moves_list)
			if winner2:
				print("Computer Wins")
				break

		else:
			print("COMPUTER MOVE")
			random_computer_move(board,player_list,moves_list,environment)
			winner2=check_winner(board,player_list,environment,winner,moves_list)
			if winner2:
				print("Computer Wins")
				break
			if moves_list==[]:
				print("Its a draw")
				break

			player_move(board,player_list,moves_list,environment)
			winner1=check_winner(board,player_list,environment,winner,moves_list)
			if winner1:
				print("Player Wins")
				break
			
def main():	
	main_header()
	#loop_game(moves_list,board)
	play_game(moves_list,board)
if __name__=='__main__':
	
	board=np.array([' ']*9)
	moves_list=[1,2,3,4,5,6,7,8,9]
	main()