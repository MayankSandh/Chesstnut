import pygame
import sys
import tkinter as tk

# Constants
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
    
    return board

def pawnPromotion(board, row, col):
    root = tk.Tk()

    def button_click(board, row, col, num):
        board[row][col] = num+me*7 + 2
        root.destroy()
        

    root.title("Image Dialog")
    root.geometry("200x200")

    # Load images
    img_names = [f"pieces_new/{me*7+2}.png", f"pieces_new/{me*7+3}.png", f"pieces_new/{me*7+4}.png", f"pieces_new/{me*7+5}.png"]
    images = [tk.PhotoImage(file=img) for img in img_names]

    # Create buttons with images
    buttons = []
    for i in range(4):
        button = tk.Button(root, image=images[i], command=lambda idx=i: button_click(board, row, col, idx))
        button.grid(row=i // 2, column=i % 2, padx=10, pady=10)
        buttons.append(button)

    root.mainloop()
    
# Function to generate the chessboard using the integer array
def drawSquare(board, row, col, status):
    if (status == 2):
        pygame.draw.rect(screen, RED, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))  
    elif (status == 1):
        print("reached here")
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
    flipped_board = [row[::1] for row in board[::-1]]
    return flipped_board

# Function to get the square index based on mouse click
def getSquareFromClick(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

# Piece codes dictionary


me = 0

if (me):
    opponent = 0
else:
    opponent = 1

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


def showLegal(board, row, col):
    print("reached here show legal")
    generateBoard(board)
    if (board[row][col]//7 == me and board[row][col]%7 == 6):
        print("this is a pawn")
        direction = (me*-1,0)
        direction_attack = (me*-1,1), (me*-1,-1)
        for x,y in direction_attack:
            if (row+x)<8 and (row+x)>=0 and (col+y)<8 and (col+y)>=0:
                if board[row+x][col+y]//7 == opponent:
                    drawCaptureSquare(board, row+x,col+y)
        x,y = direction
        drawFreeSquares(board, row+x, col+y)
                    
            

    


def mouseClickHandler(board, firstClick, row, col, prev_row, prev_col):
    # if (board[row][col]//7 == me):
    if (firstClick):
        generateBoard(board)
        drawSquare(chessboard, row, col, 1)
        showLegal(board, row, col)
    else:
        if (board[row][col]//7 == me):
            print("clicked my piece again")
            mouseClickHandler(board, 1, row, col, prev_row, prev_col)
        else:
            clicked_piece = board[prev_row][prev_col]
            board[prev_row][prev_col] = -1
            board[row][col] = clicked_piece
            print("reached to this unholy place")
            print(board[row][col]%7,"    ", row)
            if (board[row][col]%7 == 6 and row == opponent*7):
                print("PAWN PROMOTION BEGINS!")
                pawnPromotion(board, row, col)
            generateBoard(board)
# else:
#     generateBoard(board)

# Example FEN string



# example_fen = 'N7/n2p1n2/3R4/Pp5p/1rPp4/3p3k/8/r3RK2 w - - 0 1'
example_fen = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'

# Create the chessboard array based on FEN notation
chessboard = readFen(example_fen)
print(chessboard)
# Main loop
running = True
generateBoard(chessboard)

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
                    if (chessboard[row][col]//7 != me):
                        continue
                    prev_row, prev_col = row, col
                    mouseClickHandler(chessboard, firstClick, row, col, prev_row, prev_col)
                    clickedPiece = chessboard[row][col]
                    print("first click occurs")
                    firstClick = 0

                else:
                    mouseClickHandler(chessboard, firstClick, row, col, prev_row, prev_col)
                    print("second click occurs")
                    firstClick = 1
                # Get the mouse click coordinates and square
                # print(f"Mouse clicked at square: {clicked_square}")
                

    # Generate the chessboard using the generated array

    # Highlight the clicked square (if exists)
    if 'clicked_square' in locals():
        row, col = clicked_square
        # pygame.draw.rect(screen, RED, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
        # drawSquare(chessboard, row, col, 1)
    
    pygame.display.flip()

pygame.quit()
sys.exit()
