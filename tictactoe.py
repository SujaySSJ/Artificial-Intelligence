import os
import itertools
import math
board=[['_' for x in range(3)]for y in range(3)]
indices=[0,1,2]
player='X'
opponent='0'
def makeMove(face,row,col):
	board[row][col]=face

def printBoard():
	os.system("clear")
	for row in range(3):
		for col in range(3):
			print(board[row][col]),
		print 

def areMovesLeft():
	return any('_' in sublist for sublist in board)	

def evaluate():
	for row in range(3):
		if board[row][0] is not '_':
			if all(board[row][0] == x for x in board[row]):
				if board[row][0] is not opponent:
					return 10
				else:
					return -10
	for col in range(3):
		if board[0][col] is not '_':
			if board[0][col]==board[1][col] and board[1][col]==board[2][col]:
				if board[0][col] is not opponent:
					return 10
				else:
					return -10
	if board[0][0]==board[1][1] and board[1][1]==board[2][2] and board[0][0] is not '_':
		if board[0][0] is not opponent:
			return 10
		else:
			return -10	
	if board[0][2]==board[1][1] and board[1][1]==board[2][0] and board[0][2] is not '_':
		if board[0][2] is not opponent:
			return 10
		else:
			return -10
	return 0		

def minimax(depth,playerType,alpha,beta):
	score=evaluate()
	if score==10:
		return score
	elif score==-10:
		return score
	if(areMovesLeft() is False):
		return 0
	if playerType is 'X':
		max_score=-20
		for row,col in itertools.product(indices,repeat=2):
			if board[row][col] is '_':
				board[row][col]=playerType
				max_score=max(max_score,minimax(depth+1,'0',alpha,beta))
				alpha=max(max_score,alpha)
				board[row][col]='_'
				if beta<=alpha:
					break
		return max_score
	if playerType is '0':
		min_score=20
		for row,col in itertools.product(indices,repeat=2):
			if board[row][col] is '_':
				board[row][col]=playerType
				min_score=min(min_score,minimax(depth+1,'X',alpha,beta))
				beta=min(min_score,beta)
				board[row][col]='_'
				if beta<=alpha:
					break
		return min_score

def getNextMove():
	max_board_score=-20
	next_row,next_col=-1,-1
	for row,col in itertools.product(indices,repeat=2):
		if board[row][col] is '_':
			board[row][col]=player
			new_board_score=minimax(0,opponent,1000,-1000)
			board[row][col]='_'
			if new_board_score>max_board_score:
				max_board_score=new_board_score
				next_row,next_col=row,col
	return next_row,next_col			


# makeMove('X',0,2)
# makeMove('X',1,1)
# makeMove('X',2,0)
# printBoard()
# print(evaluate())
# for row,col in itertools.product(indices,repeat=2):
# 	print(row,col)

print("X is computer")
ch=raw_input("Do you want to go first?")
if ch=='y':
	row,col=raw_input("Enter position: ").split()
	board[int(row)][int(col)]=opponent
	printBoard()
	

while areMovesLeft() is True:
	score=evaluate()
	if score is 0 and areMovesLeft() is False:
		print("Game Tied")
		break
	elif score is 10:
		print("You Lose")
		break
	row,col=getNextMove()
	board[row][col]=player
	printBoard()
	row,col=raw_input("Enter position: ").split()
	board[int(row)][int(col)]=opponent
	printBoard()

		
