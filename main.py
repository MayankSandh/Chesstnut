import pygame
import sys
import tkinter as tk
from utils import logic
from utils import graphics
from random import randint
from time import time
from copy import deepcopy

# Constants

screen = pygame.display.set_mode((graphics.WIDTH, graphics.HEIGHT))
pygame.display.set_caption('Chess Board')

board = [-1]*64
# example_fen = '4QB2/1k6/1Np5/3p4/2p1PN2/2r1pP2/5P2/K2n3q w - - 0 1'
example_fen = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
board = logic.readFen(example_fen)
# board[9] = logic.WhitePawn
    
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
            print("========================MY MOVE==================================")
            print("========================MY MOVE==================================")
            print("========================MY MOVE==================================")
            print("========================MY MOVE==================================")
            print("========================MY MOVE==================================")
            print("========================MY MOVE==================================")
            if [prev_index, index] in logic.legalMoves(board, prev_index, currentTurn):
                captured_piece, flag = logic.makeMove(board, [prev_index, index])
                graphics.generateBoard(board, screen)

                # castling constants handler
                if logic.isKing(board[index]):
                    logic.changeKingStatus(board[index])
                    if logic.isKing(board[index]) and ((index%8 -prev_index%8 == 2) or (index%8 -prev_index%8 == -2)):
                        if (index%8 - prev_index%8 == 2):
                            logic.changeRightRookStatus(board[index])
                        else:
                            logic.changeLeftRookStatus(board[index])
                        logic.printConstants()

                #rook constant handler
                if logic.isRook(board[index]):
                    logic.changeRookStatus(board[index], prev_index)

                # rook capture handler  # can be written more efficiently
                if logic.isRook(captured_piece):
                    if currentTurn:
                        if not (logic.hasBlackLeftRookMoved and logic.hasBlackRightRookMoved):
                            if index//8 == (0+7*logic.OPP): # the captured rook is not the unmoved one
                                if index%8 == 0 and not logic.hasBlackLeftRookMoved:
                                    logic.changeLeftRookStatus(captured_piece)
                                elif index%8 == 7 and not logic.hasBlackRightRookMoved:
                                    logic.changeRightRookStatus(captured_piece)
                    else:
                        if not (logic.hasWhiteLeftRookMoved and logic.hasWhiteRightRookMoved):
                            if index//8 == ((7-7*logic.OPP)): # the captured rook is not the unmoved one
                                if index%8 == 0 and not logic.hasWhiteLeftRookMoved:
                                    logic.changeLeftRookStatus(captured_piece)
                                elif index%8 == 7 and not logic.hasWhiteRightRookMoved:
                                    logic.changeRightRookStatus(captured_piece)

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

def computerMakeMove(board, depth, currentTurn, og_depth):
    if (depth == 0):
        return logic.evaluateBoard(board)
    bestMove = list()
    if currentTurn:
        bestEval = -1000000
        for move in logic.generateAllMoves(board, currentTurn):
            constants = deepcopy(logic.fetchConstants())
            logic.printConstants()
            print("made move")
            capture, flag = logic.makeMove(board, move)
            val = computerMakeMove(board, depth-1, (not currentTurn), og_depth)
            if val > bestEval:
                bestMove = move
                bestEval = val
            logic.unmakeMove(board, move, capture, flag)
            print("unmake move")
            print("the constants, i stored",constants)
            logic.restoreConstants(constants)
            logic.printConstants()
            print()
    else:
        bestEval = 1000000
        for move in logic.generateAllMoves(board, currentTurn):
            constants = deepcopy(logic.fetchConstants())
            logic.printConstants()
            print("made move")
            capture, flag = logic.makeMove(board, move)
            val = computerMakeMove(board, depth-1, (not currentTurn), og_depth)
            if val < bestEval:
                bestMove = move
                bestEval = val
            logic.unmakeMove(board, move, capture, flag)
            print("unmake move")
            print("the constants, i stored",constants)
            logic.restoreConstants(constants)
            logic.printConstants()
    if (depth == og_depth):
        return bestMove
    else:
        return bestEval


graphics.generateBoard(board, screen)
running = True
currentTurn = True
firstclick = 1
prev_index = 0
firstclick = True
starttime = time()

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
            depth = 2
            move = computerMakeMove(board, depth, currentTurn, depth)
            logic.makeMove(board, move)
            graphics.generateBoard(board, screen)
            if currentTurn:
                currentTurn = False
            else:
                currentTurn = True
    pygame.display.flip()

# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         if not (currentTurn ^ logic.ME):
#             # if event.type == pygame.MOUSEBUTTONDOWN:
#             #     if event.button == 1:
#             #         clicked_pos = graphics.getSquareFromClick(pygame.mouse.get_pos())
#             #         row, col = clicked_pos
#             #         index = row*8+col
#             #         if firstclick:
#             #             if board[index]//7 != currentTurn:
#             #                 continue
#             #             prev_index = index
#             #             mouseClickHandler(board, firstclick, index, prev_index)
#             #             firstclick = False
                        
#             #         else:
#             #             if board[index]//7 == currentTurn:
#             #                 prev_index = index
#             #                 mouseClickHandler(board, firstclick, index, prev_index)
#             #                 continue
#             #             currentTurn = mouseClickHandler(board, firstclick, index, prev_index)
#             #             firstclick = True
#             if time() - starttime >0.5:
#                 move = computerMakeMove(board, currentTurn)
#                 logic.makeMove(board, move)
#                 graphics.generateBoard(board, screen)
                
#                 if currentTurn:
#                     currentTurn = False
#                 else:
#                     currentTurn = True
#                 starttime = time()
#         else:
#             if time() - starttime >0.5:
#                 move = computerMakeMove(board, currentTurn)
#                 logic.makeMove(board, move)
#                 graphics.generateBoard(board, screen)
                
#                 if currentTurn:
#                     currentTurn = False
#                 else:
#                     currentTurn = True
#                 starttime = time()
#     pygame.display.flip()

pygame.quit()
sys.exit()