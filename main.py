import pygame
import sys
import tkinter as tk
from operator import add
from utils import logic
from utils import graphics
from copy import deepcopy\


import time

# Constants

screen = pygame.display.set_mode((graphics.WIDTH, graphics.HEIGHT))
pygame.display.set_caption('Chess Board')


# example_fen = '4QB2/1k6/1Np5/3p4/2p1PN2/2r1pP2/5P2/K2n3q w - - 0 1'
example_fen = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
board = logic.readFen(example_fen)

running = True
currentTurn = True
firstClick = 1
prev_row, prev_col = 0, 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        graphics.generateBoard(board, screen)

    pygame.display.flip()

pygame.quit()
sys.exit()