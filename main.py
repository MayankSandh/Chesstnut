import pygame
import sys
import tkinter as tk
from utils import logic
from utils import graphics
from random import randint
from time import time
from copy import deepcopy
from utils import eval


# Constants

screen = pygame.display.set_mode((graphics.WIDTH, graphics.HEIGHT))
pygame.display.set_caption('Chess Board')

board = [-1]*64
# example_fen = '4QB2/1k6/1Np5/3p4/2p1PN2/2r1pP2/5P2/K2n3q w - - 0 1'
example_fen = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
# example_fen = '3qr2k/pbpp2pp/1p5N/3Q2b1/2P1P3/P7/1PP2PPP/R4RK1 w - - 0 1'
# example_fen = '8/8/8/8/8/8/8/5B2'
board = logic.readFen(example_fen)
# board[5] = logic.WhiteRook
# logic.displayGird(logic.whiteAttackSquares)
# board[9] = logic.WhitePawn

def printMyStats(board, index, prev_index):
    print("\n--------------------MADE MY MOVE ------------------------")
    print("piece_moved is: ", board[index])
    print("move played:", [prev_index, index])
    logic.displayGird(board)
    print("constants status:, ")
    logic.printConstants()
    print("----------------------------------------------------------")
def printCompStats(board, index, prev_index):
    print("\n--------------------COMPUTER MOVE ------------------------")
    print("piece_moved is: ", board[index])
    print("move played:", [prev_index, index])
    logic.displayGird(board)
    print("constants status:, ")
    logic.printConstants()
    print("----------------------------------------------------------")
def printStats(board):
    logic.displayGird(board)
    logic.printConstants()

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
                        # logic.printConstants()

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
                # printMyStats(board, index, prev_index)
                
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

def computerMakeMove(board, depth, currentTurn, og_depth, alpha, beta):
    if (depth == 0):
        return eval.evaluateBoard(board)
    bestMove = list()
    if currentTurn:
        bestEval = -100000
        # print("the moves calculated for depth:,", depth, "and currentTurn", currentTurn, "are:-")
        # print(logic.generateAllMoves(board, currentTurn))
        for move in logic.generateAllMoves(board, currentTurn):
            constants = deepcopy(logic.fetchConstants())
            # logic.printConstants()    
            piece = board[move[0]]
            # print("Board Stats before making move:", move, piece, "depth: ", depth)
            # printStats(board)
            capture, flag = logic.makeMove(board, move)
            # print("\nBoard Stats after making move:", move, piece, "depth: ", depth)
            # printStats(board)
            val = computerMakeMove(board, depth-1, (not currentTurn), og_depth, alpha, beta)
            if val > bestEval:
                bestMove = move
                bestEval = val
            logic.unmakeMove(board, move, capture, flag)
            logic.restoreConstants(constants)
            alpha = max(alpha, val)
            if beta<=alpha:
                break
            # print("\nBoard Stats after unmaking move:", move, piece, "depth: ", depth)
            # printStats(board)
    else:
        bestEval = 100000
        # print("the moves calculated for depth:,", depth, "and currentTurn", currentTurn, "are:-")
        # print(logic.generateAllMoves(board, currentTurn))
        for move in logic.generateAllMoves(board, currentTurn):
            constants = deepcopy(logic.fetchConstants())
            piece = board[move[0]]
            # print("Board Stats before making move:", move, piece, "depth: ", depth)
            # printStats(board)
            capture, flag = logic.makeMove(board, move)
            # print("\nBoard Stats after making move:", move, piece, "depth: ", depth)
            # printStats(board)
            val = computerMakeMove(board, depth-1, (not currentTurn), og_depth, alpha, beta)
            if val < bestEval:
                bestMove = move
                bestEval = val
            logic.unmakeMove(board, move, capture, flag)
            logic.restoreConstants(constants)
            beta = min(beta, val)
            if beta<=alpha:
                break
            # print("\nBoard Stats after unmaking move:", move, piece, "depth: ", depth)
            # printStats(board)
    if (depth == og_depth):
        return bestMove, bestEval
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
            depth = 3
            starttime = time()
            # print("before computer move")
            # logic.displayGird(board)
            # logic.printConstants()
            move, bestEval = computerMakeMove(board, depth, currentTurn, depth, -10000, 10000)
            # print(move,bestEval)
            # if (bestEval > 15000):
            #     graphics.show_winner(1)
            #     pygame.quit()
            #     sys.exit()
            # elif (bestEval < -15000):
            #     graphics.show_winner(0)
            #     pygame.quit()
            #     sys.exit()
            logic.makeMove(board, move)
            print("Time taken by computer:-", time()-starttime)
            graphics.generateBoard(board, screen)
            # printCompStats(board, move[1], move[0])
            if currentTurn:
                currentTurn = False
            else:
                currentTurn = True
    pygame.display.flip()

pygame.quit()
sys.exit()
