from processing import *
import gameboard

#declare variables
board = gameboard.board
pieces = gameboard.pieces
player_letter = None
player2_letter = None
turn = None
sizeW = 560
sizeH = 560
blackTurn = False

whitechess = ["♙", "♘" , "♗" , "♖" , "♕" , "♔" ]


blackChess = ["♟" ,  "♞" ,"♝" ,"♜", "♛" , "♚"]#add all the black pieces as string.


# #start the game
# def get_starting_player():
#   random_num = 1 
#   # print("get_starting_player() functional")  #test code
#   if random_num == 0:
#       # print("random = 0")  #test code
#       return "player"  #black
#   else:
#       # print("random = 1") #test code
#       return "player2"  #white


#run player turn	
def run_player_turn():  #
  global board
  global pieces
  if mouse.pressed and board[mouse.y//70][mouse.x//70][0] != None:
    pieces.insert(0, board[mouse.y//70][mouse.x//70][0])
    print(pieces)
    board[mouse.y//70][mouse.x//70][0] = None
    
    gameboard.drawBoard(board)
    pieces.pop(1)
    print(pieces)
    gameboard.drawBoard(board)
    return True
  elif  mouse.pressed and board[mouse.y//70][mouse.x//70][0] == None:
    # gameboard.drawBoard(board)
    gameboard.drawBoard(board)
    print(pieces)
    board[mouse.y//70][mouse.x//70][0] = pieces[0]
    gameboard.drawBoard(board)
    return True
  else:
    return False #erase the og pieces
    
def run_Player2_turn():
  global board
  global pieces
  # number = 0
  # print("2")
  if mouse.pressed and board[mouse.y//70][mouse.x//70][0] != None:
    pieces.insert(0, board[mouse.y//70][mouse.x//70][0])
    print(pieces)
    board[mouse.y//70][mouse.x//70][0] = None
    # gameboard.drawBoard(board)
    pieces.pop(1)
    print(pieces)
    gameboard.drawBoard(board)
    return True
  elif  mouse.pressed and board[mouse.y//70][mouse.x//70][0] == None:
    # gameboard.redrawSequence(board)
    print(pieces)
    board[mouse.y//70][mouse.x//70][0] = pieces[0]
    gameboard.drawBoard(board)
    return True
  else:
    return False
    
def isBlackTurn(chess): #should be a string
   global whitechess
   global blackChess
   for w in range(len(whitechess)):
     if chess == whiteChess[w]:
       return False
   for b in range(len(blackChess)):
     if chess == blackChess[b]:
       return True
   return False
   
def isBlackTurn(chess): #should be a string
   global whitechess
   global blackChess
   for w in range(len(whitechess)):
     if chess == whiteChess[w]:
       return True
   for b in range(len(blackChess)):
     if chess == blackChess[b]:
       return False
   return True
#settings (setup() only run once)
def setup():
	size(sizeW, sizeH)
	global board
	global turn
	global player_letter
	global player2_letter
	#draw the board
	gameboard.drawBoard(board)
	gameboard.drawLetters(board)
	#start()
	#drawLetters(board)
	
  #determine the text to print
	turn = "player2"

	  
#Main function (Will loops forever)
def draw():
  global board
  global turn
  global player_letter
  global player2_letter
  global pieces
  #run all the functions that is needed
  # drawBoard(board)
  # print(pieces)
  if turn == "player":
    if run_player_turn():  
      # gameboard.redrawSequence(board)
      gameboard.redrawSequence(board)
      turn = "player2"
  elif turn == "player2":
    if run_Player2_turn():
      gameboard.redrawSequence(board)
      turn = "player"
      

    
  
  


#The execute function lol
run()
