import pygame
import os
from config import PATH
class Person:
    gunsL = {'original':pygame.image.load(PATH+os.path.join('data', 'weapons','original.png')),
    'laser':pygame.image.load(PATH+os.path.join('data', 'weapons','laser.png'))}
    gunsR = {'original':pygame.transform.flip(pygame.image.load(PATH+os.path.join('data', 'weapons','original.png')), True, False),
    'laser':pygame.transform.flip(pygame.image.load(PATH+os.path.join('data', 'weapons','laser.png')), True, False)}
    walkLeft = [pygame.image.load(PATH+os.path.join('data', 'char','p0.png')), pygame.image.load(PATH+os.path.join('data', 'char','p1.png')),
                pygame.image.load(PATH+os.path.join('data', 'char','p2.png')), pygame.image.load(PATH+os.path.join('data', 'char','p3.png')),
                pygame.image.load(PATH+os.path.join('data', 'char','p4.png')), pygame.image.load(PATH+os.path.join('data', 'char','p5.png')),
                pygame.image.load(PATH+os.path.join('data', 'char','p6.png'))]
    walkRight = [pygame.image.load(PATH+os.path.join('data', 'char','r0.png')), pygame.image.load(PATH+os.path.join('data', 'char','r1.png')),
                 pygame.image.load(PATH+os.path.join('data', 'char','r2.png')), pygame.image.load(PATH+os.path.join('data', 'char','r3.png')),
                 pygame.image.load(PATH+os.path.join('data', 'char','r4.png')), pygame.image.load(PATH+os.path.join('data', 'char','r5.png')),
                 pygame.image.load(PATH+os.path.join('data', 'char','r6.png'))]
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.vel = 5
        self.width = width
        self.height = height
        self.left = False
        self.right = False
        self.walkCount = 0
        self.standing = True
        self.isJump = False
        self.jumpAcc = 20
        self.health=200
        self.shotDelay = 10
        self.grenades = 3
        self.weapon = 'original'

    def draw(self, win):
        if self.walkCount + 1 >= 28:
            self.walkCount = 0

        if not self.standing:
            if self.left:
                win.blit(Person.walkLeft[self.walkCount // 4], (self.x, self.y))
                win.blit(Person.gunsL[self.weapon], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(Person.walkRight[self.walkCount // 4], (self.x, self.y))
                win.blit(Person.gunsR[self.weapon], (self.x, self.y))
                self.walkCount += 1
        else:
            if self.left:
                win.blit(Person.walkLeft[0], (self.x, self.y))
                win.blit(Person.gunsL[self.weapon], (self.x, self.y))
            else:
                win.blit(Person.walkRight[0], (self.x, self.y))
                win.blit(Person.gunsR[self.weapon], (self.x, self.y))
