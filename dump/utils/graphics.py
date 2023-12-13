import pygame
from operator import add
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

def isValid(board, pos, legal_moves, og_row, og_col, currentTurn):
    row, col = pos
    if row == og_row and col == og_col:
        return True
    if (row)<8 and (row)>=0 and (col)<8 and (col)>=0:
        if board[row][col]//7 == (not currentTurn):
            legal_moves.append([row, col])
            return False        
        if board[row][col]//7 == currentTurn:
            return False
        return True
        
    else:
        return False
def LegalSquares(board, row, col, currentTurn):
    if currentTurn:
        mult = -1
    else:
        mult = 1
    legal_moves = list()
    if board[row][col]//7 == currentTurn:
        if board[row][col]%7 == 5: # BISHOP MOVIES
            directions = ((1,1), (1,-1), (-1,1), (-1,-1))
            for d in directions:
                pos = [row, col]
                while isValid(board, pos, legal_moves, row, col, currentTurn):
                    legal_moves.append(pos)
                    pos = list((map(add, pos, d)))
            while([row, col] in legal_moves):
                legal_moves.remove([row, col])
        elif board[row][col]%7 == 6: # PAWN MOVES
            direction = ((mult*1,0), (mult*2, 0))
            direction_attack = (mult*1,1), (mult*1,-1)
            for x,y in direction_attack:
                if (row+x)<8 and (row+x)>=0 and (col+y)<8 and (col+y)>=0:
                    if currentTurn:
                        if board[row+x][col+y]//7 == False:
                            legal_moves.append([row+x, col+y])
                    else:
                        if board[row+x][col+y]//7 == True:
                            legal_moves.append([row+x, col+y])

            x,y = direction[0]
            if board[x+row][y+col]==-1:
                legal_moves.append([row+x, col+y])
            x,y = direction[1]
            if (currentTurn):
                if board[x+row][y+col]==-1 and row == 6:
                    legal_moves.append([row+x, col+y])
            else:
                if board[x+row][y+col]==-1 and row == 1:
                    legal_moves.append([row+x, col+y])
                
        elif board[row][col]%7 == 3: # ROOK MOVIES
            directions = ((0,1), (0,-1), (-1,0), (1,0))
            for d in directions:
                pos = [row, col]
                while isValid(board, pos, legal_moves, row, col, currentTurn):
                    legal_moves.append(pos)
                    pos = list((map(add, pos, d)))
            while([row, col] in legal_moves):
                legal_moves.remove([row, col])

        elif board[row][col]%7 == 2: #  QUEEN MOVES
            directions = ((0,1), (0,-1), (-1,0), (1,0))
            for d in directions:
                pos = [row, col]
                while isValid(board, pos, legal_moves, row, col, currentTurn):
                    legal_moves.append(pos)
                    pos = list((map(add, pos, d)))
            directions = ((1,1), (1,-1), (-1,1), (-1,-1))
            for d in directions:
                pos = [row, col]
                while isValid(board, pos, legal_moves, row, col, currentTurn):
                    legal_moves.append(pos)
                    pos = list((map(add, pos, d)))
            while([row, col] in legal_moves):
                legal_moves.remove([row, col])
        elif board[row][col]%7 == 1: # KING MOVES
            direction = ((0,1), (0,-1), (-1,0), (1,-0), (1,1), (1,-1), (-1,1), (-1,-1))
            for x,y in direction:
                if (row+x)<8 and (row+x)>=0 and (col+y)<8 and (col+y)>=0:
                    if isValid(board, [row+x, col+y], legal_moves, row, col, currentTurn):
                        legal_moves.append([row+x, col+y])
            while([row, col] in legal_moves):
                legal_moves.remove([row, col])

                        # drawCaptureSquare(board, row+x,col+y)
        elif board[row][col]%7 == 4: # KNIGHT MOVES
            direction = ((2,1), (2,-1), (-1,2), (1,2),(-2,1), (-2,-1), (-1,-2), (1,-2))
            for x,y in direction:
                if (row+x)<8 and (row+x)>=0 and (col+y)<8 and (col+y)>=0:
                    if isValid(board, [row+x, col+y], legal_moves, row, col, currentTurn):
                        legal_moves.append([row+x, col+y])
            while([row, col] in legal_moves):
                legal_moves.remove([row, col])

    return legal_moves


def drawSquare(board, row, col, status, screen):
    if (status == 1):
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

def generateBoard(board, screen):
    for row in range(8):
        for col in range(8):
            drawSquare(board, row, col, 0, screen)

def drawCaptureSquare(board, row, col, screen):
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
def drawFreeSquares(board, row, col, screen):
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

def showLegal(board, row, col, currentTurn, screen):
    legal_moves = LegalSquares(board, row, col, currentTurn)
    for x in legal_moves:
        if board[x[0]][x[1]]//7 != -1:
            drawCaptureSquare(board, x[0], x[1], screen)
        elif board:
            drawFreeSquares(board, x[0], x[1], screen)









