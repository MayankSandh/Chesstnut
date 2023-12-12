import pygame
import sys
import tkinter as tk
from operator import add
from utils import graphics
from copy import deepcopy\


import time

# Constants

screen = pygame.display.set_mode((graphics.WIDTH, graphics.HEIGHT))
pygame.display.set_caption('Chess Board')

def getSquareFromClick(pos):
    x, y = pos
    row = y // graphics.SQUARE_SIZE
    col = x // graphics.SQUARE_SIZE
    return row, col

board = [-1]*64

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