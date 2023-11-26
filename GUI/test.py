import pygame
import tkinter as tk
from tkinter import filedialog

# Initialize Pygame
pygame.init()

# Set up Pygame window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("File Explorer in Pygame")

# Function to open file explorer
def open_file_explorer():
    # root = tk.Tk()
    # root.withdraw()  # Hide the main window

    file_path = filedialog.askopenfilename()
    print("Selected File:", file_path)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_o:
                open_file_explorer()

    pygame.display.flip()

# Quit Pygame
pygame.quit()
