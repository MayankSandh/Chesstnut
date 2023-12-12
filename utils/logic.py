ME = 1
if ME:
    OPP = 0
else:
    OPP = 1

currentTurn = True

lastMoveOfBlack = [0, 0]
lastMoveOfWhite = [0, 0]


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
    if piece_code//7 == 0:
        return False
    else:
        return True

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
        print(isBishop(piece_code), isQueen(piece_code), isRook(piece_code))
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

def generateMoves(board, currentTurn):
    allMovesList = list()
    for startSquare in range(64):
        piece = board[startSquare]
        if (piece)//7 == currentTurn:
            if isSlidingPiece(piece):
                allMovesList.append(generateSlidingMoves(board, startSquare, currentTurn))
            if isKnight(piece):
                allMovesList.append(generateKnightMoves(board, startSquare, currentTurn))
            if isPawn(piece):
                allMovesList.append(generatePawnMoves(board, startSquare, currentTurn))
            if isKing(piece):
                allMovesList.append(generateKingMoves(board, startSquare, currentTurn))

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
    print(move_list)
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
            print("my white pawn detected")
            directions = [-8, -16]
            if row == 6:
                if board[directions[1]+index]//7 == -1:
                    move_list.append([index, directions[1]+index])
            if board[directions[0]+index]//7 == -1:
                move_list.append([index, directions[0]+index])
            print(move_list)
            directionsAttack = [-7, -9]
            for direction in directionsAttack:
                targetSquare = index+direction
                if squareWithinBounds(index, direction):
                    if targetSquare//7 == (not currentTurn):
                        move_list.append([index, targetSquare])
                    
        else:
            directions = [8, 16]
            if row == 1:
                if board[directions[1]+index]//7 == -1:
                    move_list.append([index, directions[1]+index])
            if board[directions[0]+index]//7 == -1:
                move_list.append([index, directions[0]+index])
            directionsAttack = [7, 9]
            for direction in directionsAttack:
                targetSquare = index+direction
                if squareWithinBounds(index, direction):
                    if targetSquare//7 == (not currentTurn):
                        move_list.append([index, targetSquare])
    else:
        if isBlack(piece):
            directions = [-8, -16]
            if row == 6:
                if board[directions[1]+index]//7 == -1:
                    move_list.append([index, directions[1]+index])
            if board[directions[0]+index]//7 == -1:
                move_list.append([index, directions[0]+index])
            directionsAttack = [-7, -9]
            for direction in directionsAttack:
                targetSquare = index+direction
                if squareWithinBounds(index, direction):
                    if targetSquare//7 == (not currentTurn):
                        move_list.append([index, targetSquare])
        else:
            directions = [8, 16]
            if row == 1:
                if board[directions[1]+index]//7 == -1:
                    move_list.append([index, directions[1]+index])
            if board[directions[0]+index]//7 == -1:
                move_list.append([index, directions[0]+index])
            directionsAttack = [7, 9]
            for direction in directionsAttack:
                targetSquare = index+direction
                if squareWithinBounds(index, direction):
                    if targetSquare//7 == (not currentTurn):
                        move_list.append([index, targetSquare])
    return move_list

def generateKingMoves(board, index, currentTurn):
    move_list = list()
    for direction in DirectionOffsets:
        if squareWithinBounds(index, direction):
            targetSquare = index+direction
            if targetSquare//7 == currentTurn:
                continue
            if isKingSafe(targetSquare, currentTurn):
                move_list.append([index, targetSquare])
    return move_list


    

