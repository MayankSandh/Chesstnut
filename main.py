import pygame
import sys

# Constants
WIDTH, HEIGHT = 512, 512
SQUARE_SIZE = WIDTH // 8  # Size of each square

# Colors (Green and Ivory)
GREEN = (118, 150, 86)
IVORY = (255, 247, 228)

# Create the Pygame window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Chess Board')

# Piece codes dictionary
piece_codes = {
    '1': 0,
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

# Function to create an integer array representing the chessboard based on FEN notation
def readFen(fen):
    board = [[0] * 8 for _ in range(8)]  # Initialize the chessboard with zeros

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

# Function to generate the chessboard using the integer array
def generateBoard(board):
    for row in range(8):
        for col in range(8):
            color = GREEN if (row + col) % 2 == 0 else IVORY
            pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            
            piece_code = board[7 - row][col]  # Reverse row iteration
            if piece_code != 0:
                # Construct the image path based on piece code (assuming filenames match piece codes)
                image_path = f'pieces_new/{piece_code}.png'
                try:
                    piece_image = pygame.image.load(image_path)
                    piece_image = pygame.transform.scale(piece_image, (SQUARE_SIZE, SQUARE_SIZE))
                    screen.blit(piece_image, (col * SQUARE_SIZE, row * SQUARE_SIZE))
                except pygame.error as e:
                    print(f"Error loading image '{image_path}': {e}")
def flipBoard(board):
    flipped_board = [row[::1] for row in board[::-1]]
    return flipped_board

# Example FEN string
example_fen = '3n4/8/5q2/1PP1P1Pp/1Ppk4/3prp2/bp6/3K4 w - - 0 1'

# Create the chessboard array based on FEN notation
chessboard = (readFen(example_fen))

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Generate the chessboard using the generated array
    generateBoard(chessboard)

    pygame.display.flip()

pygame.quit()
sys.exit()
