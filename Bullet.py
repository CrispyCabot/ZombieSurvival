import pygame
import os
from config import PATH, SCREEN_WIDTH
class Bullet:
    bulletImg = pygame.image.load(PATH+os.path.join('data', 'weapons','originalShot.png'))
    originalLeft = pygame.transform.scale(bulletImg, (15, 7))
    originalRight = pygame.transform.flip(originalLeft, True, False)
    img = pygame.image.load(PATH+os.path.join('data', 'weapons', 'laserShot.png'))
    laser = pygame.transform.scale(img, (15, 7))
    img = pygame.image.load(PATH+os.path.join('data', 'weapons', 'plasmaShot.png'))
    plasma = pygame.transform.scale(img, (40,40))
    def __init__(self, x, y, left, type):
        self.x = x
        self.y = y
        self.left = left
        self.type = type
        self.speed = 10

    def draw(self, win):
        if self.type == 'machine':
            self.speed = 20
        else:
            self.speed = 10
        if self.left:
            self.x -= self.speed
        else:
            self.x += self.speed
        if self.type == 'original' and self.left:
            win.blit(Bullet.originalLeft, (self.x, self.y))
        elif self.type == 'original':
            win.blit(Bullet.originalRight, (self.x, self.y))
        elif self.type == 'laser':
            win.blit(Bullet.laser, (self.x, self.y))
        elif self.type == 'machine':
            pygame.draw.rect(win, (100,100,100), pygame.Rect(self.x, self.y, 6, 2))
        elif self.type == 'plasma':
            win.blit(Bullet.plasma, (self.x, self.y-20))
        if self.x > SCREEN_WIDTH or self.x < 0:
            return True
