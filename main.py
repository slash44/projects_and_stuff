import pygame
import math
import sys

pygame.init()
fps = 60
clock = pygame.time.Clock()
game_running = True


def main():

    # Create the main game loop
    while game_running:

        # Here goes the boiler code.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


if __name__ == '__main__':
    main()
