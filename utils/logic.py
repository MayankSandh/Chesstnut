ME = 0
if ME:
    OPP = 0
else:
    OPP = 1

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
        False
def isQueen(piece_code):
    if piece_code%7 == 2:
        return True
    else:
        False
def isRook(piece_code):
    if piece_code%7 == 3:
        return True
    else:
        False
def isKnight(piece_code):
    if piece_code%7 == 4:
        return True
    else:
        False
def isBishop(piece_code):
    if piece_code%7 == 5:
        return True
    else:
        False
def isPawn(piece_code):

    if piece_code%7 == 5:
        return True
    else:
        False

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

    rank_index = 0  # Start from index 0 to properly populate the board
    file_index = 0
    for char in fen:
        if char.isdigit():
            file_index += int(char)
        elif char == '/':
            rank_index += 1
            file_index = 0
        elif char in piece_codes:
            piece_code = piece_codes[char]
            board[rank_index*8+file_index] = piece_code
            file_index += 1
        else:
            continue  # Ignore unexpected characters
    if (not ME):
        board = board[::-1]
    return board

