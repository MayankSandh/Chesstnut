import pygame
from operator import add
import time
from copy import deepcopy
import tkinter as tk

WIDTH, HEIGHT = 512, 512
SQUARE_SIZE = WIDTH // 8  # Size of each square
WIDTH = 512
# Colors (Green and Ivory)
GREEN = (118, 150, 86)
LIGHT_GREEN = (173, 255, 47)
# LIGHT_GREEN = (144, 216, 141)
DARK_GREEN = (50, 80, 30)
# LIGHT_GREEN = (144, 216, 141)
IVORY = (255, 247, 228)
LIGHT_IVORY = (210, 255, 0)
# LIGHT_IVORY = (255, 255, 255)
LIGHT_GREY = (200, 200, 200)
RED = (255, 0, 0)

def isWhite(piece_code):
    if piece_code//7 == 1:
        return True
    else:
        return False
def isPawn(piece_code):
    if piece_code%7 == 6:
        return True
    else:
        return False
def isKing(piece_code):
    if piece_code%7 == 1:
        return True
    else:
        return False

def drawSquare(board, index, screen):
    row = index//8
    col = index%8
    color = IVORY if (row + col) % 2 == 0 else GREEN
    pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
    
    piece_code = board[row*8+col]  # Reverse row iteration
    if piece_code != -1:
        # Construct the image path based on piece code (assuming filenames match piece codes)
        image_path = f'pieces_new/{piece_code}.png'
        try:
            piece_image = pygame.image.load(image_path)
            piece_image = pygame.transform.scale(piece_image, (SQUARE_SIZE, SQUARE_SIZE))
            screen.blit(piece_image, (col * SQUARE_SIZE, row * SQUARE_SIZE))
        except pygame.error as e:
            print(f"Error loading image '{image_path}': {e}")

def highlightSquare(board, index, screen):
    row = index//8
    col = index%8
    generateBoard(board, screen)
    color = LIGHT_IVORY if (row + col) % 2 == 0 else LIGHT_GREEN
    pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
    
    piece_code = board[row*8+col]  # Reverse row iteration
    if piece_code != -1:
        # Construct the image path based on piece code (assuming filenames match piece codes)
        image_path = f'pieces_new/{piece_code}.png'
        try:
            piece_image = pygame.image.load(image_path)
            piece_image = pygame.transform.scale(piece_image, (SQUARE_SIZE, SQUARE_SIZE))
            screen.blit(piece_image, (col * SQUARE_SIZE, row * SQUARE_SIZE))
        except pygame.error as e:
            print(f"Error loading image '{image_path}': {e}")

def drawFreeSquares(board, index, screen):
    row = index//8
    col = index%8
    if (board[row*8+col]//7 == -1):
        base_color = IVORY if (row + col) % 2 == 0 else GREEN
        pygame.draw.rect(screen, base_color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

        # Calculate the center coordinates of the square
        center_x = col * SQUARE_SIZE + SQUARE_SIZE // 2
        center_y = row * SQUARE_SIZE + SQUARE_SIZE // 2

        circle_radius = SQUARE_SIZE // 6  # Smaller radius for the circle
        darker_color = DARK_GREEN if base_color == GREEN else LIGHT_GREY
        
        pygame.draw.circle(screen, darker_color, (center_x, center_y), circle_radius)
        piece_code = board[row*8+col]  # Reverse row iteration
        if piece_code != -1:
            # Construct the image path based on piece code (assuming filenames match piece codes)
            image_path = f'pieces_new/{piece_code}.png'
            try:
                piece_image = pygame.image.load(image_path)
                piece_image = pygame.transform.scale(piece_image, (SQUARE_SIZE, SQUARE_SIZE))
                screen.blit(piece_image, (col * SQUARE_SIZE, row * SQUARE_SIZE))
            except pygame.error as e:
                print(f"Error loading image '{image_path}': {e}")

def drawCaptureSquare(board, index, screen):
    row, col = index//8, index%8
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

    piece_code = board[row*8+col]  # Reverse row iteration
    if piece_code != -1:
        # Construct the image path based on piece code (assuming filenames match piece codes)
        image_path = f'pieces_new/{piece_code}.png'
        try:
            piece_image = pygame.image.load(image_path)
            piece_image = pygame.transform.scale(piece_image, (SQUARE_SIZE, SQUARE_SIZE))
            screen.blit(piece_image, (col * SQUARE_SIZE, row * SQUARE_SIZE))
        except pygame.error as e:
            print(f"Error loading image '{image_path}': {e}")

def generateBoard(board, screen):
    for row in range(8):
        for col in range(8):
            drawSquare(board, 8*row + col, screen)

def makeMove(board, move): # also return the piece captured
    clicked_piece = board[move[0]]
    captured_piece = board[move[1]]
    board[move[1]] = clicked_piece
    board[move[0]] = -1
    piece = board[move[1]]

    #promotion handler
    if isPawn(piece) and ((move[1]//8 == 0) or (move[1]//8 == 7)):
        board[move[1]] = 7*(isWhite(piece))+2

    #castling handler
    if isKing(piece) and ((move[1]%8 - move[0]%8 == 2) or (move[1]%8 - move[0]%8 == -2)):
        if (move[1]%8 - move[0]%8 == 2):
            board[move[1]-1] = board[((move[1]//8)+1)*8 - 1]
            board[((move[1]//8)+1)*8 - 1] = -1
        else:
            board[move[1]+1] = board[((move[1]//8))*8]
            board[((move[1]//8))*8] = -1
    return captured_piece

def unmakeMove(board, move, captured_piece): # the move should be as it was made before and not like reverse the move or something
    clicked_piece = board[move[1]]
    board[move[0]] = clicked_piece
    board[move[1]] = captured_piece

def getSquareFromClick(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col