import pygame
from constants import SCREEN_HEIGHT,SCREEN_WIDTH
from logger import log_state,log_event
from player import Player
from asteroids import Asteroid
from asteroidfield import AsteroidField
from circleshape import CircleShape
from shot import Shot
import sys


def main():

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    #groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    #containers
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable,drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots,updatable,drawable)

    #objects
    asteroid_field = AsteroidField()
    player_one = Player(SCREEN_WIDTH/2 , SCREEN_HEIGHT/2)
    
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)
        for asteroid_obj in asteroids:
            if asteroid_obj.collides_with(player_one):
                log_event("player_hit")
                print("Game Over!")
                sys.exit(1)
        for asteroid_obj in asteroids:
            for player_shots in shots:
                if player_shots.collides_with(asteroid_obj):
                    log_event("asteroid_shot")
                    asteroid_obj.split()
                    player_shots.kill()


        screen.fill("black")
        for drawables in drawable:
            drawables.draw(screen)
        pygame.display.flip()
        dt = (clock.tick(60))/1000




if __name__ == "__main__":
    main()
