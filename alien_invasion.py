import game_functions as gf
import pygame
from pygame.sprite import Group
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
    ship = Ship(ai_settings, screen)

    # Make a group to store bullets in
    bullets = Group()

    # Make alien
    alien = Alien(ai_settings, screen)

    while True:

        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, bullets, alien)

run_game()
