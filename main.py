import pygame
from constants import  (
    SCREEN_WIDTH, 
    SCREEN_HEIGHT,
    ASTEROID_MIN_RADIUS, 
    ASTEROID_MAX_RADIUS, 
    ASTEROID_KINDS, 
    ASTEROID_SPAWN_RATE
    )


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))    
    print("Starting Asteroids!")
    print(f"Screen width: {1280}") 
    print(f"Screen height: {720}")
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        # Update and draw game elements here (e.g., asteroids)
        # For now, just fill the screen with black
        screen.fill((0, 0, 0))
        
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
