import pygame

class Ship():
    def __init__(self, screen):
        """ Initialize the ship and set its starting position"""
        self.screen = screen

        # Load the ship image and get its rect
        self.image = pygame.image.load("pixabay_spaceship.bmp")
        self.image = pygame.transform.scale(self.image, (50,50))
        self.rect = self.image.get_rect()
        # rect_x, rect_y, rect_width, rect_length = self.rect
        # self.rect = rect(rect_x, rect_y, rect_width/10, rect_length/10)
        self.screen_rect = screen.get_rect()

        # start each new ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)