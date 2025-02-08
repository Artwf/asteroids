# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

import sys

# import constants in constants.py
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    # open new GUI window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    clock = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots_group = pygame.sprite.Group()

    

    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots_group, updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()
    dt = 0
    
    while True:
        # enable ability to quit game by closing window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        player.update(dt, shots_group)
        for sprite in updatable:
            if sprite!= player:
                sprite.update(dt)
        for item in asteroids:
            if item.collision_check(player):
                print("Game over!")
                sys.exit()
            for i in shots_group:
                if item.collision_check(i):
                    item.split(asteroids)
                    i.kill()
        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        
        dt = clock.tick() / 1000

if __name__ == "__main__":
    main()