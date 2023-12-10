import pygame
import sys
import tkinter as tk
from operator import add
import graphics
from copy import deepcopy
from time import sleep
import computer
import time

# Constants

screen = pygame.display.set_mode((graphics.WIDTH, graphics.HEIGHT))
pygame.display.set_caption('Chess Board')

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
    if (not graphics.ME):
        board = flipBoard(board)
    return board

def pawnPromotion(board, row, col):
    root = tk.Tk()

    def button_click(board, row, col, num):
        board[row][col] = num+graphics.ME*7 + 2
        root.destroy()
        

    root.title("Choose Your Promotion!")
    root.geometry("300x300")

    # Load images
    img_names = [f"pieces_new/{graphics.ME*7+2}.png", f"pieces_new/{graphics.ME*7+3}.png", f"pieces_new/{graphics.ME*7+4}.png", f"pieces_new/{graphics.ME*7+5}.png"]
    images = [tk.PhotoImage(file=img) for img in img_names]

    # Create buttons with images
    buttons = []
    for i in range(4):
        button = tk.Button(root, image=images[i], command=lambda idx=i: button_click(board, row, col, idx),width=120, height=120)
        button.grid(row=i // 2, column=i % 2, padx=10, pady=10)
        buttons.append(button)
    board[row][col] = graphics.ME*7 + 2
    root.mainloop()

def flipBoard(board):
    flipped_board = [row[::-1] for row in board[::-1]]
    return flipped_board

def getSquareFromClick(pos):
    x, y = pos
    row = y // graphics.SQUARE_SIZE
    col = x // graphics.SQUARE_SIZE
    return row, col

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



            # drawFreeSquares(board, row+x, col+y)                 

def makeMove(board, row, col, prev_row, prev_col):
    clicked_piece = board[prev_row][prev_col]
    board[prev_row][prev_col] = -1
    board[row][col] = clicked_piece

def mouseClickHandler(board, firstClick, row, col, prev_row, prev_col, currentTurn):
    # if (board[row][col]//7 == graphics.ME):
    if (firstClick):
        graphics.generateBoard(board, screen)
        graphics.drawSquare(chessboard, row, col, 1, screen)
        graphics.showLegal(board, row, col, currentTurn, screen)
    else:
        if (board[row][col]//7 == currentTurn):
            mouseClickHandler(board, 1, row, col, prev_row, prev_col, currentTurn)
        else:          
            if [row, col] in graphics.LegalSquares(board, prev_row, prev_col, currentTurn):
                makeMove(board, row, col, prev_row, prev_col)
                if (board[row][col]%7 == 6 and (row == 0 or row == 7)):
                    pawnPromotion(board, row, col)
                graphics.generateBoard(board, screen)
                if currentTurn:
                    return False
                else:
                    return True
            else:
                graphics.generateBoard(board, screen) # waste generation
    return currentTurn

# example_fen = '4QB2/1k6/1Np5/3p4/2p1PN2/2r1pP2/5P2/K2n3q w - - 0 1'
example_fen = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
chessboard = readFen(example_fen)
graphics.generateBoard(chessboard, screen)


def computerMove(board, opp):
    move_list = list()
    for row in range(8):
        for col in range(8):
            if board[row][col] // 7 == opp:
                for move in graphics.LegalSquares(board, row, col, currentTurn):
                    move_list.append([move[0], move[1], row, col])
    new_board = deepcopy(board)
    if opp == 1:
        bestEval = -999999
    else:
        bestEval = 999999
    for move in move_list:
        makeMove(new_board, move[0], move[1], move[2], move[3])
        # displayGird(new_board, depth, currentTurn, move, board)
        if opp == 0:
            if computer.evaluateBoard(new_board)<=bestEval:
                bestEval = computer.evaluateBoard(new_board)
                bestMove = move
        else:
            if computer.evaluateBoard(new_board)>=bestEval:
                bestMove = move
                bestEval = computer.evaluateBoard(new_board)
        new_board = deepcopy(board)
    makeMove(new_board, bestMove[0], bestMove[1], bestMove[2], bestMove[3])
    graphics.generateBoard(new_board, screen)
    print("Current Evaluation: ",computer.evaluateBoard(new_board))
    return new_board
    








def moveGenerationTest(board, depth, currentTurn, move, prev_board):
    new_board = deepcopy(board)
    # displayGird(new_board, depth, currentTurn, move, prev_board)

    if (depth == 0):
        return 1
    
    move_list = list()
    for row in range(8):
        for col in range(8):
            if board[row][col] // 7 == currentTurn:
                for move in graphics.LegalSquares(board, row, col, currentTurn):
                    move_list.append([move[0], move[1], row, col])
    positions = 0
    if currentTurn:
        nextTurn = False
    else:
        nextTurn = True

    for move in move_list:
        makeMove(new_board, move[0], move[1], move[2], move[3])
        # displayGird(new_board, depth, currentTurn, move, board)
        positions+=moveGenerationTest(new_board, depth-1, nextTurn, move, board)
        new_board = deepcopy(board)
    return positions

    


# Main loop
running = True
currentTurn = True
firstClick = 1
prev_row, prev_col = 0, 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if not (currentTurn ^ graphics.ME):
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Check for left mouse button click
                    click_pos = pygame.mouse.get_pos()
                    clicked_square = getSquareFromClick(click_pos)
                    row, col = clicked_square

                    if (firstClick == 1):
                        if (chessboard[row][col]//7 != currentTurn):
                            continue
                        prev_row, prev_col = row, col
                        mouseClickHandler(chessboard, firstClick, row, col, prev_row, prev_col, currentTurn)
                        firstClick = 0

                    else:
                        currentTurn = mouseClickHandler(chessboard, firstClick, row, col, prev_row, prev_col, currentTurn)
                        firstClick = 1
        else:
            chessboard = computerMove(chessboard, graphics.OPP)
            if currentTurn:
                currentTurn = False
            else:
                currentTurn = True

    pygame.display.flip()

pygame.quit()
sys.exit()
