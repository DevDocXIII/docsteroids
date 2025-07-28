import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED

class Player(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0
        
    def draw(self, screen):
        self.screen = screen
        pygame.draw.polygon(screen,(255,255,255),self.triangle(),2)
        
    #    return super().draw(screen)
    # def update(self, dt):
    #     self.dt = dt
    #     keys = pygame.key.get_pressed()

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:  # left key pressed
            self.rotation += dt * PLAYER_TURN_SPEED * -1  # rotate left
        
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:  # right key pressed
            self.rotation += dt * PLAYER_TURN_SPEED  # rotate right

        if keys[pygame.K_w] or keys[pygame.K_UP]: #forward speed pressed (UP)
            self.move(dt)
            
        if keys[pygame.K_s] or keys[pygame.K_DOWN]: #backward speed pressed (down)
            self.move(dt*-1)

    def move(self,dt):
        #print(f"{dt}th of a second")
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
   
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        #print(f"A:{a} B:{b} C:{c}")
        return [a, b, c]