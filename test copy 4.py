import tkinter as tk
import pygame

def display_image(image_name):
    print("Clicked image:", image_name)
    return image_name

def create_dialog():
    root = tk.Tk()

    def button_click(image_name):
        root.destroy()
        display_image(image_name)

    root.title("Image Dialog")
    root.geometry("300x300")

    # Load images
    img_names = ["image1.png", "image2.png", "image3.png", "image4.png"]
    images = [tk.PhotoImage(file=img) for img in img_names]

    # Create buttons with images
    buttons = []
    for i in range(4):
        button = tk.Button(root, image=images[i], command=lambda idx=i: button_click(img_names[idx]))
        button.grid(row=i // 2, column=i % 2, padx=10, pady=10)
        buttons.append(button)

    root.mainloop()

# Pygame initialization
pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Image Display')

font = pygame.font.Font(None, 36)
text_color = (255, 255, 255)
bg_color = (0, 0, 0)
current_image = ""

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left click
            create_dialog()

    screen.fill(bg_color)
    text_surface = font.render(current_image, True, text_color)
    screen.blit(text_surface, (100, 100))

    pygame.display.flip()

pygame.quit()
