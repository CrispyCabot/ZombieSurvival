from config import SCREEN_WIDTH, SCREEN_HEIGHT, PATH
import pygame
import os
class Grenade:
    explosion = [pygame.image.load(PATH+os.path.join('data', 'explosion','tile000.png')), pygame.image.load(PATH+os.path.join('data', 'explosion','tile001.png')), pygame.image.load(PATH+os.path.join('data', 'explosion','tile002.png')), pygame.image.load(PATH+os.path.join('data', 'explosion','tile003.png')), pygame.image.load(PATH+os.path.join('data', 'explosion','tile004.png')), pygame.image.load(PATH+os.path.join('data', 'explosion','tile005.png')), pygame.image.load(PATH+os.path.join('data', 'explosion','tile006.png')), pygame.image.load(PATH+os.path.join('data', 'explosion','tile007.png')), pygame.image.load(PATH+os.path.join('data', 'explosion','tile008.png')), pygame.image.load(PATH+os.path.join('data', 'explosion','tile009.png')), pygame.image.load(PATH+os.path.join('data', 'explosion','tile010.png')), pygame.image.load(PATH+os.path.join('data', 'explosion','tile011.png')), pygame.image.load(PATH+os.path.join('data', 'explosion','tile012.png')), pygame.image.load(PATH+os.path.join('data', 'explosion','tile013.png')), pygame.image.load(PATH+os.path.join('data', 'explosion','tile014.png')), pygame.image.load(PATH+os.path.join('data', 'explosion','tile015.png')), pygame.image.load(PATH+os.path.join('data', 'explosion','tile016.png')), pygame.image.load(PATH+os.path.join('data', 'explosion','tile017.png')), pygame.image.load(PATH+os.path.join('data', 'explosion','tile018.png')), pygame.image.load(PATH+os.path.join('data', 'explosion','tile019.png')), pygame.image.load(PATH+os.path.join('data', 'explosion','tile020.png')), pygame.image.load(PATH+os.path.join('data', 'explosion','tile021.png')), pygame.image.load(PATH+os.path.join('data', 'explosion','tile022.png')), pygame.image.load(PATH+os.path.join('data', 'explosion','tile023.png')), pygame.image.load(PATH+os.path.join('data', 'explosion','tile024.png')), pygame.image.load(PATH+os.path.join('data', 'explosion','tile025.png')), pygame.image.load(PATH+os.path.join('data', 'explosion','tile026.png')), pygame.image.load(PATH+os.path.join('data', 'explosion','tile027.png')), pygame.image.load(PATH+os.path.join('data', 'explosion','tile028.png')), pygame.image.load(PATH+os.path.join('data', 'explosion','tile029.png')), pygame.image.load(PATH+os.path.join('data', 'explosion','tile030.png')), pygame.image.load(PATH+os.path.join('data', 'explosion','tile031.png')), pygame.image.load(PATH+os.path.join('data', 'explosion','tile032.png')), pygame.image.load(PATH+os.path.join('data', 'explosion','tile033.png')), pygame.image.load(PATH+os.path.join('data', 'explosion','tile034.png')), pygame.image.load(PATH+os.path.join('data', 'explosion','tile035.png')), pygame.image.load(PATH+os.path.join('data', 'explosion','tile036.png')), pygame.image.load(PATH+os.path.join('data', 'explosion','tile037.png')), pygame.image.load(PATH+os.path.join('data', 'explosion','tile038.png')), pygame.image.load(PATH+os.path.join('data', 'explosion','tile039.png')), pygame.image.load(PATH+os.path.join('data', 'explosion','tile040.png')), pygame.image.load(PATH+os.path.join('data', 'explosion','tile041.png')), pygame.image.load(PATH+os.path.join('data', 'explosion','tile042.png')), pygame.image.load(PATH+os.path.join('data', 'explosion','tile043.png')), pygame.image.load(PATH+os.path.join('data', 'explosion','tile044.png')), pygame.image.load(PATH+os.path.join('data', 'explosion','tile045.png')), pygame.image.load(PATH+os.path.join('data', 'explosion','tile046.png')), pygame.image.load(PATH+os.path.join('data', 'explosion','tile047.png')), pygame.image.load(PATH+os.path.join('data', 'explosion','tile048.png')), pygame.image.load(PATH+os.path.join('data', 'explosion','tile049.png')), pygame.image.load(PATH+os.path.join('data', 'explosion','tile050.png')), pygame.image.load(PATH+os.path.join('data', 'explosion','tile051.png')), pygame.image.load(PATH+os.path.join('data', 'explosion','tile052.png')), pygame.image.load(PATH+os.path.join('data', 'explosion','tile053.png')), pygame.image.load(PATH+os.path.join('data', 'explosion','tile054.png')), pygame.image.load(PATH+os.path.join('data', 'explosion','tile055.png')), pygame.image.load(PATH+os.path.join('data', 'explosion','tile056.png')), pygame.image.load(PATH+os.path.join('data', 'explosion','tile057.png')), pygame.image.load(PATH+os.path.join('data', 'explosion','tile058.png')), pygame.image.load(PATH+os.path.join('data', 'explosion','tile059.png')), pygame.image.load(PATH+os.path.join('data', 'explosion','tile060.png')), pygame.image.load(PATH+os.path.join('data', 'explosion','tile061.png')), pygame.image.load(PATH+os.path.join('data', 'explosion','tile062.png')), pygame.image.load(PATH+os.path.join('data', 'explosion','tile063.png')), pygame.image.load(PATH+os.path.join('data', 'explosion','tile064.png')), pygame.image.load(PATH+os.path.join('data', 'explosion','tile065.png')), pygame.image.load(PATH+os.path.join('data', 'explosion','tile066.png')), pygame.image.load(PATH+os.path.join('data', 'explosion','tile067.png')), pygame.image.load(PATH+os.path.join('data', 'explosion','tile068.png')), pygame.image.load(PATH+os.path.join('data', 'explosion','tile069.png')), pygame.image.load(PATH+os.path.join('data', 'explosion','tile070.png')), pygame.image.load(PATH+os.path.join('data', 'explosion','tile071.png')), pygame.image.load(PATH+os.path.join('data', 'explosion','tile072.png')), pygame.image.load(PATH+os.path.join('data', 'explosion','tile073.png'))]
    img = pygame.image.load(PATH+os.path.join('data', 'images','grenade.png'))
    imgx, imgy = img.get_rect().size
    img = pygame.transform.scale(img, (int(.03*imgx), int(.03*imgy)))
    def __init__(self, x, y, direction, moving):
        self.x = x
        self.y = y
        self.dirr = direction
        self.jumpVar = 9
        self.angle = 25
        self.moving = moving
        self.exploding = False
        self.frameCounter = 0
        self.w, self.h = Grenade.explosion[35].get_rect().size
    def update(self, win, sound):
        if not self.exploding:
            if self.dirr: #LEFT
                self.x -= 7
                if self.moving:
                    self.x -= 5
            else:
                self.x += 7
                if self.moving:
                    self.x += 5
            if self.y < SCREEN_HEIGHT-100:
                self.y -= self.jumpVar
                self.jumpVar -= 1
            else: #Hit ground
                self.exploding = True
                sound.play()
            self.angle += 5
            grenade = pygame.transform.rotate(Grenade.img, self.angle)
            w, h = grenade.get_rect().size
            win.blit(grenade, (self.x+w//2, self.y+h//2))
        else:
        #    w, h = explosion[self.frameCounter//1].get_rect().size
            win.blit(Grenade.explosion[self.frameCounter//1], (self.x, self.y))
            self.frameCounter += 1
            if self.frameCounter >= 74: #148 if above is //2
                return True
