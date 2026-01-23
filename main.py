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
    score = 0
    lives = 3
    font = pygame.font.Font(None, 36)
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
            center = pygame.Vector2(SCREEN_WIDTH / 2,SCREEN_HEIGHT / 2)
            for shot in shots:
                if obj.collides_with(shot):
                    log_event("asteroid_shot")
                    obj.split()
                    score += obj.score()
                    obj.kill()
                    shot.kill()
            if obj.collides_with(player):
                lives -= 1
                player.kill()
                if lives <= 0:
                    log_event("player_hit")
                    print(f"Score:{score}")
                    print("Game over!")
                    sys.exit()
                else:
                    # to remove the asteroids near re-spawn location
                    for asteroid in asteroids:
                        if asteroid.position.distance_to(center) < 200:
                            asteroid.kill()
                    player = Player(SCREEN_WIDTH / 2,SCREEN_HEIGHT / 2)
                    break
        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)
        
        score_text = font.render(f"Score: {score}", True, "white")
        lives_text = font.render(f"Lives: {lives}", True, "white")
        screen.blit(lives_text, (10,40))
        screen.blit(score_text, (10, 10))
        pygame.display.flip()


if __name__ == "__main__":
    main()
