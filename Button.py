import pygame
from RoundRect import AAfilledRoundedRect #Got from https://www.pygame.org/project-AAfilledRoundedRect-2349-.html
class Button:
    def __init__(self,x,y,width,height,color, text, font, txtCol):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.color = color
        self.active = True
        self.font = font
        self.txtCol = txtCol
    def isInside(self):
        x, y = pygame.mouse.get_pos()
        if x > self.x and x < self.x+self.width and y < self.y+self.height and y > self.y:
            return True
        return False
    def update(self, win):
        if self.isInside():
            AAfilledRoundedRect(win, pygame.Rect(self.x, self.y, self.width, self.height), (self.color[0]-20, self.color[1]-20, self.color[2]-20))
        else:
            AAfilledRoundedRect(win, pygame.Rect(self.x, self.y, self.width, self.height), (self.color[0], self.color[1], self.color[2]))
        text = self.font.render(self.text, False, (self.txtCol[0], self.txtCol[1], self.txtCol[2]))
        tW, tH = text.get_rect().size
        temp = (self.width-tW)/2
        temp1 = (self.height-tH)/2
        win.blit(text,(self.x+temp,self.y+temp1))
    def clicked(self):
        if self.isInside() and pygame.mouse.get_pressed()[0]:
            return True
        return False
