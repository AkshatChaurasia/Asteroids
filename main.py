import pygame, sys
from logger import log_state, log_event
from shot import Shot
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import SCREEN_HEIGHT, SCREEN_WIDTH

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        dt = clock.tick(60)/1000
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        for obj in asteroids:
            for shot in shots:
                if obj.collides_with(shot):
                    log_event("asteroid_shot")
                    obj.split()
                    obj.kill()
                    shot.kill()
            if obj.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()
