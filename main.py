from processing import *
import gameboard

#declare variables
board = gameboard.board
player_letter = None
player2_letter = None
turn = None
pieces = gameboard.pieces



#start the game
def get_starting_player():
  random_num = int(random(3))
  # print("get_starting_player() functional")  #test code
  if random_num == 0:
      # print("random = 0")  #test code
      return "player"
  else:
      # print("random = 1") #test code
      return "player2"

#run player turn	
def run_player_turn(player_letter):
  global board
  global pieces
  # print("run_player_turn() functional")   #test code
  if mouse.pressed and board[mouse.y//70][mouse.x//70][0] != None:
    pieces.append(board[mouse.y//70][mouse.x//70][0])
    print(pieces) #test code
    board[mouse.y//70][mouse.x//70][0] = None
    #gameboard.drawBoard(board)
  elif mouse.pressed and board[mouse.y//70][mouse.x//70][0] != None:
    board[mouse.y//70][mouse.x//70][0] = player2_letter
    # gameboard.drawBoard(board)
    # print(pieces) #test code
    return True
  else:
    return False
    
def run_Player2_turn(player2_letter):
  global board
  # print("run_player_turn() functional")   #test code
  if mouse.pressed and board[mouse.y//70][mouse.x//70][0] == None:
    board[mouse.y//70][mouse.x//70][0] = player2_letter
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
  gameboard.drawLetters(board)
  if turn == "player":
    if run_player_turn(player_letter):
      # print("ran player turn") #test code
      turn = "player2"
  elif turn == "player2":
    if run_Player2_turn(player2_letter):
      # print("ran player2 turn")  #test code
      turn = "player"
#Selecting System
# def mouseClicked(): 
#   if player_letter:
#     board[0][6][0] = "♟"
#   elif player_letter:
#   else:
    
  
  


#The execute function lol
run()
