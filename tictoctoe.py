


def isValidBoard(board):
    if len(board) != 3:  # 1st dimension
        print("how dare u call me with that!!!")
        return False
    
    if len(board[0]) != 3 or len(board[1]) != 3 or len(board[2]) != 3: # 2nd dimensoin
        print("how dare u call me with that second!!!")
        return False

    for r in range(len(board)):
        for c in range(len(board[0])):
            if (board[r][c] == -1 or board[r][c] == 0 or board[r][c] == 1):
                continue
            else:
                print("How dare u call me with wrong values! Are u out of ur mind!!!")
                return False
    
    return True


def didAnyoneWin(v1, v2, v3):
    if (v1 or v2 or v3) == 0:
        return False

    return v1 == v2 and v2 == v3

# given a 2-d (3 * 3) board, return if a player won or nobody won
# board values should only be -1 (O), 0, 1 (X)
def didIWin(board):
    if not isValidBoard(board):
        return {"error": "What did u say?"}

    # check rows
    for r in range(len(board)):
        player = "X" if board[r][0] == 1 else "O"

        #if isAWinningLine(r, 0, board[r][0], r, 1, board[r][1], r, 2, board[r][2]):
        if didAnyoneWin(board[r][0], board[r][1], board[r][2]):
            return {"result" : player + " Won!!!"}

    #check columns
    for c in range(len(board[0])):
        player = "X" if board[0][c] == 1 else "O" 

        #if isAWinningLine(0, c, board[0][c], 1, c, board[1][c], 2, c, board[2][c]):
        if didAnyoneWin(board[0][c], board[1][c], board[2][c]):
            return {"result" : player + " Won!!!"}

    #check diagonal 1
    player = "X" if board[0][0] == 1 else "O"

    #if isAWinningLine(0, 0, board[0][0], 1, 1, board[1][1], 2, 2, board[2][2]):
    if didAnyoneWin(board[0][0], board[1][1], board[2][2]):
        return {"result" : player + " Won!!!"}
        

    #check diagonal 2
    player = "X" if board[0][2] == 1 else "O"

    #if isAWinningLine(0, 2, board[0][2], 1, 1, board[1][1], 2, 0, board[2][0]):
    if didAnyoneWin(board[0][2], board[1][1], board[2][0]):
        return {"result" : player + " Won!!!"}

    return {"error" : 'game continues'}


def checkBoard(curBoard):
    if (len(curBoard) != 9):
        return {"error" : "check your board!"}

    board = [[0 for x in range(3)] for y in range(3)]

    for i in range(len(curBoard)):
        board[i//3][i%3] = curBoard[i]

    return didIWin(board)

