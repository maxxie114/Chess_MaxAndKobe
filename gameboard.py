







#This is a chess game that is created by Max and Kobe as a final project. 
#This is the class that is in charge of drawing the pieces and creating the board. 


from processing import *


#declare colors
r = 255
g = 255
b = 0
# Create the board
board = [ [[None, "brown"],[None,"yellow"],[None,"brown"],[None, "yellow"],[None,"brown"],[None, "yellow"],[None,"brown"],[None, "brown"]], 
          [[None, "yellow"],[None,"brown"],[None,"yellow"],[None, "brown"],[None,"yellow"],[None, "brown"],[None,"yellow"],[None, "yellow"]], 
          [[None, "brown"],[None,"yellow"],[None,"brown"],[None, "yellow"],[None,"brown"],[None, "yellow"],[None,"brown"],[None, "brown"]], 
          [[None, "yellow"],[None,"brown"],[None,"yellow"],[None, "brown"],[None,"yellow"],[None, "brown"],[None,"yellow"],[None, "yellow"]], 
          [[None, "brown"],[None,"yellow"],[None,"brown"],[None, "yellow"],[None,"brown"],[None, "yellow"],[None,"brown"],[None, "brown"]], 
          [[None, "yellow"],[None,"brown"],[None,"yellow"],[None, "brown"],[None,"yellow"],[None, "brown"],[None,"yellow"],[None, "yellow"]], 
          [[None, "brown"],[None,"yellow"],[None,"brown"],[None, "yellow"],[None,"brown"],[None, "yellow"],[None,"brown"],[None, "brown"]],
          [[None, "yellow"],[None,"brown"],[None,"yellow"],[None, "brown"],[None,"yellow"],[None, "brown"],[None,"yellow"],[None, "yellow"]]
          
]


pieces = []


# print("status report:\n")  #test code

#Draw the box
def drawBoard(board):
  global r
  global g
  global b
  # print("drawBoard() functional")  #test code
  fill(r, g, b)
  for y in range(len(board)):
    for x in range(len(board[0])):
      # print(y, x) #test code
      if board[y][x][1] is "brown":
        brown()
      else:
        yellow()
      # print(board[0][0][1]) #test code
      rect(x*70, y*70, 70, 70)
      fill(r, g, b)
  textSize(40)
  fill(0,0,0)
  #White Pawns

  
#Draw the new sequence
def movePieces(board):
    # print("")  #test code
    for row in range(len(board)):
      for col in range(len(board[0])):
        if board[row][col] != None :
                # print("functional")
                # print(board[row][col][0]) #test code
                textSize(40)
                text(board[row][col][0], col*70 + 13, row*70 + 46)
                fill(0,0,0)  

#Draw letters
def drawLetters(board):
    # print("")  #test code
    board[0][1][0] = "♙"
    board[1][1][0] = "♙"
    board[2][1][0] = "♙"
    board[3][1][0] = "♙"
    board[4][1][0] = "♙"
    board[5][1][0] = "♙"
    board[6][1][0] = "♙"
    board[7][1][0] = "♙"
    #White Knights
    board[1][0][0] = "♘"
    board[6][0][0] = "♘"
    #White Bishops
    board[2][0][0] = "♗"
    board[5][0][0] = "♗"  
    #White Castle
    board[0][0][0] = "♖"
    board[7][0][0] = "♖"
    #White Queen
    board[3][0][0] = "♕"
    #White King
    board[4][0][0] = "♔"
  
  
  
    # black Pawns
    board[0][6][0] = "♟"
    board[1][6][0] = "♟"
    board[2][6][0] = "♟"
    board[3][6][0] = "♟"
    board[4][6][0] = "♟"
    board[5][6][0] = "♟"
    board[6][6][0] = "♟"
    board[7][6][0] = "♟"
    #Black Knights
    board[1][7][0] = "♞"
    board[6][7][0] = "♞"  
    #Black Bishops
    board[2][7][0] = "♝"
    board[5][7][0] = "♝"
    #Black Rooks
    board[0][7][0] = "♜"
    board[7][7][0] = "♜"
    #Black Queen
    board[3][7][0] = "♛"
    #Black Kings
    board[4][7][0] = "♚"
  
    for row in range(8):
      for col in range(8):
        if board[row][col] != None :
                # print("functional")
                # print(board[row][col][0]) #test code
                textSize(40)
                text(board[row][col][0], col*70 + 13, row*70 + 46)
                fill(0,0,0)
    
#Add colors
def yellow():
  global r
  global g
  global b
  r = 255
  g = 255
  b = 0
  
def brown():
  global r
  global g
  global b
  r = 204
  g = 102
  b = 0  
