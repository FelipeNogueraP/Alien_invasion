import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        # load the alien image and set its rect attribute
        self.image = pygame.image.load("images/alien.png")
        self.rect = self.image.get_rect()
        # start new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # store the alien's exact horizontal position
        self.x = float(self.rect.x)
        self.settings = ai_game.settings

    def update(self):
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x

    def check_edges(self):
        # return True if an alien reach the edge
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
