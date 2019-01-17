import pygame
import os
from config import PATH, SCREEN_WIDTH
class Bullet:
    bulletImg = pygame.image.load(PATH+os.path.join('data', 'weapons','originalShot.png'))
    originalLeft = pygame.transform.scale(bulletImg, (15, 7))
    originalRight = pygame.transform.flip(originalLeft, True, False)
    img = pygame.image.load(PATH+os.path.join('data', 'weapons', 'laserShot.png'))
    laser = pygame.transform.scale(img, (15, 7))
    def __init__(self, x, y, left, type):
        self.x = x
        self.y = y
        self.left = left
        self.type = type

    def draw(self, win):
        if self.left:
            self.x -= 10
            if self.type == 'original':
                win.blit(Bullet.originalLeft, (self.x, self.y))
            elif self.type == 'laser':
                win.blit(Bullet.laser, (self.x, self.y))
        else:
            self.x += 10
            if self.type == 'original':
                win.blit(Bullet.originalRight, (self.x, self.y))
            elif self.type == 'laser':
                win.blit(Bullet.laser, (self.x, self.y))
        if self.x > SCREEN_WIDTH or self.x < 0:
            return True
