import pygame
class LoadingScreen:
    def __init__(self, win, screenWidth, screenHeight, font):
        self.text = 'Fonts'
        self.barLevel = 0
        self.frameCount = 0
        self.speed = 1
        self.totalBars = 52
        self.multi = 5
        self.screenHeight = screenHeight
        self.screenWidth = screenWidth
        self.loadFont = font
    def update(self, win):
        self.barLevel += 1
        pygame.draw.rect(win, (0,0,0), pygame.Rect(0, self.screenHeight-100, self.screenWidth, 100))
        pygame.draw.rect(win, (255,255,255), pygame.Rect((self.screenWidth-self.totalBars*self.multi)/2, self.screenHeight-75, self.totalBars*self.multi, 20), 1)
        pygame.draw.rect(win, (0,255,0), pygame.Rect((self.screenWidth-self.totalBars*self.multi)/2, self.screenHeight-75, self.barLevel*self.multi, 20))
    #    print(self.barLevel) #Used to find the total bar level
        text = self.loadFont.render(self.text, True, (255,255,255))
        imgX, ignore = text.get_rect().size
        win.blit(text, ((self.screenWidth-imgX)/2,self.screenHeight-40))
    #    time.sleep(.1)
