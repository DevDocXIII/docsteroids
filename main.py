# Import necessary modules from pygame and constants module
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS, ASTEROID_KINDS, ASTEROID_SPAWN_RATE
from player import Player, PLAYER_RADIUS
from asteroid import Asteroid
from asteroidfield import AsteroidField

# Define the main function for game loop and event handling
def main():
    # Initialize pygame module to start using its functions
    pygame.init()

    # Create a display surface with specified screen width and height
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))    
    
    # Print initial game information (screen width, height) to the console
    print("Starting Asteroids!")
    print(f"Screen width: {1280}") 
    print(f"Screen height: {720}")

    # Create a clock object to control the frame rate of the game loop
    clock = pygame.time.Clock()
    dt = 0 # delta time
    # Set caption for the display window of the game
    pygame.display.set_caption("DevDocSteroids")
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroid_group = pygame.sprite.Group()

    Asteroid.containers = (asteroid_group,updatable,drawable)
    AsteroidField.containers = (updatable,)
    Player.containers = (updatable,drawable)

    asteroid_field = AsteroidField()    
    our_hero = Player(SCREEN_WIDTH/2 ,SCREEN_HEIGHT/2, PLAYER_RADIUS)
    

    # Start main game loop that runs until user quits the game
    while True:
        # Event handling loop to process events such as keyboard input, mouse clicks etc.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # If user closes the window, quit the game and return
                pygame.quit()
                return
        # Control the frame rate of the game loop to run at desired speed (60 fps)
        dt = clock.tick(60)/1000

        # Fill the display surface with black color to clear previous frame's drawing
        screen.fill((0, 0, 0))
        #our_hero.update(dt)
        updatable.update(dt)

        for sprite in drawable:
            sprite.draw(screen)
        #our_hero.draw(screen)


        # Update the display surface by flipping it (double buffering)
        pygame.display.flip()

        # Control the frame rate of the game loop to run at desired speed (60 fps)
        dt = clock.tick(60)


# Check if script is being run directly, call main function to start the gamel
if __name__ == "__main__":
    main()
