import sys
import pygame
from settings import Settings
from ship import Ship

def run_game():
    # Initialize pygame, settings, and screen objects
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    ai_settings = Settings()
    screen = pygame.display.set_mode((
        ai_settings.screen_width, ai_settings.screen_height
    ))
    # Make ship
    ship = Ship(screen)
    print(ship.rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # Redraw the screen during each pass through the loop.
        screen.fill(ai_settings.bg_color)
        ship.blitme()

        pygame.display.flip()

run_game()

