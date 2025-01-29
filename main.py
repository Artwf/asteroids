# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

# import constants in constants.py
from constants import *

def main():
    pygame.init()
    # open new GUI window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    while True:
        # enable ability to quit game by closing window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.display.flip()

if __name__ == "__main__":
    main()