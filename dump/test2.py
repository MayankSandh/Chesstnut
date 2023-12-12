import pygame
import sys
import time

# Constants
WIDTH, HEIGHT = 512, 512
SQUARE_SIZE = WIDTH // 8  # Size of each square
FPS = 30  # Frames per second for the fading effect

# Colors
GREEN = (118, 150, 86)
IVORY = (255, 247, 228)
RED = (255, 0, 0)

# Create the Pygame window
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Initialize variables to track the clicked square and fading effect
fade_alpha = 0
  # Fade duration in milliseconds (3 seconds)

# Function to generate the chessboard
def generateBoard():
    screen.fill(IVORY)  # Fill the screen with ivory color

    # Generate the chessboard
    for row in range(8):
        for col in range(8):
            color = GREEN if (row + col) % 2 == 0 else IVORY
            pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    pygame.display.flip()

# Function to flash a red square with fade-in and fade-out effect
def flashRedSquare(row, col):

    fade_alpha = 0
    fading_in = True
    fading_out = False
    fade_duration = 700
    start_time = time.time()

    while fading_in or fading_out:
        current_time = time.time()
        elapsed_time = current_time - start_time

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if fading_in:
            fade_alpha = int((elapsed_time / (fade_duration /1000)) * 255)
            if fade_alpha >= 255:
                fade_alpha = 255
                fading_in = False
                fading_out = True
                start_time = time.time()

        elif fading_out:
            fade_alpha = int(((fade_duration / 1000 - elapsed_time)) / (fade_duration / 1000) * 255)
            if fade_alpha <= 0:
                fade_alpha = 0
                fading_out = False

        # Draw the square with fading red color
        color = RED + (fade_alpha,)
        pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
        pygame.display.flip()

    generateBoard()

    # Redraw the board after fading effect

if __name__ == '__main__':
    generateBoard()  # Generate the initial chessboard

    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Check for left mouse button click
                    # Get the mouse click coordinates
                    click_x, click_y = event.pos
                    # Calculate the square indices based on click coordinates
                    square_col = click_x // SQUARE_SIZE
                    square_row = click_y // SQUARE_SIZE
                    flashRedSquare(square_row, square_col)  # Flash the clicked square
