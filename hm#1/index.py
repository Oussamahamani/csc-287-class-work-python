
def printBoard(board):
    row = ""
    for index,tile in enumerate(board):
            row+= str(tile)+" "
            if (index+1 % 3 != 0 ):
                row+= "| "
            if (index+1) % 3 ==0 :
                print(row)
                row = ""

def getChoice(currentPlayer,board):
    while True:
        choice = input(f"Your move, {currentPlayer}: ")
        index= int(choice)-1
        if isinstance(board[index], int):
            return index
        
        print("Your choice is not valid try again.")

def check_winner(currentPlayer,board):
    win = False
    for number in range(3,10,3):
        if board[number-3] == currentPlayer and board[number-2] == currentPlayer and board[number-1] == currentPlayer:
            win = True
    for number in range(0,3):
        if board[number] == currentPlayer and board[number+3] == currentPlayer and board[number+6] == currentPlayer:
            win = True
    if board[0] == currentPlayer and board[4] == currentPlayer and board[8] == currentPlayer:
        win = True
    if board[2] == currentPlayer and board[4] == currentPlayer and board[6] == currentPlayer:
        win = True
    return win

def game_loop():
    currentTurn=1
    board = [i for i in range(1,10) ]
    while currentTurn<10:
        printBoard(board)
        currentPlayer = "x"if currentTurn %2 !=0 else "o"
        choice = getChoice(currentPlayer,board)
        board[choice] = currentPlayer
        if (check_winner(currentPlayer,board)):
            print(f"player {currentPlayer} has won the game")
            printBoard(board)
            break
        currentTurn+=1
    if currentTurn ==10:
        print("It is a draw")
        

while True:
    game_loop()
    command = input("Do you want to play another round?: ")
    if command !="yes": break