ME = 1
if ME:
    OPP = 0
else:
    OPP = 1

currentTurn = True

lastMoveOfBlack = [0, 0]
lastMoveOfWhite = [0, 0]

blackPiecesLocation = list()
whitePiecesLocation = list()

BlackKing = 1
WhiteKing = 7
BlackQueen = 2
WhiteQueen = 9
BlackRook = 3
WhiteRook = 10
BlackKnight = 4
WhiteKnight = 11
BlackBishop = 5
WhiteBishop = 12
BlackPawn = 6
WhitePawn = 13

hasWhiteKingMoved, hasBlackKingMoved, hasWhiteLeftRookMoved, hasBlackLeftRookMoved, hasWhiteRightRookMoved, hasBlackRightRookMoved = False, False, False, False, False, False

def fetchConstants():
    global hasWhiteKingMoved, hasBlackKingMoved, hasWhiteLeftRookMoved, hasBlackLeftRookMoved, hasWhiteRightRookMoved, hasBlackRightRookMoved, blackPiecesLocation, whitePiecesLocation
    return [hasWhiteKingMoved, hasBlackKingMoved, hasWhiteLeftRookMoved, hasBlackLeftRookMoved, hasWhiteRightRookMoved, hasBlackRightRookMoved, blackPiecesLocation, whitePiecesLocation]
def restoreConstants(constants):
    global hasWhiteKingMoved, hasBlackKingMoved, hasWhiteLeftRookMoved, hasBlackLeftRookMoved, hasWhiteRightRookMoved, hasBlackRightRookMoved, blackPiecesLocation, whitePiecesLocation
    hasWhiteKingMoved, hasBlackKingMoved, hasWhiteLeftRookMoved, hasBlackLeftRookMoved, hasWhiteRightRookMoved, hasBlackRightRookMoved, blackPiecesLocation, whitePiecesLocation = constants[0], constants[1], constants[2], constants[3], constants[4], constants[5], constants[6], constants[7]
def printConstants():
    global hasWhiteKingMoved, hasBlackKingMoved, hasWhiteLeftRookMoved, hasBlackLeftRookMoved, hasWhiteRightRookMoved, hasBlackRightRookMoved, blackPiecesLocation, whitePiecesLocation
    print(hasWhiteKingMoved, hasBlackKingMoved, hasWhiteLeftRookMoved, hasBlackLeftRookMoved, hasWhiteRightRookMoved, hasBlackRightRookMoved, blackPiecesLocation, whitePiecesLocation)

def changeKingStatus(piece_code):
    global hasWhiteKingMoved, hasBlackKingMoved
    if isWhite(piece_code):
        hasWhiteKingMoved = True
    else:
        hasBlackKingMoved = True
def changeRightRookStatus(piece_code):
    global hasWhiteRightRookMoved, hasBlackRightRookMoved
    if isWhite(piece_code):
        hasWhiteRightRookMoved = True
    else:
        hasBlackRightRookMoved = True
def changeLeftRookStatus(piece_code):
    global hasWhiteLeftRookMoved, hasBlackLeftRookMoved
    if isWhite(piece_code):
        hasWhiteLeftRookMoved = True
    else:
        hasBlackLeftRookMoved = True
def changeRookStatus(piece_code, prev_index):
    global hasWhiteLeftRookMoved, hasBlackLeftRookMoved, hasWhiteRightRookMoved, hasBlackRightRookMoved
    if isWhite(piece_code):
        if prev_index%8 == 0 and not hasWhiteLeftRookMoved:
            hasWhiteLeftRookMoved = True
        elif not hasWhiteRightRookMoved:
            hasWhiteRightRookMoved = True
    else:
        if prev_index%8 == 0 and not hasBlackLeftRookMoved:
            hasBlackLeftRookMoved = True
        elif not hasBlackRightRookMoved:
            hasBlackRightRookMoved = True 

def castlingFlagsHandler(piece, move):
    
    if isBlack(piece):
        pass

# def restoreConstants(whiteKing, blackKing, whiteLR, blackLR, whiteRR, blackRR):
#     global hasWhiteKingMoved, hasBlackKingMoved, hasWhiteLeftRookMoved, hasBlackLeftRookMoved, hasWhiteRightRookMoved, hasBlackRightRookMoved
#     hasWhiteKingMoved, hasBlackKingMoved, hasWhiteLeftRookMoved, hasBlackLeftRookMoved, hasWhiteRightRookMoved, hasBlackRightRookMoved = whiteKing, blackKing, whiteLR, blackLR, whiteRR, blackRR

def isBlankSquare(piece_code):
    if piece_code%7 == -1:
        return True
    else:
        return False
def isBlack(piece_code):
    if piece_code//7 == 0:
        return True
    else:
        return False
def isWhite(piece_code):
    if piece_code//7 == 1:
        return True
    else:
        return False

def isKing(piece_code):
    if piece_code%7 == 1:
        return True
    else:
        return False
def isQueen(piece_code):
    if piece_code%7 == 2:
        return True
    else:
        return False
def isRook(piece_code):
    if piece_code%7 == 3:
        return True
    else:
        return False
def isKnight(piece_code):
    if piece_code%7 == 4:
        return True
    else:
        return False
def isBishop(piece_code):
    if piece_code%7 == 5:
        return True
    else:
        return False
def isPawn(piece_code):
    if piece_code%7 == 6:
        return True
    else:
        return False

def isSlidingPiece(piece_code):
    if isBishop(piece_code) or isQueen(piece_code) or isRook(piece_code):
        return True
    else:
        return False

def isKingSafe(targetSquare, currentTurn):
    return True

def squareWithinBounds(index, direction):
    row_add, col_add = actualOffsets[direction]
    row, col = index//8+row_add, index%8+col_add
    if (row > 7) or (row < 0):
        return False
    else:
        if (col > 7) or (col < 0):
            return False
        else:
            return True

def readFen(fen):
    piece_codes = {
        '1': -1,
        'k': 1,  # black king
        'q': 2,  # black queen
        'r': 3,  # black rook
        'n': 4,  # black knight
        'b': 5,  # black bishop
        'p': 6,  # black pawn
        'K': 8,  # white king
        'Q': 9,  # white queen
        'R': 10, # white rook
        'N': 11, # white knight
        'B': 12, # white bishop
        'P': 13  # white pawn
    }
    board = [-1]*64  # Initialize the chessboard with zeros
    fen = fen.split(' ')[0]  # Remove additional FEN information after the board position

    col_index = 0  # Start from index 0 to properly populate the board
    row_index = 0
    for char in fen:
        if char.isdigit():
            row_index += int(char)
        elif char == '/':
            col_index += 1
            row_index = 0
        elif char in piece_codes:
            piece_code = piece_codes[char]
            board[col_index*8+row_index] = piece_code
            if isBlack(piece_code):
                blackPiecesLocation.append(col_index*8+row_index)
            else:
                whitePiecesLocation.append(col_index*8+row_index)
            row_index += 1
        else:
            continue  # Ignore unexpected characters
    if (not ME):
        board = board[::-1]
    return board

DirectionOffsets = [-8, 8, -1, 1, 7, -7, 9, -9]
numSquaresToEdge = []
for i in range(64):
    numSquaresToEdge.append(list())
for row in range(8):
    for col in range(8):
        numNorth = row
        numSouth = 7-row
        numWest = col
        numEast = 7 - col
        numSquaresToEdge[row*8+col] = [
            numNorth,
            numSouth,
            numWest,
            numEast,
            min(numSouth, numWest),
            min(numNorth, numEast),
            min(numSouth, numEast),
            min(numNorth, numWest)
        ]

actualOffsets = {
    -17: (-2, -1),
    -10: (-1, -2),
    6: (1, -2),
    15: (2, -1),
    -15: (-2, 1),
    -6: (-1, 2),
    10: (1, 2),
    17: (2, 1),
    7: (1,-1),
    9: (1, 1),
    -7: (-1, 1),
    -9: (-1, -1),
    -1: (0, -1),
    1: (0, 1),
    8: (1, 0),
    -8: (-1, 0)
}

def legalMoves(board, index, currentTurn):
    piece = board[index]
    if (piece)//7 == currentTurn:
        if isSlidingPiece(piece):
            return (generateSlidingMoves(board, index, currentTurn))
        if isKnight(piece):
            return (generateKnightMoves(board, index, currentTurn))
        if isPawn(piece):
            return (generatePawnMoves(board, index, currentTurn))
        if isKing(piece):
            return (generateKingMoves(board, index, currentTurn))

def generateAllMoves(board, currentTurn):
    allMovesList = list()
    for startSquare in range(64):
        piece = board[startSquare]
        if (piece)//7 == currentTurn:
            if isSlidingPiece(piece):
                allMovesList+=(generateSlidingMoves(board, startSquare, currentTurn))
            if isKnight(piece):
                allMovesList+=(generateKnightMoves(board, startSquare, currentTurn))
            if isPawn(piece):
                allMovesList+=(generatePawnMoves(board, startSquare, currentTurn))
            if isKing(piece):
                allMovesList+=(generateKingMoves(board, startSquare, currentTurn))
    return allMovesList

def generateKnightMoves(board, index, currentTurn):
    move_list = list()
    knightDirections = [-15, -17, 15, 17, 10, -6, -10, 6]
    for direction in knightDirections:
        targetSquare = index+direction
        if squareWithinBounds(index, direction):
            pieceOnTargetSquare = board[targetSquare]
            if (pieceOnTargetSquare//7 == currentTurn):
                continue
            else:
                move_list.append([index, targetSquare])
    return move_list

def generateSlidingMoves(board, index, currentTurn):
    move_list = list()
    piece = board[index]
    startIndex = (0+4*(isBishop(piece)))
    endIndex = (4+4*(not isRook(piece)))
    for directionIndex in range(startIndex, endIndex):
        for n in range(numSquaresToEdge[index][directionIndex]):
            targetSquare = index + DirectionOffsets[directionIndex]*(n+1)
            pieceOnTargetSquare = board[targetSquare]
            if pieceOnTargetSquare//7 == currentTurn:
                break
            move_list.append([index, targetSquare])
            if (pieceOnTargetSquare)//7 == (not currentTurn):
                break
    return move_list

def generatePawnMoves(board, index, currentTurn):
    move_list = list()
    row, col = index//8, index%8
    piece = board[index]
    if ME:
        if isWhite(piece):
            directions = [-8, -16]
            if board[directions[0]+index]//7 == -1:
                move_list.append([index, directions[0]+index])
                if row == 6:
                    if board[directions[1]+index]//7 == -1:
                        move_list.append([index, directions[1]+index])
            directionsAttack = [-7, -9]
            for direction in directionsAttack:
                targetSquare = index+direction
                if squareWithinBounds(index, direction):
                    if board[targetSquare]//7 == (not currentTurn):
                        move_list.append([index, targetSquare])
                    
        else:
            directions = [8, 16]
            if board[directions[0]+index]//7 == -1:
                move_list.append([index, directions[0]+index])
                if row == 1:
                    if board[directions[1]+index]//7 == -1:
                        move_list.append([index, directions[1]+index])
            directionsAttack = [7, 9]
            for direction in directionsAttack:
                targetSquare = index+direction
                if squareWithinBounds(index, direction):
                    if board[targetSquare]//7 == (not currentTurn):
                        move_list.append([index, targetSquare])
    else:
        if isBlack(piece):
            directions = [-8, -16]
            if board[directions[0]+index]//7 == -1:
                move_list.append([index, directions[0]+index])
                if row == 6:
                    if board[directions[1]+index]//7 == -1:
                        move_list.append([index, directions[1]+index])
            directionsAttack = [-7, -9]
            for direction in directionsAttack:
                targetSquare = index+direction
                if squareWithinBounds(index, direction):
                    if board[targetSquare]//7 == (not currentTurn):
                        move_list.append([index, targetSquare])
        else:
            directions = [8, 16]
            if board[directions[0]+index]//7 == -1:
                move_list.append([index, directions[0]+index])
                if row == 1:
                    if board[directions[1]+index]//7 == -1:
                        move_list.append([index, directions[1]+index])
            directionsAttack = [7, 9]
            for direction in directionsAttack:
                targetSquare = index+direction
                if squareWithinBounds(index, direction):
                    if board[targetSquare]//7 == (not currentTurn):
                        move_list.append([index, targetSquare])
    return move_list

def generateKingMoves(board, index, currentTurn):
    global hasWhiteKingMoved, hasBlackKingMoved, hasWhiteLeftRookMoved, hasBlackLeftRookMoved, hasWhiteRightRookMoved, hasBlackRightRookMoved
    move_list = list()
    piece = board[index]
    for direction in DirectionOffsets:
        targetSquare = index+direction
        if squareWithinBounds(index, direction):
            if board[targetSquare]//7 == currentTurn:
                continue
            if isKingSafe(targetSquare, currentTurn):
                move_list.append([index, targetSquare])

    if ME:
        if isWhite(piece):
            if (not hasWhiteKingMoved):
                if (not hasWhiteLeftRookMoved):
                    LeftCastlingPossible = False
                    ctr = index-1
                    for i in range(1,4):
                        if board[ctr]!= -1:
                            break
                        ctr-=1
                    else:
                        LeftCastlingPossible = True
                    if LeftCastlingPossible:
                        move_list.append([index, index-2])
                if (not hasWhiteRightRookMoved):
                    RightCastlingPossible = False
                    ctr = index+1
                    for i in range(5,7):
                        if board[ctr]!= -1:
                            break
                        ctr+=1
                    else:
                        RightCastlingPossible = True
                    if RightCastlingPossible:
                        move_list.append([index, index+2])
        else:
            if (not hasBlackKingMoved):
                if (not hasBlackLeftRookMoved):
                    LeftCastlingPossible = False
                    ctr = index-1
                    for i in range(1,4):
                        if board[ctr]!= -1:
                            break
                        ctr-=1
                    else:
                        LeftCastlingPossible = True
                    if LeftCastlingPossible:
                        move_list.append([index, index-2])
                if (not hasBlackRightRookMoved):
                    RightCastlingPossible = False
                    ctr = index+1
                    for i in range(5,7):
                        if board[ctr]!= -1:
                            break
                        ctr+=1
                    else:
                        RightCastlingPossible = True
                    if RightCastlingPossible:
                        move_list.append([index, index+2])
    else:
        if isBlack(piece):
            if (not hasBlackKingMoved):
                if (not hasBlackRightRookMoved):
                    LeftCastlingPossible = False
                    ctr = index+1
                    for i in range(1,4):
                        if board[ctr]!= -1:
                            break
                        ctr+=1
                    else:
                        RightCastlingPossible = True
                    if RightCastlingPossible:
                        move_list.append([index, index+2])
                if (not hasBlackLeftRookMoved):
                    LeftCastlingPossible = False
                    ctr = index-1
                    for i in range(5,7):
                        if board[ctr]!= -1:
                            break
                        ctr-=1
                    else:
                        LeftCastlingPossible = True
                    if LeftCastlingPossible:
                        move_list.append([index, index-2])
        else:
            if (not hasWhiteKingMoved):
                if (not hasWhiteRightRookMoved):
                    LeftCastlingPossible = False
                    ctr = index+1
                    for i in range(1,4):
                        if board[ctr]!= -1:
                            break
                        ctr+=1
                    else:
                        RightCastlingPossible = True
                    if RightCastlingPossible:
                        move_list.append([index, index+2])
                if (not hasWhiteLeftRookMoved):
                    LeftCastlingPossible = False
                    ctr = index-1
                    for i in range(5,7):
                        if board[ctr]!= -1:
                            break
                        ctr-=1
                    else:
                        LeftCastlingPossible = True
                    if LeftCastlingPossible:
                        move_list.append([index, index-2])
    return move_list

def makeMove(board, move): # also return the piece captured
    global blackPiecesLocation, whitePiecesLocation

    flag = 0
    clicked_piece = board[move[0]]
    captured_piece = board[move[1]]
    board[move[1]] = clicked_piece
    board[move[0]] = -1
    piece = board[move[1]]

    if captured_piece%7 != -1:
        pass

    #promotion handler
    if isPawn(piece) and ((move[1]//8 == 0) or (move[1]//8 == 7)):
        board[move[1]] = 7*(isWhite(piece))+2
        flag = 2

    #castling handler
    isCastling = False
    if isKing(piece) and ((move[1]%8 - move[0]%8 == 2) or (move[1]%8 - move[0]%8 == -2)):
        isCastling = True
        if (move[1]%8 - move[0]%8 == 2): # right castling
            board[move[1]-1] = board[((move[1]//8)+1)*8 - 1]
            board[((move[1]//8)+1)*8 - 1] = -1
            updatePieceLocationMoved(board[((move[1]//8)+1)*8 - 1], [((move[1]//8)+1)*8 - 1, move[1]-1])
        else: # left castling
            board[move[1]+1] = board[((move[1]//8))*8]
            board[((move[1]//8))*8] = -1
            updatePieceLocationMoved(board[((move[1]//8))*8], [((move[1]//8))*8, move[1]+1])
        flag = 1
    if not isCastling:
        updatePieceLocationMoved(piece, move)
    updatedPieceLocationCaptured(captured_piece, move)
    
    return captured_piece, flag

def unmakeMove(board, move, captured_piece, flag): # the move should be as it was made before and not like reverse the move or something
    if flag == 0:
        clicked_piece = board[move[1]]
        board[move[0]] = clicked_piece
        board[move[1]] = captured_piece
        restoreCapturePieceLocation(captured_piece, move)
        # updatedPieceLocationCaptured(captured_piece, move)
            
    elif flag == 1:
        if (move[1]%8 - move[0]%8 == 2):
            clicked_piece = board[move[1]]
            board[move[0]] = clicked_piece
            board[move[1]] = captured_piece
            restoreCapturePieceLocation(captured_piece, move)
            cancelRightCastelling(board, move)
            
        else:
            clicked_piece = board[move[1]]
            board[move[0]] = clicked_piece
            board[move[1]] = captured_piece
            restoreCapturePieceLocation(captured_piece, move)
            cancelLeftCastelling(board, move)
    elif flag == 2:
        clicked_piece = board[move[1]]
        if isWhite(clicked_piece):
            board[move[0]] = WhitePawn
        else:
            board[move[0]] = BlackPawn
        board[move[1]] = captured_piece
        updatedPieceLocationCaptured(clicked_piece, [move[1], move[0]])

def cancelRightCastelling(board, move):
    global hasWhiteKingMoved, hasBlackKingMoved, hasWhiteLeftRookMoved, hasBlackLeftRookMoved, hasWhiteRightRookMoved, hasBlackRightRookMoved
    if isWhite(board[move[1]]):
        hasWhiteKingMoved = False
        hasWhiteRightRookMoved = False
    else:
        hasBlackKingMoved = False
        hasBlackRightRookMoved = False
    board[((move[1]//8)+1)*8 - 1] = board[move[1]-1]
    board[move[1]-1] = -1
    updatePieceLocationMoved(board[move[1]-1], [move[1]-1, ((move[1]//8)+1)*8 - 1])
def cancelLeftCastelling(board, move):
    global hasWhiteKingMoved, hasBlackKingMoved, hasWhiteLeftRookMoved, hasBlackLeftRookMoved, hasWhiteRightRookMoved, hasBlackRightRookMoved
    if isWhite(board[move[1]]):
        hasWhiteKingMoved = False
        hasWhiteLeftRookMoved = False
    else:
        hasBlackKingMoved = False
        hasBlackLeftRookMoved = False
    board[((move[1]//8))*8] =  board[move[1]+1]
    board[move[1]+1] = -1
    updatePieceLocationMoved(board[move[1]+1], [move[1]+1, ((move[1]//8))*8])
def updatedPieceLocationCaptured(captured_piece,move):
    if isWhite(captured_piece):
        whitePiecesLocation.remove(move[1])
    elif isBlack(captured_piece):
        blackPiecesLocation.remove(move[1])
def updatePieceLocationMoved(piece, move):
    global whitePiecesLocation, blackPiecesLocation
    if isWhite(piece):
        whitePiecesLocation.remove(move[0])
        whitePiecesLocation.append(move[1])
    elif isBlack(piece):
        blackPiecesLocation.remove(move[0])
        blackPiecesLocation.append(move[1])
def restoreCapturePieceLocation(captured_piece, move):
    global whitePiecesLocation, blackPiecesLocation
    if isWhite(captured_piece):
        whitePiecesLocation.append(move[1])
    elif isBlack(captured_piece):
        blackPiecesLocation.append(move[1])
def restoreMovedPieceLocation(piece, move):
    global whitePiecesLocation, blackPiecesLocation
    if isWhite(piece):
        whitePiecesLocation.remove([move[1]])
        whitePiecesLocation.append(move[0])
    elif isBlack(piece):
        whitePiecesLocation.remove([move[1]])
        whitePiecesLocation.append(move[0])




PawnValue = 100
KnightValue = 320
BishopValue = 330
RookValue = 500
QueenValue = 900
KingValue = 20000

pawn_heatmap = [
    0,  0,  0,  0,  0,  0,  0,  0,
    50, 50, 50, 50, 50, 50, 50, 50,
    10, 10, 20, 30, 30, 20, 10, 10,
    5,  5, 10, 25, 25, 10,  5,  5,
    0,  0,  0, 20, 20,  0,  0,  0,
    5, -5,-10,  0,  0,-10, -5,  5,
    5, 10, 10,-20,-20, 10, 10,  5,
    0,  0,  0,  0,  0,  0,  0,  0
]

pawn_heatmap_opponent = [
    0,  0,  0,  0,  0,  0,  0,  0,
    5, 10, 10,-20,-20, 10, 10,  5,
    5, -5,-10,  0,  0,-10, -5,  5,
    0,  0,  0, 20, 20,  0,  0,  0,
    5,  5, 10, 25, 25, 10,  5,  5,
    10, 10, 20, 30, 30, 20, 10, 10,
    50, 50, 50, 50, 50, 50, 50, 50,
    0,  0,  0, 0, 0, 0, 0, 0

]

knight_heatmap = [
    -50, -40, -30, -30, -30, -30, -40, -50,
    -40, -20,  0,   0,   0,   0,  -20, -40,
    -30,  0,   10,  15,  15,  10,  0,  -30,
    -30,  5,   15,  20,  20,  15,  5,  -30,
    -30,  0,   15,  20,  20,  15,  0,  -30,
    -30,  5,   10,  15,  15,  10,  5,  -30,
    -40, -20,  0,   5,   5,   0,  -20, -40,
    -50, -40, -30, -30, -30, -30, -40, -50
]

knight_heatmap_opponent = [
    -50,-40,-30,-30,-30,-30,-40,-50,
    -40,-20,  0,  5,  5,  0,-20,-40,
    -30,  5, 10, 15, 15, 10,  5,-30,
    -30,  0, 15, 20, 20, 15,  0,-30,
    -30,  5, 15, 20, 20, 15,  5,-30,
    -30,  0, 10, 15, 15, 10,  0,-30,
    -40,-20,  0,  0,  0,  0,-20,-40,
    -50,-40,-40,-50,-50,-40,-40,-50
]

bishop_heatmap = [
    -20, -10, -10, -10, -10, -10, -10, -20,
    -10,   0,   0,   0,   0,   0,   0, -10,
    -10,   0,   5,  10,  10,   5,   0, -10,
    -10,   5,   5,  10,  10,   5,   5, -10,
    -10,   0,  10,  10,  10,  10,   0, -10,
    -10,  10,  10,  10,  10,  10,  10, -10,
    -10,   5,   0,   0,   0,   0,   5, -10,
    -20, -10, -10, -10, -10, -10, -10, -20
]

bishop_heatmap_opponent = [
    -20, -10, -10, -10, -10, -10, -10, -20,
    -10,   5,   0,   0,   0,   0,   5, -10,
    -10,  10,  10,  10,  10,  10,  10, -10,
    -10,   0,  10,  10,  10,  10,   0, -10,
    -10,   5,   5,  10,  10,   5,   5, -10,
    -10,   0,   5,  10,  10,   5,   0, -10,
    -10,   0,   0,   0,   0,   0,   0, -10,
    -20, -10, -10, -10, -10, -10, -10, -20
]

rook_heatmap = [
    0,  0,  0,  0,  0,  0,  0,  0,
    5, 10, 10, 10, 10, 10, 10,  5,
   -5,  0,  0,  0,  0,  0,  0, -5,
   -5,  0,  0,  0,  0,  0,  0, -5,
   -5,  0,  0,  0,  0,  0,  0, -5,
   -5,  0,  0,  0,  0,  0,  0, -5,
   -5,  0,  0,  0,  0,  0,  0, -5,
    0,  0,  0,  5,  5,  0,  0,  0
]

rook_heatmap_opponent = [
    0,  0,  0,  5,  5,  0,  0,  0,
   -5,  0,  0,  0,  0,  0,  0, -5,
   -5,  0,  0,  0,  0,  0,  0, -5,
   -5,  0,  0,  0,  0,  0,  0, -5,
   -5,  0,  0,  0,  0,  0,  0, -5,
   -5,  0,  0,  0,  0,  0,  0, -5,
    5, 10, 10, 10, 10, 10, 10,  5,
    0,  0,  0,  0,  0,  0,  0,  0
]

queen_heatmap = [
    -20,-10,-10, -5, -5,-10,-10,-20,
    -10,  0,  0,  0,  0,  0,  0,-10,
    -10,  0,  5,  5,  5,  5,  0,-10,
    -5,   0,  5,  5,  5,  5,  0, -5,
    0,    0,  5,  5,  5,  5,  0, -5,
    -10,  5,  5,  5,  5,  5,  0,-10,
    -10,  0,  5,  0,  0,  0,  0,-10,
    -20,-10,-10, -5, -5,-10,-10,-20
]
queen_heatmap_opponent = [-20, -10, -10, -5, -5, -10, -10, -20, -10, 0, 5, 0, 0, 0, 0, -10, -10, 5, 5, 5, 5, 5, 0, -10, 0, 0, 5, 5, 5, 5, 0, -5, -5, 0, 5, 5, 5, 5, 0, -5, -10, 0, 5, 5, 5, 5, 0, -10, -10, 0, 0, 0, 0, 0, 0, -10, -20, -10, -10, -5, -5, -10, -10, -20]

king_middlegame_heatmap = [
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -20, -30, -30, -40, -40, -30, -30, -20,
    -10, -20, -20, -20, -20, -20, -20, -10,
    20,  20,   0,   0,   0,   0,  20,  20,
    20,  30,  10,   0,   0,  10,  30,  20
]
king_middlegame_heatmap_opponent = [
    20,  30,  10,   0,   0,  10,  30,  20,
    20,  20,   0,   0,   0,   0,  20,  20,
   -10, -20, -20, -20, -20, -20, -20, -10,
   -20, -30, -30, -40, -40, -30, -30, -20,
   -30, -40, -40, -50, -50, -40, -40, -30,
   -30, -40, -40, -50, -50, -40, -40, -30,
   -30, -40, -40, -50, -50, -40, -40, -30,
   -30, -40, -40, -50, -50, -40, -40, -30
]

king_endgame_heatmap=[
    -50, -40, -30, -20, -20, -30, -40, -50,
    -30, -20, -10,   0,   0, -10, -20, -30,
    -30, -10,  20,  30,  30,  20, -10, -30,
    -30, -10,  30,  40,  40,  30, -10, -30,
    -30, -10,  30,  40,  40,  30, -10, -30,
    -30, -10,  20,  30,  30,  20, -10, -30,
    -30, -30,   0,   0,   0,   0, -30, -30,
    -50, -30, -30, -30, -30, -30, -30, -50
]
king_endgame_heatmap_opponent = [
    -50, -30, -30, -30, -30, -30, -30, -50,
    -30, -30,   0,   0,   0,   0, -30, -30,
    -30, -10,  20,  30,  30,  20, -10, -30,
    -30, -10,  30,  40,  40,  30, -10, -30,
    -30, -10,  30,  40,  40,  30, -10, -30,
    -30, -10,  20,  30,  30,  20, -10, -30,
    -30, -20, -10,   0,   0, -10, -20, -30,
    -50, -40, -30, -20, -20, -30, -40, -50
]

def displayGird(board):
    for row in range(8):
        for col in range(8):
            print(board[row*8+col], end = " ")
        print()

def evaluateBoard(board):
    eval = 0
    for location in range(64):
        if isBlack(board[location]):
            black_piece = board[location]
            if isKing(black_piece):
                eval-=(KingValue+king_middlegame_heatmap_opponent[location])
            elif isQueen(black_piece):
                eval-=(QueenValue+queen_heatmap_opponent[location])
            elif isPawn(black_piece):
                eval-=(PawnValue+pawn_heatmap_opponent[location])
            elif isBishop(black_piece):
                eval-=(BishopValue+bishop_heatmap_opponent[location])
            elif isKnight(black_piece):
                eval-=(KnightValue+knight_heatmap_opponent[location])
        elif isWhite(board[location]):
                white_piece = board[location]
                if isKing(white_piece):
                    eval+=(KingValue+king_middlegame_heatmap[location])
                elif isQueen(white_piece):
                    eval+=(QueenValue+queen_heatmap[location])
                elif isPawn(white_piece):
                    eval+=(PawnValue+pawn_heatmap[location])
                elif isBishop(white_piece):
                    eval+=(BishopValue+bishop_heatmap[location])
                elif isKnight(white_piece):
                    eval+=(KnightValue+knight_heatmap[location])
    return eval