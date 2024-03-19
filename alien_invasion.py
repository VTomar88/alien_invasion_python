import game_functions as gf
import pygame
from settings import Settings
from ship import Ship
from alien import Alien

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

    # Make alien
    alien = Alien(ai_settings, screen)

    while True:
        gf.check_events()
        gf.update_screen(ai_settings, screen, ship, alien)

run_game()
