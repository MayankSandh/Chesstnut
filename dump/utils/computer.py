def WhiteMatesBlack(board):
    return False
def BlackMatesWhite(board):
    return False
def BlackWhiteDraw(board):
    return False


pawn_heatmap = [
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [0.5, 0.5, 0.0, -0.1, -0.1, 0.0, 0.5, 0.5],
    [0.1, 0.1, 0.0, -0.2, -0.2, 0.0, 0.1, 0.1],
    [0.05, 0.05, 0.0, 0.1, 0.1, 0.0, 0.05, 0.05],
    [0.0, 0.0, 0.0, 0.2, 0.2, 0.0, 0.0, 0.0],
    [0.05, -0.05, 0.0, 0.0, 0.0, 0.0, -0.05, 0.05],
    [0.05, 0.1, 0.1, -0.1, -0.1, 0.1, 0.1, 0.05],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
]

knight_heatmap = [
    [-0.5, -0.4, -0.4, -0.4, -0.4, -0.4, -0.4, -0.5],
    [-0.4, -0.2, 0.0, 0.0, 0.0, 0.0, -0.2, -0.4],
    [-0.4, 0.0, 0.1, 0.2, 0.2, 0.1, 0.0, -0.4],
    [-0.4, 0.0, 0.2, 0.25, 0.25, 0.2, 0.0, -0.4],
    [-0.4, 0.0, 0.2, 0.25, 0.25, 0.2, 0.0, -0.4],
    [-0.4, 0.0, 0.1, 0.2, 0.2, 0.1, 0.0, -0.4],
    [-0.4, -0.2, 0.0, 0.0, 0.0, 0.0, -0.2, -0.4],
    [-0.5, -0.4, -0.4, -0.4, -0.4, -0.4, -0.4, -0.5]
]

bishop_heatmap = [
    [-0.2, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.2],
    [-0.1, 0.1, 0.0, 0.0, 0.0, 0.0, 0.1, -0.1],
    [-0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, -0.1],
    [-0.1, 0.0, 0.1, 0.1, 0.1, 0.1, 0.0, -0.1],
    [-0.1, 0.0, 0.0, 0.1, 0.1, 0.0, 0.0, -0.1],
    [-0.1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.1],
    [-0.1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.1],
    [-0.2, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.2]
]

rook_heatmap = [
    [0.0, 0.0, 0.0, 0.1, 0.1, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.1, 0.1, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.1, 0.1, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.1, 0.1, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.1, 0.1, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.1, 0.1, 0.0, 0.0, 0.0],
    [1.0, 1.0, 1.0, 1.1, 1.1, 1.0, 1.0, 1.0],
    [0.0, 0.0, 0.0, 0.1, 0.1, 0.0, 0.0, 0.0]
]

queen_heatmap = [
    [-0.2, -0.1, -0.1, -0.05, -0.05, -0.1, -0.1, -0.2],
    [-0.1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.1],
    [-0.1, 0.0, 0.05, 0.05, 0.05, 0.05, 0.0, -0.1],
    [-0.05, 0.0, 0.05, 0.05, 0.05, 0.05, 0.0, -0.05],
    [0.0, 0.0, 0.05, 0.05, 0.05, 0.05, 0.0, -0.05],
    [-0.1, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, -0.1],
    [-0.1, 0.0, 0.05, 0.0, 0.0, 0.0, 0.0, -0.1],
    [-0.2, -0.1, -0.1, -0.05, -0.05, -0.1, -0.1, -0.2]
]

king_heatmap = [
    [-0.3, -0.4, -0.4, -0.5, -0.5, -0.4, -0.4, -0.3],
    [-0.3, -0.4, -0.4, -0.5, -0.5, -0.4, -0.4, -0.3],
    [-0.3, -0.4, -0.4, -0.5, -0.5, -0.4, -0.4, -0.3],
    [-0.3, -0.4, -0.4, -0.5, -0.5, -0.4, -0.4, -0.3],
    [-0.2, -0.3, -0.3, -0.4, -0.4, -0.3, -0.3, -0.2],
    [-0.1, -0.2, -0.2, -0.2, -0.2, -0.2, -0.2, -0.1],
    [0.2, 0.2, 0.0, 0.0, 0.0, 0.0, 0.2, 0.2],
    [0.2, 0.3, 0.1, 0.0, 0.0, 0.1, 0.3, 0.2]
]


def evaluateBoard(board):
    score = 0
    if WhiteMatesBlack(board):
        return 1000
    if BlackMatesWhite(board):
        return -1000
    if BlackWhiteDraw(board):
        return 0
    
    for row in range(8):
        for col in range(8):
            if (board[row][col]//7 == 1):
                if (board[row][col]%7 == 6): # pawn
                    score+=(1+pawn_heatmap[row][col])
                    continue
                if (board[row][col]%7 == 5): # bishop
                    score+=(3+bishop_heatmap[row][col])
                    continue
                if (board[row][col]%7 == 4): # knight
                    score+=(3+knight_heatmap[row][col])
                    continue
                if (board[row][col]%7 == 3): # rook
                    score+=(5+rook_heatmap[row][col])
                    continue
                if (board[row][col]%7 == 2): # queen
                    score+=(9+queen_heatmap[row][col])
                    continue
            elif (board[row][col]//7 == 0):
                if (board[row][col]%7 == 6): # pawn
                    score-=(1+pawn_heatmap[row][col])
                    continue
                if (board[row][col]%7 == 5): # bishop
                    score-=(3+bishop_heatmap[row][col])
                    continue
                if (board[row][col]%7 == 4): # knight
                    score-=(3+knight_heatmap[row][col])
                    continue
                if (board[row][col]%7 == 3): # rook
                    score-=(5+rook_heatmap[row][col])
                    continue
                if (board[row][col]%7 == 2): # queen
                    score-=(9+queen_heatmap[row][col])
                    continue
    return score


def printMoveInWords(board, move, prev_board):
    prev_coord = [move[2], move[3]]
    final_coord = [move[0], move[1]]
    color = "Black" if board[final_coord[0]][final_coord[1]] //7 == 0 else "White"
    piece = ""
    if board[final_coord[0]][final_coord[1]]%7 == 6:
        piece = "pawn"
    elif board[final_coord[0]][final_coord[1]]%7 == 5:
        piece = "bishop"
    elif board[final_coord[0]][final_coord[1]]%7 == 4:
        piece = "knight"
    elif board[final_coord[0]][final_coord[1]]%7 == 3:
        piece = "rook"
    elif board[final_coord[0]][final_coord[1]]%7 == 2:
        piece = "queen"
    elif board[final_coord[0]][final_coord[1]]%7 == 1:
        piece = "king"
    message = color + " " + piece + " moved from " + str(prev_coord) + " to " + str(final_coord)
    print(message)
    # capture_message = "Capture Occurs: Piece Capture is" + prev_board[prev_coord[0]][prev_coord[1]] 
def displayGird(board, depth, currentTurn, move, prev_board):
    print("Depth is: ", depth, " | Current turn is: ", currentTurn)
    for i in range(8):
        for j in range(8):
            if board[i][j] == -1:
                print(-1, " ", end="")
                continue
            if board[i][j]<10:
                print("", board[i][j], " ", end = "")
            else:
                print(board[i][j], " ", end = "")
        print()
    printMoveInWords(board, move, prev_board)
    print("\n\n")