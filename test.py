import pygame
import sys
import tkinter as tk
from operator import add

# Constants
ME = 1

WIDTH, HEIGHT = 512, 512
SQUARE_SIZE = WIDTH // 8  # Size of each square

# Colors (Green and Ivory)
GREEN = (118, 150, 86)
LIGHT_GREEN = (144, 216, 141)
DARK_GREEN = (50, 80, 30)
# LIGHT_GREEN = (144, 216, 141)
IVORY = (255, 247, 228)
LIGHT_IVORY = (255, 255, 255)
LIGHT_GREY = (200, 200, 200)

# Create the Pygame window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Chess Board')

# Function to create an integer array representing the chessboard based on FEN notation
def readFen(fen):
    board = [[-1] * 8 for _ in range(8)]  # Initialize the chessboard with zeros

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
            board[rank_index][file_index] = piece_code
            file_index += 1
        else:
            continue  # Ignore unexpected characters
    if (not ME):
        board = flipBoard(board)
    return board

def pawnPromotion(board, row, col):
    root = tk.Tk()

    def button_click(board, row, col, num):
        board[row][col] = num+ME*7 + 2
        root.destroy()
        

    root.title("Choose Your Promotion!")
    root.geometry("300x300")

    # Load images
    img_names = [f"pieces_new/{ME*7+2}.png", f"pieces_new/{ME*7+3}.png", f"pieces_new/{ME*7+4}.png", f"pieces_new/{ME*7+5}.png"]
    images = [tk.PhotoImage(file=img) for img in img_names]

    # Create buttons with images
    buttons = []
    for i in range(4):
        button = tk.Button(root, image=images[i], command=lambda idx=i: button_click(board, row, col, idx),width=120, height=120)
        button.grid(row=i // 2, column=i % 2, padx=10, pady=10)
        buttons.append(button)
    board[row][col] = ME*7 + 2
    root.mainloop()
    
# Function to generate the chessboard using the integer array
def drawSquare(board, row, col, status):
    if (status == 1):
        color = LIGHT_IVORY if (row + col) % 2 == 0 else LIGHT_GREEN
        pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
        
        piece_code = board[row][col]  # Reverse row iteration
        if piece_code != -1:
            # Construct the image path based on piece code (assuming filenames match piece codes)
            image_path = f'pieces_new/{piece_code}.png'
            try:
                piece_image = pygame.image.load(image_path)
                piece_image = pygame.transform.scale(piece_image, (SQUARE_SIZE, SQUARE_SIZE))
                screen.blit(piece_image, (col * SQUARE_SIZE, row * SQUARE_SIZE))
            except pygame.error as e:
                print(f"Error loading image '{image_path}': {e}")
    
    else:
        color = IVORY if (row + col) % 2 == 0 else GREEN
        pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
        
        piece_code = board[row][col]  # Reverse row iteration
        if piece_code != -1:
            # Construct the image path based on piece code (assuming filenames match piece codes)
            image_path = f'pieces_new/{piece_code}.png'
            try:
                piece_image = pygame.image.load(image_path)
                piece_image = pygame.transform.scale(piece_image, (SQUARE_SIZE, SQUARE_SIZE))
                screen.blit(piece_image, (col * SQUARE_SIZE, row * SQUARE_SIZE))
            except pygame.error as e:
                print(f"Error loading image '{image_path}': {e}")

def generateBoard(board):
    for row in range(8):
        for col in range(8):
            drawSquare(board, row, col, 0)

# Function to flip the chessboard
def flipBoard(board):
    flipped_board = [row[::-1] for row in board[::-1]]
    return flipped_board

# Function to get the square index based on mouse click
def getSquareFromClick(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

# Piece codes dictionary


if (ME):
    OPP = 0
else:
    OPP = 1

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
def drawCaptureSquare(board, row, col):
    base_color = IVORY if (row + col) % 2 == 0 else GREEN
    pygame.draw.rect(screen, base_color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    # Calculate the center coordinates of the square
    center_x = col * SQUARE_SIZE + SQUARE_SIZE // 2
    center_y = row * SQUARE_SIZE + SQUARE_SIZE // 2

    circle_radius = SQUARE_SIZE // 2.0 # Further increased radius for the hollow circle
    border_width = 5  # Increased width of the border for the hollow circle
    darker_color = DARK_GREEN if base_color == GREEN else LIGHT_GREY
    
    # Draw hollow circle
    pygame.draw.circle(screen, darker_color, (center_x, center_y), circle_radius, border_width)

    piece_code = board[row][col]  # Reverse row iteration
    if piece_code != -1:
        # Construct the image path based on piece code (assuming filenames match piece codes)
        image_path = f'pieces_new/{piece_code}.png'
        try:
            piece_image = pygame.image.load(image_path)
            piece_image = pygame.transform.scale(piece_image, (SQUARE_SIZE, SQUARE_SIZE))
            screen.blit(piece_image, (col * SQUARE_SIZE, row * SQUARE_SIZE))
        except pygame.error as e:
            print(f"Error loading image '{image_path}': {e}")
def drawFreeSquares(board, row, col):
    if (board[row][col]//7 == -1):
        base_color = IVORY if (row + col) % 2 == 0 else GREEN
        pygame.draw.rect(screen, base_color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

        # Calculate the center coordinates of the square
        center_x = col * SQUARE_SIZE + SQUARE_SIZE // 2
        center_y = row * SQUARE_SIZE + SQUARE_SIZE // 2

        circle_radius = SQUARE_SIZE // 6  # Smaller radius for the circle
        darker_color = DARK_GREEN if base_color == GREEN else LIGHT_GREY
        
        pygame.draw.circle(screen, darker_color, (center_x, center_y), circle_radius)
        piece_code = board[row][col]  # Reverse row iteration
        if piece_code != -1:
            # Construct the image path based on piece code (assuming filenames match piece codes)
            image_path = f'pieces_new/{piece_code}.png'
            try:
                piece_image = pygame.image.load(image_path)
                piece_image = pygame.transform.scale(piece_image, (SQUARE_SIZE, SQUARE_SIZE))
                screen.blit(piece_image, (col * SQUARE_SIZE, row * SQUARE_SIZE))
            except pygame.error as e:
                print(f"Error loading image '{image_path}': {e}")
def isValid(board, pos, legal_moves, og_row, og_col):
    row, col = pos
    if row == og_row and col == og_col:
        return True
    if (row)<8 and (row)>=0 and (col)<8 and (col)>=0:
        if board[row][col]//7 == OPP:
            legal_moves.append([row, col])
            return False        
        if board[row][col]//7 == ME:
            return False
        return True
        
    else:
        return False
def LegalSqaures(board, row, col):
    legal_moves = list()
    if board[row][col]//7 == ME:
        if board[row][col]%7 == 5: # BISHOP MOVIES
            directions = ((1,1), (1,-1), (-1,1), (-1,-1))
            for d in directions:
                pos = [row, col]
                while isValid(board, pos, legal_moves, row, col):
                    print("reached bishop")
                    legal_moves.append(pos)
                    pos = list((map(add, pos, d)))
            print(legal_moves)

        elif board[row][col]%7 == 6: # PAWN MOVES
            direction = ((-1,0), (-2, 0))
            direction_attack = (-1,1), (-1,-1)
            for x,y in direction_attack:
                if (row+x)<8 and (row+x)>=0 and (col+y)<8 and (col+y)>=0:
                    if board[row+x][col+y]//7 == OPP:
                        legal_moves.append([row+x, col+y])
                        # drawCaptureSquare(board, row+x,col+y)

            x,y = direction[0]
            if board[x+row][y+col]==-1:
                legal_moves.append([row+x, col+y])
            x,y = direction[1]
            if board[x+row][y+col]==-1 and row == 6:
                legal_moves.append([row+x, col+y])
        elif board[row][col]%7 == 3: # ROOK MOVIES
            directions = ((0,1), (0,-1), (-1,0), (1,0))
            for d in directions:
                pos = [row, col]
                while isValid(board, pos, legal_moves, row, col):
                    legal_moves.append(pos)
                    pos = list((map(add, pos, d)))
            print(legal_moves)

        elif board[row][col]%7 == 2: #  QUEEN MOVIES
            directions = ((0,1), (0,-1), (-1,0), (1,0))
            for d in directions:
                pos = [row, col]
                while isValid(board, pos, legal_moves, row, col):
                    legal_moves.append(pos)
                    pos = list((map(add, pos, d)))
            directions = ((1,1), (1,-1), (-1,1), (-1,-1))
            for d in directions:
                pos = [row, col]
                while isValid(board, pos, legal_moves, row, col):
                    print("reached bishop")
                    legal_moves.append(pos)
                    pos = list((map(add, pos, d)))
        elif board[row][col]%7 == 1: # KING MOVES
            direction = ((0,1), (0,-1), (-1,0), (1,-0), (1,1), (1,-1), (-1,1), (-1,-1))
            for x,y in direction:
                if (row+x)<8 and (row+x)>=0 and (col+y)<8 and (col+y)>=0:
                    if isValid(board, [row+x, col+y], legal_moves, row, col):
                        legal_moves.append([row+x, col+y])
                        # drawCaptureSquare(board, row+x,col+y)
        elif board[row][col]%7 == 4: # KNIGHT MOVES
            direction = ((2,1), (2,-1), (-1,2), (1,2),(-2,1), (-2,-1), (-1,-2), (1,-2))
            for x,y in direction:
                if (row+x)<8 and (row+x)>=0 and (col+y)<8 and (col+y)>=0:
                    if isValid(board, [row+x, col+y], legal_moves, row, col):
                        legal_moves.append([row+x, col+y])
                        # drawCaptureSquare(board, row+x,col+y)

    return legal_moves
            # drawFreeSquares(board, row+x, col+y)
def showLegal(board, row, col):
    legal_moves = LegalSqaures(board, row, col)
    for x in legal_moves:
        if board[x[0]][x[1]]//7 != OPP:
            print("reached free: ", x[0], x[1])
            drawFreeSquares(board, x[0], x[1])
        elif board:
            print("reached opp: ", x[0], x[1])
            drawCaptureSquare(board, x[0], x[1])
                  
def mouseClickHandler(board, firstClick, row, col, prev_row, prev_col):
    # if (board[row][col]//7 == ME):
    if (firstClick):
        generateBoard(board)
        drawSquare(chessboard, row, col, 1)
        print(row, col)
        showLegal(board, row, col)
    else:
        if (board[row][col]//7 == ME):
            mouseClickHandler(board, 1, row, col, prev_row, prev_col)
        else:          
            if [row, col] in LegalSqaures(board, prev_row, prev_col):
                clicked_piece = board[prev_row][prev_col]
                board[prev_row][prev_col] = -1
                board[row][col] = clicked_piece
                if (board[row][col]%7 == 6 and row == 0):
                    pawnPromotion(board, row, col)
                generateBoard(board)
            else:
                generateBoard(board)




# example_fen = '4QB2/1k6/1Np5/3p4/2p1PN2/2r1pP2/5P2/K2n3q w - - 0 1'
example_fen = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
chessboard = readFen(example_fen)
generateBoard(chessboard)






# Main loop
running = True
firstClick = 1
clickedPiece = 0
prev_row, prev_col = 0, 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Check for left mouse button click
                click_pos = pygame.mouse.get_pos()
                clicked_square = getSquareFromClick(click_pos)
                row, col = clicked_square

                if (firstClick == 1):
                    if (chessboard[row][col]//7 != ME):
                        continue
                    prev_row, prev_col = row, col
                    mouseClickHandler(chessboard, firstClick, row, col, prev_row, prev_col)
                    clickedPiece = chessboard[row][col]
                    firstClick = 0

                else:
                    mouseClickHandler(chessboard, firstClick, row, col, prev_row, prev_col)
                    firstClick = 1

    pygame.display.flip()

pygame.quit()
sys.exit()
