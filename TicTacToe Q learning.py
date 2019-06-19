import numpy as np
import copy
import random
import os

class TicTacToe:
	def __init__(self,playerX,playerO):
		self.board=[' ']*9
		self.playerX,self.playerO=playerX,playerO
		self.playerX_turn=random.choice([True,False])

	def play_game(self):
		self.playerX.start_game('X')
		self.playerO.start_game('O')
		while True:
			if self.playerX_turn:
				player,letter,other_player=self.playerX,'X',self.playerO
				global letter
			else:
				player,letter,other_player=self.playerO,'O',self.playerX
				global letter
			if player.type=='human':
				self.show_board()
			move=player.move(self.board)
			if self.board[move-1]!=' ':
				player.reward(-10,self.board)
				break
			self.board[move-1]=letter
			if self.player_wins():
				player.reward(1,self.board)
				other_player.reward(-1,self.board)
				break
			if self.board_full():
				player.reward(0.5,self.board)
				other_player.reward(0.5,self.board)
				break
			other_player.reward(0,self.board)
			self.playerX_turn = not self.playerX_turn

	def player_wins(self):
		#VERTICAL VICTORY
		if (self.board[0] =='X' and self.board[1] =='X' and self.board[2] == 'X'):
			return True
		elif (self.board[3]=='X' and self.board[4] =='X' and self.board[5] == 'X') or (self.board[3]=='O' and self.board[4]=='O' and self.board[5] == 'O'):
			return True
		elif (self.board[6]=='X' and self.board[7]=='X' and self.board[8] == 'X') or (self.board[6]=='O' and self.board[7]=='O' and self.board[8] == 'O'):
			return True
	#HORIZONTAL VICTORY
		elif (self.board[0]=='X' and self.board[3]=='X' and self.board[6] == 'X') or (self.board[0]=='O' and self.board[3]=='O' and self.board[6] == 'O'):
			return True
		elif (self.board[1]=='X' and self.board[4]=='X' and self.board[7] == 'X') or (self.board[1]=='O' and self.board[4]=='O' and self.board[7] == 'O'):
			return True
		elif (self.board[2]=='X' and self.board[5]=='X' and self.board[8] == 'X') or (self.board[2]=='O' and self.board[5]=='O' and self.board[8] == 'O'):
			return True
	#DIAGONAL VICTORY
		elif (self.board[0]=='X' and self.board[4]=='X' and self.board[8] == 'X') or (self.board[0]=='O' and self.board[4]=='O' and self.board[8] == 'O'):
			return True
		elif (self.board[2]=='X' and self.board[4]=='X' and self.board[6] == 'X') or (self.board[2]=='O' and self.board[4]=='O' and self.board[6] == 'O'):
			return True
		else:
			return False

	def board_full(self):
		return not any([space == ' ' for space in self.board])

	def show_board(self):
		print('      |      |   ')
		print('   '+self.board[0]+'  |   '+self.board[1]+'  |   '+self.board[2])
		print('      |      |   ')
		print('---------------------')
		print('      |      |   ')
		print('   '+self.board[3]+'  |   '+self.board[4]+'  |   '+self.board[5])
		print('      |      |   ')
		print('---------------------')
		print('      |      |   ')
		print('   '+self.board[6]+'  |   '+self.board[7]+'  |   '+self.board[8])
		print('      |      |   ')

class Player(object):
	def __init__(self):
		self.type='human'
	
	def start_game(self,letter):
		 print ("\nYou are {}!".format(letter))
	
	def move(self,board):
		return int(raw_input("Where do you want to place {}?".format(letter)))
	
	def reward(self,value,board):
		print("{} is the reward".format(value))
	
	def move_list(self,board):
		return [i+1 for i in range(0,9) if board[i] == ' ']

class QLearningPlayer(Player):
	def __init__(self,epsilon=0.2,alpha=0.3,gamma=0.9):
		self.type='QLearner'
		self.q={}
		self.epsilon=epsilon
		self.alpha=alpha
		self.gamma=gamma

	def start_game(self,letter):
		self.last_board = (' ',)*9
		self.last_move = None

	def getQ(self, state, action):
		if self.q.get((state, action)) is None:
			self.q[(state, action)] = 1.0
		return self.q.get((state, action))

	def move(self, board):
		self.last_board = tuple(board)
		actions = self.move_list(board)
		if random.random() < self.epsilon:
			self.last_move = random.choice(actions)
			return self.last_move

		qs = [self.getQ(self.last_board, a) for a in actions]
		maxQ = max(qs)

		if qs.count(maxQ) > 1:           
			best_options = [i for i in range(len(actions)) if qs[i] == maxQ]
			i = random.choice(best_options)
		else:
			i = qs.index(maxQ)

		self.last_move = actions[i]
		return actions[i]

	def reward(self, value, board):
		if self.last_move:
			self.learn(self.last_board, self.last_move, value, tuple(board))

	def learn(self, state, action, reward, result_state):
		prev = self.getQ(state, action)
		maxqnew = max([self.getQ(result_state, a) for a in self.move_list(state)])
		self.q[(state, action)] = prev + self.alpha * ((reward + self.gamma*maxqnew) - prev)

p1 = QLearningPlayer()
p2 = QLearningPlayer()
for i in xrange(0,10000):
	t = TicTacToe(p1, p2)
	t.play_game()

p1 = Player()
p2.epsilon = 0

while True:
	t = TicTacToe(p1, p2)
	t.play_game()