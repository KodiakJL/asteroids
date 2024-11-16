# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from shot import Shot


def main():
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    score = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)
    asteroid_field = AsteroidField()
    font = pygame.font.Font(None, 36)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    as_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")

        for u in updatable:
            u.update(dt)

        for d in drawable:
            d.draw(screen)
            score_text = font.render(f"Score: {score}", True, "white")
            screen.blit(score_text, (10, 10))

        for a in asteroids:
            if a.collision_check(player):
                print("Game over!")
                raise SystemExit
            for bullet in shots:
                if bullet.collision_check(a):
                    a.split()
                    bullet.kill()
                    score += ASTEROID_DESTROY_SCORE
            

        pygame.display.flip()

        #limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()