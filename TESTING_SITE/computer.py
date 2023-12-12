from operator import add
from  copy import deepcopy
def LegalSquares(board, row, col, currentTurn):
    if not isKingUnderCheck(board, currentTurn):
        if currentTurn:
            mult = -1
        else:
            mult = 1
        legal_moves = list()
        if board[row][col]//7 == currentTurn:
            if board[row][col]%7 == 5: # BISHOP MOVIES
                directions = ((1,1), (1,-1), (-1,1), (-1,-1))
                for d in directions:
                    pos = [row, col]
                    while isValid(board, pos, legal_moves, row, col, currentTurn):
                        legal_moves.append(pos)
                        pos = list((map(add, pos, d)))
                while([row, col] in legal_moves):
                    legal_moves.remove([row, col])
            elif board[row][col]%7 == 6: # PAWN MOVES
                direction = ((mult*1,0), (mult*2, 0))
                direction_attack = (mult*1,1), (mult*1,-1)
                for x,y in direction_attack:
                    if (row+x)<8 and (row+x)>=0 and (col+y)<8 and (col+y)>=0:
                        if currentTurn:
                            if board[row+x][col+y]//7 == False:
                                legal_moves.append([row+x, col+y])
                        else:
                            if board[row+x][col+y]//7 == True:
                                legal_moves.append([row+x, col+y])

                x,y = direction[0]
                if board[x+row][y+col]==-1:
                    legal_moves.append([row+x, col+y])
                    x,y = direction[1]
                    if (currentTurn):
                        if board[x+row][y+col]==-1 and row == 6:
                            legal_moves.append([row+x, col+y])
                    else:
                        if board[x+row][y+col]==-1 and row == 1:
                            legal_moves.append([row+x, col+y])
                    
            elif board[row][col]%7 == 3: # ROOK MOVIES
                directions = ((0,1), (0,-1), (-1,0), (1,0))
                for d in directions:
                    pos = [row, col]
                    while isValid(board, pos, legal_moves, row, col, currentTurn):
                        legal_moves.append(pos)
                        pos = list((map(add, pos, d)))
                while([row, col] in legal_moves):
                    legal_moves.remove([row, col])

            elif board[row][col]%7 == 2: #  QUEEN MOVES
                directions = ((0,1), (0,-1), (-1,0), (1,0))
                for d in directions:
                    pos = [row, col]
                    while isValid(board, pos, legal_moves, row, col, currentTurn):
                        legal_moves.append(pos)
                        pos = list((map(add, pos, d)))
                directions = ((1,1), (1,-1), (-1,1), (-1,-1))
                for d in directions:
                    pos = [row, col]
                    while isValid(board, pos, legal_moves, row, col, currentTurn):
                        legal_moves.append(pos)
                        pos = list((map(add, pos, d)))
                while([row, col] in legal_moves):
                    legal_moves.remove([row, col])
            elif board[row][col]%7 == 1: # KING MOVES
                direction = ((0,1), (0,-1), (-1,0), (1,-0), (1,1), (1,-1), (-1,1), (-1,-1))
                for x,y in direction:
                    if (row+x)<8 and (row+x)>=0 and (col+y)<8 and (col+y)>=0:
                        if isValid(board, [row+x, col+y], legal_moves, row, col, currentTurn):
                            legal_moves.append([row+x, col+y])
                while([row, col] in legal_moves):
                    legal_moves.remove([row, col])

                            # drawCaptureSquare(board, row+x,col+y)
            elif board[row][col]%7 == 4: # KNIGHT MOVES
                direction = ((2,1), (2,-1), (-1,2), (1,2),(-2,1), (-2,-1), (-1,-2), (1,-2))
                for x,y in direction:
                    if (row+x)<8 and (row+x)>=0 and (col+y)<8 and (col+y)>=0:
                        if isValid(board, [row+x, col+y], legal_moves, row, col, currentTurn):
                            legal_moves.append([row+x, col+y])
                while([row, col] in legal_moves):
                    legal_moves.remove([row, col])

        return legal_moves
    else:
        if currentTurn:
            mult = -1
        else:
            mult = 1
        legal_moves = list()
        if board[row][col]//7 == currentTurn:
            if board[row][col]%7 == 5: # BISHOP MOVIES
                directions = ((1,1), (1,-1), (-1,1), (-1,-1))
                for d in directions:
                    pos = [row, col]
                    while isValid(board, pos, legal_moves, row, col, currentTurn):
                        pos2 = pos + [row, col]
                        newBoard = deepcopy(board)
                        if pos2 != [row, col, row, col]:
                            makeMove(newBoard, pos2[0], pos2[1], pos2[2], pos2[3])
                            if not isKingUnderCheck(newBoard, currentTurn):
                                legal_moves.append(pos)
                        pos = list((map(add, pos, d)))
            elif board[row][col]%7 == 6: # PAWN MOVES
                direction = ((mult*1,0), (mult*2, 0))
                direction_attack = (mult*1,1), (mult*1,-1)
                for x,y in direction_attack:
                    if (row+x)<8 and (row+x)>=0 and (col+y)<8 and (col+y)>=0:
                        if currentTurn:
                            if board[row+x][col+y]//7 == False:
                                pos2 = [row+x, col+y, row, col]
                                newBoard = deepcopy(board)
                                if pos2 != [row, col, row, col]:
                                    makeMove(newBoard, pos2[0], pos2[1], pos2[2], pos2[3])
                                    if not isKingUnderCheck(newBoard, currentTurn):
                                        legal_moves.append([row+x, col+y])
                            else:
                                if board[row+x][col+y]//7 == True:
                                    pos2 = [row+x, col+y, row, col]
                                    newBoard = deepcopy(board)
                                    if pos2 != [row, col, row, col]:
                                        makeMove(newBoard, pos2[0], pos2[1], pos2[2], pos2[3])
                                        if not isKingUnderCheck(newBoard, currentTurn):
                                            legal_moves.append([row+x, col+y])

                        x,y = direction[0]
                        if board[x+row][y+col]==-1:
                            pos2 = [row+x, col+y, row, col]
                            newBoard = deepcopy(board)
                            if pos2 != [row, col, row, col]:
                                makeMove(newBoard, pos2[0], pos2[1], pos2[2], pos2[3])
                                if not isKingUnderCheck(newBoard, currentTurn):
                                    legal_moves.append([row+x, col+y])
                            x,y = direction[1]
                            if (currentTurn):
                                if board[x+row][y+col]==-1 and row == 6:
                                    pos2 = [row+x, col+y, row, col]
                                    newBoard = deepcopy(board)
                                    if pos2 != [row, col, row, col]:
                                        makeMove(newBoard, pos2[0], pos2[1], pos2[2], pos2[3])
                                        if not isKingUnderCheck(newBoard, currentTurn):
                                            legal_moves.append([row+x, col+y])
                        else:
                            if board[x+row][y+col]==-1 and row == 1:
                                pos2 = [row+x, col+y, row, col]
                                newBoard = deepcopy(board)
                                if pos2 != [row, col, row, col]:
                                    makeMove(newBoard, pos2[0], pos2[1], pos2[2], pos2[3])
                                    if not isKingUnderCheck(newBoard, currentTurn):
                                        legal_moves.append(pos)
                            
                    elif board[row][col]%7 == 3: # ROOK MOVIES
                        directions = ((0,1), (0,-1), (-1,0), (1,0))
                        for d in directions:
                            pos = [row, col]
                            while isValid(board, pos, legal_moves, row, col, currentTurn):
                                legal_moves.append(pos)
                                pos = list((map(add, pos, d)))
                        while([row, col] in legal_moves):
                            legal_moves.remove([row, col])
            elif board[row][col]%7 == 2: #  ROOK MOVES
                directions = ((0,1), (0,-1), (-1,0), (1,0))
                for d in directions:
                    pos = [row, col]
                    while isValid(board, pos, legal_moves, row, col, currentTurn):
                        pos2 = pos + [row, col]
                        newBoard = deepcopy(board)
                        if pos2 != [row, col, row, col]:
                            makeMove(newBoard, pos2[0], pos2[1], pos2[2], pos2[3])
                            if not isKingUnderCheck(newBoard, currentTurn):
                                legal_moves.append(pos)
                        pos = list((map(add, pos, d)))
            elif board[row][col]%7 == 2: #  QUEEN MOVES
                directions = ((0,1), (0,-1), (-1,0), (1,0))
                for d in directions:
                    pos = [row, col]
                    while isValid(board, pos, legal_moves, row, col, currentTurn):
                        pos2 = pos + [row, col]
                        newBoard = deepcopy(board)
                        if pos2 != [row, col, row, col]:
                            makeMove(newBoard, pos2[0], pos2[1], pos2[2], pos2[3])
                            if not isKingUnderCheck(newBoard, currentTurn):
                                legal_moves.append(pos)
                        pos = list((map(add, pos, d)))
                directions = ((1,1), (1,-1), (-1,1), (-1,-1))
                for d in directions:
                    pos = [row, col]
                    while isValid(board, pos, legal_moves, row, col, currentTurn):
                        pos2 = pos + [row, col]
                        newBoard = deepcopy(board)
                        if pos2 != [row, col, row, col]:
                            makeMove(newBoard, pos2[0], pos2[1], pos2[2], pos2[3])
                            if not isKingUnderCheck(newBoard, currentTurn):
                                legal_moves.append(pos)
                        pos = list((map(add, pos, d)))
            elif board[row][col]%7 == 1: # KING MOVES
                direction = ((0,1), (0,-1), (-1,0), (1,-0), (1,1), (1,-1), (-1,1), (-1,-1))
                for x,y in direction:
                    if (row+x)<8 and (row+x)>=0 and (col+y)<8 and (col+y)>=0:
                        if isValid(board, [row+x, col+y], legal_moves, row, col, currentTurn):
                            pos2 = [row+x, col+y, row, col]
                            newBoard = deepcopy(board)
                            if pos2 != [row, col, row, col]:
                                makeMove(newBoard, pos2[0], pos2[1], pos2[2], pos2[3])
                                if not isKingUnderCheck(newBoard, currentTurn):
                                    legal_moves.append([row+x, col+y])
            elif board[row][col]%7 == 4: # KNIGHT MOVES
                direction = ((2,1), (2,-1), (-1,2), (1,2),(-2,1), (-2,-1), (-1,-2), (1,-2))
                for x,y in direction:
                    if (row+x)<8 and (row+x)>=0 and (col+y)<8 and (col+y)>=0:
                        if isValid(board, [row+x, col+y], legal_moves, row, col, currentTurn):
                            pos2 = [row+x, col+y, row, col]
                            newBoard = deepcopy(board)
                            if pos2 != [row, col, row, col]:
                                makeMove(newBoard, pos2[0], pos2[1], pos2[2], pos2[3])
                                if not isKingUnderCheck(newBoard, currentTurn):
                                    legal_moves.append([row+x, col+y])

        return legal_moves


def WhiteMatesBlack(board):
    legal_moves = list()
    for row in range(8):
        for col in range(8):
            if board[row][col] // 7 == 0:
                # legal_moves.append(LegalSquares(board, row, col, 0))
                if LegalSquares(board, row, col, 0) != []:
                    return False
    return True
    
def BlackMatesWhite(board):
    legal_moves = list()
    for row in range(8):
        for col in range(8):
            if board[row][col] // 7 == 1:
                # legal_moves.append(LegalSquares(board, row, col, 0))
                if LegalSquares(board, row, col, 1) != []:
                    return False
    return True
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
            newBoard = deepcopy(board)
            makeMove(newBoard, row, col, og_row, og_col)
            if not isKingUnderCheck(newBoard, currentTurn): # waste king checking??
                legal_moves.append(pos)
                
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