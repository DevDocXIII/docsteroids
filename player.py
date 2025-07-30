import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, SHOT_RADIUS

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
        
        if keys[pygame.K_SPACE]: # space bar pressed to fire
            print("Shot Fired!!!")
            self.shoot(dt)        
    
    def shoot (self, dt):
        shot = Shot(self.position.x, self.position.y, SHOT_RADIUS, self.rotation) #create a new shot at the player's position
        shot.velocity = pygame.Vector2 (0, 1).rotate(shot.rotation) * PLAYER_SHOOT_SPEED
        pygame.draw.circle(self.screen,(255, 255, 255),(int(self.position.x),int(self.position.y)),SHOT_RADIUS,2)
        #self.velocity = pygame.Vector2 (0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED #update velocity based on rotation
        #shot.move(dt) #move the shot    

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
    
class Shot (CircleShape): #player shot
    def __init__(self, x, y, radius, rotation): #rotation is the direction of the shot
        super().__init__(x, y, radius)
        self.rotation = rotation # Store the initial rotation
        self.velocity = pygame.Vector2 (0, 1).rotate(rotation) * PLAYER_SHOOT_SPEED
                
    def draw(self,screen):
        pygame.draw.circle(screen,(255, 255, 255),(int(self.position.x),int(self.position.y)),SHOT_RADIUS,2)
        
    def update(self, dt):
        self.velocity = pygame.Vector2 (0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        self.position += self.velocity * dt

    def move (self,dt): #move the shot
        self.position += self.velocity * dt #update position based on velocity

        #self.screen = screen #needed to draw the shot
        #self.position += self.velocity * dt

            
                   