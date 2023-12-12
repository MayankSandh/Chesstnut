import pygame
from operator import add
import time
# from computer import isKingUnderCheck, makeMove
from copy import deepcopy
import tkinter as tk
ME = 1
if (ME):
    OPP = 0
else:
    OPP = 1

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

def drawSquare(board, index, screen):
    row = index//8
    col = index%8
    color = IVORY if (row + col) % 2 == 0 else GREEN
    pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
    
    # piece_code = board[row][col]  # Reverse row iteration
    # if piece_code != -1:
    #     # Construct the image path based on piece code (assuming filenames match piece codes)
    #     image_path = f'pieces_new/{piece_code}.png'
    #     try:
    #         piece_image = pygame.image.load(image_path)
    #         piece_image = pygame.transform.scale(piece_image, (SQUARE_SIZE, SQUARE_SIZE))
    #         screen.blit(piece_image, (col * SQUARE_SIZE, row * SQUARE_SIZE))
    #     except pygame.error as e:
    #         print(f"Error loading image '{image_path}': {e}")
def generateBoard(board, screen):
    for row in range(8):
        for col in range(8):
            drawSquare(board, 8*row + col, screen)