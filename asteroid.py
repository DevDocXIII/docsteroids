import pygame
import random # Import the random module for generating random numbers
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    def draw(self,screen):
        pygame.draw.circle(screen,(255, 255, 255),(int(self.position.x),int(self.position.y)),self.radius,2)
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            from asteroidfield import AsteroidField # Import the AsteroidField class from the aster 
            random_angle = random.uniform(20.0,50.0)
            velocity_vector1 = self.velocity.rotate(random_angle) * 1.2 # Rotate the velocity vector by a random angle
            velocity_vector2 = self.velocity.rotate(random_angle*-1) * 1.2 # Rotate the velocity vector by a random angle
            #print(f"vectors={random_angle} and -{random_angle}")
            new_radius = self.radius - ASTEROID_MIN_RADIUS # Calculate the new radius for the smaller asteroids
            new_asteroid1 = Asteroid (self.position.x, self.position.y, new_radius) 
            new_asteroid1.velocity = velocity_vector1 
            new_asteroid2 = Asteroid (self.position.x, self.position.y, new_radius) 
            new_asteroid2.velocity = velocity_vector2
            


            