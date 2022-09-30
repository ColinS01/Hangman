import pygame
import os

WIDTH = 1152
HEIGHT = 648
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('HANGMAN')

FPS = 60

# INITIALIZING COLORS
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


# LOADING IMAGES FOR BACKGROUND AND BODY PARTS
BACKGROUND_IMG = pygame.image.load(os.path.join('Assets', 'Hangman.png'))
HEAD_IMG = pygame.image.load(os.path.join('Assets', 'Hangman.png'))
BODY_IMG = pygame.image.load(os.path.join('Assets', 'Hangman.png'))
FIRST_ARM_IMG = pygame.image.load(os.path.join('Assets', 'Hangman.png'))
SECOND_ARM_IMG = pygame.image.load(os.path.join('Assets', 'Hangman.png'))
FIRST_LEG_IMG = pygame.image.load(os.path.join('Assets', 'Hangman.png'))
SECOND_LEG_IMG = pygame.image.load(os.path.join('Assets', 'Hangman.png'))
