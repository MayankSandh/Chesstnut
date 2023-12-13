import pygame
import sys
import tkinter as tk
from utils import logic
from utils import graphics
from random import randint


# Constants

screen = pygame.display.set_mode((graphics.WIDTH, graphics.HEIGHT))
pygame.display.set_caption('Chess Board')

board = [-1]*64
# example_fen = '4QB2/1k6/1Np5/3p4/2p1PN2/2r1pP2/5P2/K2n3q w - - 0 1'
example_fen = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
board = logic.readFen(example_fen)
# board[9] = logic.WhitePawn

def displayGird(board):
    for row in range(8):
        for col in range(8):
            print(board[row*8+col], end = " ")
        print()

    
def mouseClickHandler(board, firstclick, index, prev_index):
    if firstclick:
        graphics.highlightSquare(board,index,screen)
        if board[index]//7 == currentTurn:
            for move in logic.legalMoves(board, index, currentTurn):
                if board[move[1]]//7 == (not currentTurn):
                    graphics.drawCaptureSquare(board, move[1], screen)
                else:
                    graphics.drawFreeSquares(board, move[1], screen)
    else:
        if board[index]//7 == currentTurn:
            mouseClickHandler(board, True, index, prev_index)
        else:
            if [prev_index, index] in logic.legalMoves(board, prev_index, currentTurn):
                graphics.makeMove(board, [prev_index, index])
                graphics.generateBoard(board, screen)

                # castling constants handler
                if logic.isKing(board[index]):
                    logic.changeKingStatus(board[index])
                    if logic.isKing(board[index]) and ((index%8 -prev_index%8 == 2) or (index%8 -prev_index%8 == -2)):
                        if (index%8 - move[0]%8 == 2):
                            logic.changeRightRookStatus(board[index])
                        else:
                            logic.changeLeftRookStatus(board[index])

                #rook constant handler
                if logic.isRook(board[index]):
                    logic.changeRookStatus(board[index], prev_index)

                if currentTurn:
                    return False
                else:
                    return True
            else:
                graphics.generateBoard(board, screen)
                if currentTurn:
                    return True
                else:
                    return False

def computerMakeMove(board, currentTurn):
    moves = logic.generateAllMoves(board, currentTurn)
    return moves[randint(0, len(moves)-1)]

graphics.generateBoard(board, screen)
running = True
currentTurn = True
firstclick = 1
prev_index = 0
firstclick = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if not (currentTurn ^ logic.ME):
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    clicked_pos = graphics.getSquareFromClick(pygame.mouse.get_pos())
                    row, col = clicked_pos
                    index = row*8+col
                    if firstclick:
                        if board[index]//7 != currentTurn:
                            continue
                        prev_index = index
                        mouseClickHandler(board, firstclick, index, prev_index)
                        firstclick = False
                        
                    else:
                        if board[index]//7 == currentTurn:
                            prev_index = index
                            mouseClickHandler(board, firstclick, index, prev_index)
                            continue
                        currentTurn = mouseClickHandler(board, firstclick, index, prev_index)
                        firstclick = True
        else:
            move = computerMakeMove(board, currentTurn)
            graphics.makeMove(board, move)
            graphics.generateBoard(board, screen)
            if currentTurn:
                currentTurn = False
            else:
                currentTurn = True
    pygame.display.flip()

pygame.quit()
sys.exit()