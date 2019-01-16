import pygame
import os
from config import PATH, SCREEN_WIDTH
class Bullet:
    bulletImg = pygame.image.load(PATH+os.path.join('data', 'images','bullet.png'))
    bulletLeft = pygame.transform.scale(bulletImg, (15, 7))
    bulletRight = pygame.transform.flip(bulletLeft, True, False)
    def __init__(self, x, y, left):
        self.x = x
        self.y = y
        self.left = left

    def draw(self, win):
        if self.left:
            self.x -= 10
            win.blit(Bullet.bulletLeft, (self.x, self.y))
        else:
            self.x += 10
            win.blit(Bullet.bulletRight, (self.x, self.y))
        if self.x > SCREEN_WIDTH or self.x < 0:
            return True
