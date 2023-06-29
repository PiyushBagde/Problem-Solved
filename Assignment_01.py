board = ["-", "-", "-",
         "-","-","-",
         "-","-","-",]

currentPlayer = 'X'

winner = None

gameRunning = True


# print game board
def printBoard(board):
    print('| ' + board[0] + ' | ' + board[1] + ' | '  + board[2] + ' |')
    print("-"*13)
    print('| ' + board[3] + ' | ' + board[4] + ' | '  + board[5] + ' |')
    print("-"*13)
    print('| ' + board[6] + ' | ' + board[7] + ' | '  + board[8] + ' |')
      
#take player input
def playerInput():
    choice = int(input("Enter a number (1-9): "))
    if choice >= 1 and choice <=9 and board[choice - 1] == '-':
        board[choice - 1] = currentPlayer
    else:
        print("Please enter a valid input.")
        
        


#check for win or tie

#switch the player

#check for win or tie

while gameRunning:
    printBoard(board)
    playerInput()