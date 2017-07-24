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

#Draw letters
def drawLetters(board):
    # print("")  #test code
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