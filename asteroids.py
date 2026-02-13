from circleshape import CircleShape
import pygame
from constants import LINE_WIDTH,ASTEROID_MIN_RADIUS
from logger import log_event
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    def draw(self, screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,LINE_WIDTH)
    def update(self, dt):
        self.position += self.velocity*dt
    def split(self):
        self.kill()
        if (self.radius <= ASTEROID_MIN_RADIUS):
            return
        else:
            log_event("Asteroid_split")
            angle = random.uniform(20,50)
            ast_one_movement = self.velocity.rotate(angle)
            ast_two_movement = self.velocity.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            ast_one = Asteroid(self.position,self.position,new_radius)
            ast_two = Asteroid(self.position,self.position,new_radius)
            ast_one.velocity = ast_one_movement * 1.2
            ast_two.velocity = ast_two_movement * 1.2




