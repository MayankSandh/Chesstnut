from operator import add

def WhiteMatesBlack(board):
    return False
def BlackMatesWhite(board):
    return False
def BlackWhiteDraw(board):
    return False

def makeMove(board, row, col, prev_row, prev_col):
    clicked_piece = board[prev_row][prev_col]
    board[prev_row][prev_col] = -1
    board[row][col] = clicked_piece

def isValid(board, pos, legal_moves, og_row, og_col, currentTurn):
    row, col = pos
    if row == og_row and col == og_col:
        return True
    if (row)<8 and (row)>=0 and (col)<8 and (col)>=0:
        if board[row][col]//7 == (not currentTurn):
            legal_moves.append([row, col])
            return False        
        if board[row][col]//7 == currentTurn:
            return False
        return True
        
    else:
        return False

def isKingUnderCheck(board, currentTurn):
    for r in range(8):
        for c in range(8):
            if board[r][c]//7 == currentTurn and board[r][c]%7 == 1:
                row = r
                col = c
    legal_moves = list()

    directions = ((1,1), (1,-1), (-1,1), (-1,-1)) # bishop pawn queen checker
    for d in directions:
        pos = [row, col]
        while isValid(board, pos, legal_moves, row, col, currentTurn):
            legal_moves.append(pos)
            pos = list((map(add, pos, d)))
        if (pos[0]<8 and pos[0]>-1 and pos[1] < 8 and pos[1]>-1) and board[pos[0]][pos[1]]//7 == (not currentTurn) and (board[pos[0]][pos[1]]%7 == 6 or board[pos[0]][pos[1]]%7 == 5 or board[pos[0]][pos[1]]%7 == 2):
            return True
                
    directions = ((0,1), (0,-1), (-1,0), (1,0)) # rook queen checker
    for d in directions:
        pos = [row, col]
        while isValid(board, pos, legal_moves, row, col, currentTurn):
            legal_moves.append(pos) # waste list wasteage of space
            pos = list((map(add, pos, d)))
        if (pos[0]<8 and pos[0]>-1 and pos[1] < 8 and pos[1]>-1) and board[pos[0]][pos[1]]//7 == (not currentTurn) and (board[pos[0]][pos[1]]%7 == 3 or board[pos[0]][pos[1]]%7 == 2):
            return True

    direction = ((2,1), (2,-1), (-1,2), (1,2),(-2,1), (-2,-1), (-1,-2), (1,-2)) # knight checker
    for x,y in direction:
        if (row+x)<8 and (row+x)>=0 and (col+y)<8 and (col+y)>=0:
            if isValid(board, [row+x, col+y], legal_moves, row, col, currentTurn):
                legal_moves.append([row+x, col+y])
            if board[row+x][col+y]//7 == (not currentTurn) and (board[row+x][col+y]%7 == 4):
                return True

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


# def moveGenerationTest(board, depth, currentTurn, move, prev_board):
#     new_board = deepcopy(board)
#     # displayGird(new_board, depth, currentTurn, move, prev_board)

#     if (depth == 0):
#         return 1
    
#     move_list = list()
#     for row in range(8):
#         for col in range(8):
#             if board[row][col] // 7 == currentTurn:
#                 for move in LegalSquares(board, row, col, currentTurn):
#                     move_list.append([move[0], move[1], row, col])
#     positions = 0
#     if currentTurn:
#         nextTurn = False
#     else:
#         nextTurn = True

#     for move in move_list:
#         computer.makeMove(new_board, move[0], move[1], move[2], move[3])
#         # displayGird(new_board, depth, currentTurn, move, board)
#         positions+=moveGenerationTest(new_board, depth-1, nextTurn, move, board)
#         new_board = deepcopy(board)
#     return positions