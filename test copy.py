import pygame
import sys

# Constants
WIDTH, HEIGHT = 512, 512
SQUARE_SIZE = WIDTH // 8  # Size of each square

# Colors (Green and Ivory)
GREEN = (118, 150, 86)
DARK_GREEN = (50, 80, 30)
IVORY = (255, 247, 228)
LIGHT_GREY = (200, 200, 200)  # Light grey color for circles

# Create the Pygame window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Chess Board')

# Function to generate the chessboard using the integer array
def generateBoard(board):
    for row in range(8):
        for col in range(8):
            base_color = IVORY if (row + col) % 2 == 0 else GREEN
            pygame.draw.rect(screen, base_color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

            # Calculate the center coordinates of the square
            center_x = col * SQUARE_SIZE + SQUARE_SIZE // 2
            center_y = row * SQUARE_SIZE + SQUARE_SIZE // 2

            circle_radius = SQUARE_SIZE // 6  # Smaller radius for the circle
            darker_color = DARK_GREEN if base_color == GREEN else LIGHT_GREY
            
            pygame.draw.circle(screen, darker_color, (center_x, center_y), circle_radius)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Generate the chessboard
    generateBoard(None)  # Replace 'None' with the chessboard array if needed
    
    pygame.display.flip()

pygame.quit()
sys.exit()
