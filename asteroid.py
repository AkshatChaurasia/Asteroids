import pygame, random
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from circleshape import CircleShape
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            "white",
            self.position,
            self.radius,
            LINE_WIDTH
        )
        
    def update(self, dt):
        self.position += (self.velocity * dt)
    
    def score(self):
        if self.radius <= ASTEROID_MIN_RADIUS: 
            # small asteroid
            return 100
        elif self.radius <= ASTEROID_MIN_RADIUS * 2:
            # medium asteroid
            return 50
        # large asteroid
        return 20

    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            return 
        else:
            log_event("asteroid_split")
            angle = random.uniform(20, 50)
            vel_vec1 = self.velocity.rotate(angle)
            vel_vec2 = self.velocity.rotate(-angle)
            new_rad = self.radius - ASTEROID_MIN_RADIUS
            ast1 = Asteroid(self.position.x, self.position.y, new_rad)
            ast2 = Asteroid(self.position.x, self.position.y, new_rad)
            ast1.velocity = vel_vec1 * 1.2
            ast2.velocity = vel_vec2 * 1.2
             
