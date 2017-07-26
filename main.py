from processing import *
import gameboard

#declare variables
board = gameboard.board
pieces = gameboard.pieces
player_letter = None
player2_letter = None
turn = None




#start the game
def get_starting_player():
  random_num = 1  #This will lock the entire game to white only, and it must be changed
  # print("get_starting_player() functional")  #test code
  if random_num == 0:
      # print("random = 0")  #test code
      return "player"
  else:
      # print("random = 1") #test code
      return "player2"


#run player turn	
def run_player_turn():
  global board
  global pieces
  # print("run_player_turn() functional")   #test code
  if mouse.pressed and board[mouse.y//70][mouse.x//70][0] != None:
    pieces.insert(0, board[mouse.y//70][mouse.x//70][0])
    # print(pieces) #test code
    board[mouse.y//70][mouse.x//70][0] = None
    # gameboard.drawBoard(board)
    pieces.pop()
    return True
    # print(pieces) #test code
  elif  mouse.pressed and board[mouse.y//70][mouse.x//70][0] == None:
    # gameboard.drawBoard(board)
    # board[mouse.y//70][mouse.x//70][0] = pieces[number]
    return True
  else:
    return False #erase the og pieces
    
    
def run_Player2_turn():
  global board
  global pieces
  number = 0
  # print("2")
  if mouse.pressed and board[mouse.y//70][mouse.x//70][0] != None:
    pieces.insert(0, board[mouse.y//70][mouse.x//70][0])
    print(pieces) #test code
    board[mouse.y//70][mouse.x//70][0] = None
    gameboard.drawBoard(board)
    pieces.pop()
    # print(pieces) #test code
    return True
  elif  mouse.pressed and board[mouse.y//70][mouse.x//70][0] == None:
    gameboard.drawBoard(board)
    # board[mouse.y//70][mouse.x//70][0] = pieces[number]
    return True
  else:
    return False
 
              
              

#Determine lost or win
    
#settings (setup() only run once)
def setup():
	size(560,560)
	global board
	global turn
	global player_letter
	global player2_letter
# 	print("setup() functional")
	#draw the board
	gameboard.drawBoard(board)
	gameboard.drawLetters(board)
	#start()
	#drawLetters(board)
	
  #determine the text to print
	turn = get_starting_player()
	if turn == "player":
	  player_letter = "♙"
	  player2_letter = "♟"
	else:
	  player_letter = "♟"
	  player2_letter = "♙"

	  
#Main function (Will loops forever)
def draw():
  global board
  global turn
  global player_letter
  global player2_letter
  global pieces
  # print("draw() functional")  #test code
  # print("turn =", turn) #test code
  #run all the functions that is needed
  # drawBoard(board)
  # print(pieces)
  if turn == "player":
    if run_player_turn():
      # print("ran player turn") #test code
      print(board)
      turn = "player2"
  elif turn == "player2":
    if run_Player2_turn():
      # print("ran player2 turn")  #test code
      turn = "player"
      gameboard.movePieces(board)
#Selecting System
# def mouseClicked(): 
#   if player_letter:
#     board[0][6][0] = "♟"
#   elif player_letter:
#   else:
    
  
  


#The execute function lol
run()
