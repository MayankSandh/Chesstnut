import pygame
from tkinter import Tk, simpledialog, messagebox

# Pygame initialization
pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Name Display')

font = pygame.font.Font(None, 36)
text_color = (255, 255, 255)
bg_color = (0, 0, 0)
name = ""

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left click
            root = Tk()
            root.withdraw()  # Hide the root window
            name = simpledialog.askstring("Input", "Enter your name:")
            root.destroy()  # Close the root window after getting input
            if name:
                print("Entered name:", name)
                message = f"Hello, {name}!"
                messagebox.showinfo("Greetings", message)

    screen.fill(bg_color)
    text_surface = font.render(name, True, text_color)
    screen.blit(text_surface, (100, 100))

    pygame.display.flip()

pygame.quit()
