# Shooting game
import pygame
import time
import threading
from random import randint, choice
from Button import Button

timeStart = time.time()

loading = True

pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.mixer.init()
pygame.init()

loadFont = pygame.font.Font('28DaysLater.ttf', 36)
loadFont2 = pygame.font.Font('28DaysLater.ttf', 76)

clock = pygame.time.Clock()

screenWidth = 800
screenHeight = 500

win = pygame.display.set_mode((screenWidth, screenHeight)) #, pygame.RESIZABLE

pygame.display.set_caption('Zombie Survival')

loadZombie = [pygame.image.load('zombieLoading/tile000.png'), pygame.image.load('zombieLoading/tile001.png'),
                pygame.image.load('zombieLoading/tile002.png'), pygame.image.load('zombieLoading/tile003.png'),
                pygame.image.load('zombieLoading/tile004.png'), pygame.image.load('zombieLoading/tile005.png'),
                pygame.image.load('zombieLoading/tile006.png'), pygame.image.load('zombieLoading/tile007.png'),
                pygame.image.load('zombieLoading/tile008.png'), pygame.image.load('zombieLoading/tile009.png'),]

def zombieLoad():
    global loading, win
    speed = 5
    frameCount = 0
    while loading:
        text = loadFont2.render('Loading', True, (255,255,255))
        w, ignore = text.get_rect().size
        pygame.draw.rect(win, (0,0,0), pygame.Rect(0,0,screenWidth, screenHeight-100))
        win.blit(text, ((screenWidth-w)/2, 15))
        img = loadZombie[frameCount//speed]
        imgW, imgH = img.get_rect().size
        win.blit(img, ((screenWidth-imgW)/2, (screenHeight-imgH)/2))
        if frameCount+1 >= speed * len(loadZombie):
            frameCount = 0
        else:
            frameCount += 1
        clock.tick(60)
        pygame.display.update()

thread1 = threading.Thread(target=zombieLoad)
thread1.start()

class LoadingScreen:
    def __init__(self):
        self.text = 'Fonts'
        self.barLevel = 0
        self.frameCount = 0
        self.speed = 1
        self.totalBars = 52
        self.multi = 5
    def update(self, win):
        self.barLevel += 1
        pygame.draw.rect(win, (0,0,0), pygame.Rect(0, screenHeight-100, screenWidth, 100))
        pygame.draw.rect(win, (255,255,255), pygame.Rect((screenWidth-self.totalBars*self.multi)/2, screenHeight-75, self.totalBars*self.multi, 20), 1)
        pygame.draw.rect(win, (0,255,0), pygame.Rect((screenWidth-self.totalBars*self.multi)/2, screenHeight-75, self.barLevel*self.multi, 20))
    #    print(self.barLevel) #Used to find the total bar level
        text = loadFont.render(self.text, True, (255,255,255))
        imgX, ignore = text.get_rect().size
        win.blit(text, ((screenWidth-imgX)/2,screenHeight-40))
    #    time.sleep(.1)

loadScreen = LoadingScreen()
loadScreen.text = 'Fonts'
loadScreen.update(win)

gameScreen = 'home'

myFont = pygame.font.Font('28DaysLater.ttf', 22) #Score Font
font = pygame.font.Font('28DaysLater.ttf', 36) #Game Over Font
plFont = pygame.font.Font('28DaysLater.ttf', 56) #play font
plFont2 = pygame.font.Font('28DaysLater.ttf', 60)
splFont = pygame.font.Font('28DaysLater.ttf', 36) #Shop/Quit font
splFont2 = pygame.font.Font('28DaysLater.ttf', 40)
titleFont = pygame.font.Font('ZombieSlayer.ttf', 70)
shopFont = pygame.font.Font('varsityteam.otf', 20)
shopFont2 = pygame.font.Font('varsityteam.otf', 24)

loadScreen.text = 'Buttons'
loadScreen.update(win)

backBtn = Button(0,screenHeight-50,100,50, [100,100,100], 'Back', splFont, [255,255,255], splFont2)

def homeScreenLoad():
    global homeButtons
    homeButtons = []
    playBtn = Button((screenWidth - 200)/2,(screenHeight-100)/2-30,200,100,[200,20,20], 'Play', plFont, [0,0,0], plFont2)
    homeButtons.append(playBtn)
    quitBtn = Button((screenWidth-200)/2, (screenHeight-50)/2+50,200,50, [20,20,20], 'Quit', splFont, [150,150,150], splFont2)
    homeButtons.append(quitBtn)
homeScreenLoad()
loadScreen.update(win)
def betweenScreensLoad():
    global betweenBtns
    betweenBtns = []
    playBtn = Button((screenWidth - 220)/2,(screenHeight-100)/2-30,220,100,[200,20,20], 'Continue', plFont, [0,0,0], plFont2)
    betweenBtns.append(playBtn)
    shopBtn = Button((screenWidth-100)/2-60, (screenHeight-50)/2+50,100,50, [20,255,20], 'Shop', splFont, [0,0,0], splFont2)
    betweenBtns.append(shopBtn)
    quitBtn = Button((screenWidth-100)/2+60, (screenHeight-50)/2+50,100,50, [20,20,20], 'Quit', splFont, [150,150,150], splFont2)
    betweenBtns.append(quitBtn)
betweenScreensLoad()
loadScreen.update(win)
def shopScreenLoad():
    global shopButtons
    shopButtons = []
    healthInc = Button((screenWidth-100)/2-300,75,150,25,[96,165,243], '$20 - Health', shopFont, [255,255,255], shopFont2)
    shopButtons.append(healthInc)
shopScreenLoad()
loadScreen.update(win)
def loadShit():
    global background
    global bulletImg
    global bulletLeft
    global bulletRight
    global walkLeft
    global walkRight
    global sounds
    global songs
    global waveText
    background = pygame.image.load('images/background.jpg')
    background = pygame.transform.scale(background, (screenWidth, screenHeight))
    bulletImg = pygame.image.load('images/bullet.png')
    bulletLeft = pygame.transform.scale(bulletImg, (15, 7))
    bulletRight = pygame.transform.flip(bulletLeft, True, False)

    #convert_alpha is supposed to allow me to use set_alpha later on, but it doesn't work so fuck it.
    waveText = [pygame.image.load('waveText/wave1.png').convert_alpha(), pygame.image.load('waveText/wave2.png').convert_alpha(),
                pygame.image.load('waveText/wave3.png').convert_alpha(), pygame.image.load('waveText/wave4.png').convert_alpha(),
                pygame.image.load('waveText/wave5.png').convert_alpha(), pygame.image.load('waveText/wave6.png').convert_alpha(),
                pygame.image.load('waveText/wave7.png').convert_alpha(), pygame.image.load('waveText/wave8.png').convert_alpha(),
                pygame.image.load('waveText/wave9.png').convert_alpha(), pygame.image.load('waveText/wave10.png').convert_alpha()]
    loadScreen.text = 'Player Walk Left'
    loadScreen.update(win)
    walkLeft = [pygame.image.load('char/p0.png'), pygame.image.load('char/p1.png'),
                pygame.image.load('char/p2.png'), pygame.image.load('char/p3.png'),
                pygame.image.load('char/p4.png'), pygame.image.load('char/p5.png'),
                pygame.image.load('char/p6.png')]
    loadScreen.text = 'Player Walk Right'
    loadScreen.update(win)
    walkRight = [pygame.image.load('char/r0.png'), pygame.image.load('char/r1.png'),
                 pygame.image.load('char/r2.png'), pygame.image.load('char/r3.png'),
                 pygame.image.load('char/r4.png'), pygame.image.load('char/r5.png'),
                 pygame.image.load('char/r6.png')]

    loadScreen.text = 'Sounds'
    loadScreen.update(win)

    songs = ['songs/cant-go-to-hell.mp3', 'songs/highway-to-hell.mp3', 'songs/bloodwater.mp3']

    sounds = {'shot': pygame.mixer.Sound('sounds/bullet.wav'),
              'hit': pygame.mixer.Sound('sounds/hit.wav')}
    sounds['hit'].set_volume(0.1)
    sounds['shot'].set_volume(0.5)

def loadZombies():
    loadScreen.text = 'z1AttackL'
    loadScreen.update(win)
    global z1AttackL
    z1AttackL = []
    img = pygame.image.load('zombie1/animation/Attack1.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z1AttackL.append(img)
    img = pygame.image.load('zombie1/animation/Attack2.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z1AttackL.append(img)
    img = pygame.image.load('zombie1/animation/Attack3.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z1AttackL.append(img)
    img = pygame.image.load('zombie1/animation/Attack4.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z1AttackL.append(img)
    img = pygame.image.load('zombie1/animation/Attack5.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z1AttackL.append(img)
    img = pygame.image.load('zombie1/animation/Attack6.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z1AttackL.append(img)

    loadScreen.text = 'z1DeathL'
    loadScreen.update(win)
    global z1DeathL
    z1DeathL = []
    img = pygame.image.load('zombie1/animation/Dead1.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z1DeathL.append(img)
    img = pygame.image.load('zombie1/animation/Dead2.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z1DeathL.append(img)
    img = pygame.image.load('zombie1/animation/Dead3.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z1DeathL.append(img)
    img = pygame.image.load('zombie1/animation/Dead4.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z1DeathL.append(img)
    img = pygame.image.load('zombie1/animation/Dead5.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z1DeathL.append(img)
    img = pygame.image.load('zombie1/animation/Dead6.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z1DeathL.append(img)
    img = pygame.image.load('zombie1/animation/Dead7.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z1DeathL.append(img)
    img = pygame.image.load('zombie1/animation/Dead8.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z1DeathL.append(img)

    loadScreen.text = 'z1HurtL'
    loadScreen.update(win)
    global z1HurtL
    z1HurtL = []
    img = pygame.image.load('zombie1/animation/Hurt1.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z1HurtL.append(img)
    img = pygame.image.load('zombie1/animation/Hurt2.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z1HurtL.append(img)
    img = pygame.image.load('zombie1/animation/Hurt3.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z1HurtL.append(img)
    img = pygame.image.load('zombie1/animation/Hurt4.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z1HurtL.append(img)
    img = pygame.image.load('zombie1/animation/Hurt5.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z1HurtL.append(img)

    loadScreen.text = 'z1IdleL'
    loadScreen.update(win)
    global z1IdleL
    z1IdleL = []
    img = pygame.image.load('zombie1/animation/Idle1.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z1IdleL.append(img)
    img = pygame.image.load('zombie1/animation/Idle2.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z1IdleL.append(img)
    img = pygame.image.load('zombie1/animation/Idle3.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z1IdleL.append(img)
    img = pygame.image.load('zombie1/animation/Idle4.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z1IdleL.append(img)

    loadScreen.text = 'z1JumpL'
    loadScreen.update(win)
    global z1JumpL
    z1JumpL = []
    img = pygame.image.load('zombie1/animation/Jump1.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z1JumpL.append(img)
    img = pygame.image.load('zombie1/animation/Jump2.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z1JumpL.append(img)
    img = pygame.image.load('zombie1/animation/Jump3.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z1JumpL.append(img)
    img = pygame.image.load('zombie1/animation/Jump4.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z1JumpL.append(img)
    img = pygame.image.load('zombie1/animation/Jump5.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z1JumpL.append(img)
    img = pygame.image.load('zombie1/animation/Jump6.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z1JumpL.append(img)
    img = pygame.image.load('zombie1/animation/Jump7.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z1JumpL.append(img)

    loadScreen.text = 'z1RunL'
    loadScreen.update(win)
    global z1RunL
    z1RunL = []
    img = pygame.image.load('zombie1/animation/Run1.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z1RunL.append(img)
    img = pygame.image.load('zombie1/animation/Run2.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z1RunL.append(img)
    img = pygame.image.load('zombie1/animation/Run3.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z1RunL.append(img)
    img = pygame.image.load('zombie1/animation/Run4.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z1RunL.append(img)
    img = pygame.image.load('zombie1/animation/Run5.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z1RunL.append(img)
    img = pygame.image.load('zombie1/animation/Run6.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z1RunL.append(img)
    img = pygame.image.load('zombie1/animation/Run7.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z1RunL.append(img)
    img = pygame.image.load('zombie1/animation/Run8.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z1RunL.append(img)
    img = pygame.image.load('zombie1/animation/Run9.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z1RunL.append(img)
    img = pygame.image.load('zombie1/animation/Run10.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z1RunL.append(img)

    loadScreen.text = 'z1WalkL'
    loadScreen.update(win)
    global z1WalkL
    z1WalkL = []
    img = pygame.image.load('zombie1/animation/Walk1.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z1WalkL.append(img)
    img = pygame.image.load('zombie1/animation/Walk2.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z1WalkL.append(img)
    img = pygame.image.load('zombie1/animation/Walk3.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z1WalkL.append(img)
    img = pygame.image.load('zombie1/animation/Walk4.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z1WalkL.append(img)
    img = pygame.image.load('zombie1/animation/Walk5.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z1WalkL.append(img)
    img = pygame.image.load('zombie1/animation/Walk6.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z1WalkL.append(img)

    loadScreen.text = 'z2AttackL'
    loadScreen.update(win)
    global z2AttackL
    z2AttackL = []
    img = pygame.image.load('zombie2/animation/Attack1.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z2AttackL.append(img)
    img = pygame.image.load('zombie2/animation/Attack2.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z2AttackL.append(img)
    img = pygame.image.load('zombie2/animation/Attack3.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z2AttackL.append(img)
    img = pygame.image.load('zombie2/animation/Attack4.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z2AttackL.append(img)
    img = pygame.image.load('zombie2/animation/Attack5.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z2AttackL.append(img)
    img = pygame.image.load('zombie2/animation/Attack6.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z2AttackL.append(img)

    loadScreen.text = 'z2DeathL'
    loadScreen.update(win)
    global z2DeathL
    z2DeathL = []
    img = pygame.image.load('zombie2/animation/Dead1.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z2DeathL.append(img)
    img = pygame.image.load('zombie2/animation/Dead2.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z2DeathL.append(img)
    img = pygame.image.load('zombie2/animation/Dead3.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z2DeathL.append(img)
    img = pygame.image.load('zombie2/animation/Dead4.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z2DeathL.append(img)
    img = pygame.image.load('zombie2/animation/Dead5.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z2DeathL.append(img)
    img = pygame.image.load('zombie2/animation/Dead6.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z2DeathL.append(img)
    img = pygame.image.load('zombie2/animation/Dead7.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z2DeathL.append(img)
    img = pygame.image.load('zombie2/animation/Dead8.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z2DeathL.append(img)

    loadScreen.text = 'z2HurtL'
    loadScreen.update(win)
    global z2HurtL
    z2HurtL = []
    img = pygame.image.load('zombie2/animation/Hurt1.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z2HurtL.append(img)
    img = pygame.image.load('zombie2/animation/Hurt2.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z2HurtL.append(img)
    img = pygame.image.load('zombie2/animation/Hurt3.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z2HurtL.append(img)
    img = pygame.image.load('zombie2/animation/Hurt4.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z2HurtL.append(img)
    img = pygame.image.load('zombie2/animation/Hurt5.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z2HurtL.append(img)

    loadScreen.text = 'z2IdleL'
    loadScreen.update(win)
    global z2IdleL
    z2IdleL = []
    img = pygame.image.load('zombie2/animation/Idle1.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z2IdleL.append(img)
    img = pygame.image.load('zombie2/animation/Idle2.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z2IdleL.append(img)
    img = pygame.image.load('zombie2/animation/Idle3.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z2IdleL.append(img)
    img = pygame.image.load('zombie2/animation/Idle4.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z2IdleL.append(img)

    loadScreen.text = 'z2JumpL'
    loadScreen.update(win)
    global z2JumpL
    z2JumpL = []
    img = pygame.image.load('zombie2/animation/Jump1.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z2JumpL.append(img)
    img = pygame.image.load('zombie2/animation/Jump2.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z2JumpL.append(img)
    img = pygame.image.load('zombie2/animation/Jump3.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z2JumpL.append(img)
    img = pygame.image.load('zombie2/animation/Jump4.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z2JumpL.append(img)
    img = pygame.image.load('zombie2/animation/Jump5.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z2JumpL.append(img)
    img = pygame.image.load('zombie2/animation/Jump6.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z2JumpL.append(img)
    img = pygame.image.load('zombie2/animation/Jump7.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z2JumpL.append(img)

    loadScreen.text = 'z2RunL'
    loadScreen.update(win)
    global z2RunL
    z2RunL = []
    img = pygame.image.load('zombie2/animation/Run1.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z2RunL.append(img)
    img = pygame.image.load('zombie2/animation/Run2.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z2RunL.append(img)
    img = pygame.image.load('zombie2/animation/Run3.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z2RunL.append(img)
    img = pygame.image.load('zombie2/animation/Run4.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z2RunL.append(img)
    img = pygame.image.load('zombie2/animation/Run5.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z2RunL.append(img)
    img = pygame.image.load('zombie2/animation/Run6.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z2RunL.append(img)
    img = pygame.image.load('zombie2/animation/Run7.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z2RunL.append(img)
    img = pygame.image.load('zombie2/animation/Run8.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z2RunL.append(img)
    img = pygame.image.load('zombie2/animation/Run9.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z2RunL.append(img)
    img = pygame.image.load('zombie2/animation/Run10.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z2RunL.append(img)

    loadScreen.text = 'z2WalkL'
    loadScreen.update(win)
    global z2WalkL
    z2WalkL = []
    img = pygame.image.load('zombie2/animation/Walk1.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z2WalkL.append(img)
    img = pygame.image.load('zombie2/animation/Walk2.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z2WalkL.append(img)
    img = pygame.image.load('zombie2/animation/Walk3.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z2WalkL.append(img)
    img = pygame.image.load('zombie2/animation/Walk4.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z2WalkL.append(img)
    img = pygame.image.load('zombie2/animation/Walk5.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z2WalkL.append(img)
    img = pygame.image.load('zombie2/animation/Walk6.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z2WalkL.append(img)

    loadScreen.text = 'z3AttackL'
    loadScreen.update(win)
    global z3AttackL
    z3AttackL = []
    img = pygame.image.load('zombie3/animation/Attack1.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z3AttackL.append(img)
    img = pygame.image.load('zombie3/animation/Attack2.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z3AttackL.append(img)
    img = pygame.image.load('zombie3/animation/Attack3.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z3AttackL.append(img)
    img = pygame.image.load('zombie3/animation/Attack4.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z3AttackL.append(img)
    img = pygame.image.load('zombie3/animation/Attack5.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z3AttackL.append(img)
    img = pygame.image.load('zombie3/animation/Attack6.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z3AttackL.append(img)

    loadScreen.text = 'z3DeathL'
    loadScreen.update(win)
    global z3DeathL
    z3DeathL = []
    img = pygame.image.load('zombie3/animation/Dead1.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z3DeathL.append(img)
    img = pygame.image.load('zombie3/animation/Dead2.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z3DeathL.append(img)
    img = pygame.image.load('zombie3/animation/Dead3.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z3DeathL.append(img)
    img = pygame.image.load('zombie3/animation/Dead4.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z3DeathL.append(img)
    img = pygame.image.load('zombie3/animation/Dead5.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z3DeathL.append(img)
    img = pygame.image.load('zombie3/animation/Dead6.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z3DeathL.append(img)
    img = pygame.image.load('zombie3/animation/Dead7.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z3DeathL.append(img)
    img = pygame.image.load('zombie3/animation/Dead8.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z3DeathL.append(img)

    loadScreen.text = 'z3HurtL'
    loadScreen.update(win)
    global z3HurtL
    z3HurtL = []
    img = pygame.image.load('zombie3/animation/Hurt1.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z3HurtL.append(img)
    img = pygame.image.load('zombie3/animation/Hurt2.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z3HurtL.append(img)
    img = pygame.image.load('zombie3/animation/Hurt3.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z3HurtL.append(img)
    img = pygame.image.load('zombie3/animation/Hurt4.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z3HurtL.append(img)
    img = pygame.image.load('zombie3/animation/Hurt5.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z3HurtL.append(img)

    loadScreen.text = 'z3IdleL'
    loadScreen.update(win)
    global z3IdleL
    z3IdleL = []
    img = pygame.image.load('zombie3/animation/Idle1.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z3IdleL.append(img)
    img = pygame.image.load('zombie3/animation/Idle2.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z3IdleL.append(img)
    img = pygame.image.load('zombie3/animation/Idle3.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z3IdleL.append(img)
    img = pygame.image.load('zombie3/animation/Idle4.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z3IdleL.append(img)

    loadScreen.text = 'z3JumpL'
    loadScreen.update(win)
    global z3JumpL
    z3JumpL = []
    img = pygame.image.load('zombie3/animation/Jump1.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z3JumpL.append(img)
    img = pygame.image.load('zombie3/animation/Jump2.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z3JumpL.append(img)
    img = pygame.image.load('zombie3/animation/Jump3.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z3JumpL.append(img)
    img = pygame.image.load('zombie3/animation/Jump4.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z3JumpL.append(img)
    img = pygame.image.load('zombie3/animation/Jump5.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z3JumpL.append(img)
    img = pygame.image.load('zombie3/animation/Jump6.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z3JumpL.append(img)
    img = pygame.image.load('zombie3/animation/Jump7.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z3JumpL.append(img)

    loadScreen.text = 'z3RunL'
    loadScreen.update(win)
    global z3RunL
    z3RunL = []
    img = pygame.image.load('zombie3/animation/Run1.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z3RunL.append(img)
    img = pygame.image.load('zombie3/animation/Run2.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z3RunL.append(img)
    img = pygame.image.load('zombie3/animation/Run3.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z3RunL.append(img)
    img = pygame.image.load('zombie3/animation/Run4.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z3RunL.append(img)
    img = pygame.image.load('zombie3/animation/Run5.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z3RunL.append(img)
    img = pygame.image.load('zombie3/animation/Run6.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z3RunL.append(img)
    img = pygame.image.load('zombie3/animation/Run7.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z3RunL.append(img)
    img = pygame.image.load('zombie3/animation/Run8.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z3RunL.append(img)
    img = pygame.image.load('zombie3/animation/Run9.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z3RunL.append(img)
    img = pygame.image.load('zombie3/animation/Run10.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z3RunL.append(img)

    loadScreen.text = 'z3WalkL'
    loadScreen.update(win)
    global z3WalkL
    z3WalkL = []
    img = pygame.image.load('zombie3/animation/Walk1.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z3WalkL.append(img)
    img = pygame.image.load('zombie3/animation/Walk2.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z3WalkL.append(img)
    img = pygame.image.load('zombie3/animation/Walk3.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z3WalkL.append(img)
    img = pygame.image.load('zombie3/animation/Walk4.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z3WalkL.append(img)
    img = pygame.image.load('zombie3/animation/Walk5.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z3WalkL.append(img)
    img = pygame.image.load('zombie3/animation/Walk6.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    img = pygame.transform.flip(img, True, False)
    z3WalkL.append(img)

    loadScreen.text = 'z1AttackR'
    loadScreen.update(win)
    global z1AttackR
    z1AttackR = []
    img = pygame.image.load('zombie1/animation/Attack1.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z1AttackR.append(img)
    img = pygame.image.load('zombie1/animation/Attack2.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z1AttackR.append(img)
    img = pygame.image.load('zombie1/animation/Attack3.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z1AttackR.append(img)
    img = pygame.image.load('zombie1/animation/Attack4.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z1AttackR.append(img)
    img = pygame.image.load('zombie1/animation/Attack5.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z1AttackR.append(img)
    img = pygame.image.load('zombie1/animation/Attack6.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z1AttackR.append(img)

    loadScreen.text = 'z1DeathR'
    loadScreen.update(win)
    global z1DeathR
    z1DeathR = []
    img = pygame.image.load('zombie1/animation/Dead1.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z1DeathR.append(img)
    img = pygame.image.load('zombie1/animation/Dead2.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z1DeathR.append(img)
    img = pygame.image.load('zombie1/animation/Dead3.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z1DeathR.append(img)
    img = pygame.image.load('zombie1/animation/Dead4.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z1DeathR.append(img)
    img = pygame.image.load('zombie1/animation/Dead5.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z1DeathR.append(img)
    img = pygame.image.load('zombie1/animation/Dead6.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z1DeathR.append(img)
    img = pygame.image.load('zombie1/animation/Dead7.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z1DeathR.append(img)
    img = pygame.image.load('zombie1/animation/Dead8.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z1DeathR.append(img)

    loadScreen.text = 'z1HurtR'
    loadScreen.update(win)
    global z1HurtR
    z1HurtR = []
    img = pygame.image.load('zombie1/animation/Hurt1.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z1HurtR.append(img)
    img = pygame.image.load('zombie1/animation/Hurt2.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z1HurtR.append(img)
    img = pygame.image.load('zombie1/animation/Hurt3.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z1HurtR.append(img)
    img = pygame.image.load('zombie1/animation/Hurt4.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z1HurtR.append(img)
    img = pygame.image.load('zombie1/animation/Hurt5.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z1HurtR.append(img)

    loadScreen.text = 'z1IdleR'
    loadScreen.update(win)
    global z1IdleR
    z1IdleR = []
    img = pygame.image.load('zombie1/animation/Idle1.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z1IdleR.append(img)
    img = pygame.image.load('zombie1/animation/Idle2.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z1IdleR.append(img)
    img = pygame.image.load('zombie1/animation/Idle3.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z1IdleR.append(img)
    img = pygame.image.load('zombie1/animation/Idle4.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z1IdleR.append(img)

    loadScreen.text = 'z1JumpR'
    loadScreen.update(win)
    global z1JumpR
    z1JumpR = []
    img = pygame.image.load('zombie1/animation/Jump1.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z1JumpR.append(img)
    img = pygame.image.load('zombie1/animation/Jump2.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z1JumpR.append(img)
    img = pygame.image.load('zombie1/animation/Jump3.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z1JumpR.append(img)
    img = pygame.image.load('zombie1/animation/Jump4.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z1JumpR.append(img)
    img = pygame.image.load('zombie1/animation/Jump5.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z1JumpR.append(img)
    img = pygame.image.load('zombie1/animation/Jump6.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z1JumpR.append(img)
    img = pygame.image.load('zombie1/animation/Jump7.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z1JumpR.append(img)

    loadScreen.text = 'z1RunR'
    loadScreen.update(win)
    global z1RunR
    z1RunR = []
    img = pygame.image.load('zombie1/animation/Run1.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z1RunR.append(img)
    img = pygame.image.load('zombie1/animation/Run2.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z1RunR.append(img)
    img = pygame.image.load('zombie1/animation/Run3.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z1RunR.append(img)
    img = pygame.image.load('zombie1/animation/Run4.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z1RunR.append(img)
    img = pygame.image.load('zombie1/animation/Run5.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z1RunR.append(img)
    img = pygame.image.load('zombie1/animation/Run6.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z1RunR.append(img)
    img = pygame.image.load('zombie1/animation/Run7.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z1RunR.append(img)
    img = pygame.image.load('zombie1/animation/Run8.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z1RunR.append(img)
    img = pygame.image.load('zombie1/animation/Run9.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z1RunR.append(img)
    img = pygame.image.load('zombie1/animation/Run10.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z1RunR.append(img)

    loadScreen.text = 'z1WalkR'
    loadScreen.update(win)
    global z1WalkR
    z1WalkR = []
    img = pygame.image.load('zombie1/animation/Walk1.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z1WalkR.append(img)
    img = pygame.image.load('zombie1/animation/Walk2.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z1WalkR.append(img)
    img = pygame.image.load('zombie1/animation/Walk3.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z1WalkR.append(img)
    img = pygame.image.load('zombie1/animation/Walk4.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z1WalkR.append(img)
    img = pygame.image.load('zombie1/animation/Walk5.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z1WalkR.append(img)
    img = pygame.image.load('zombie1/animation/Walk6.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z1WalkR.append(img)

    loadScreen.text = 'z2AttackR'
    loadScreen.update(win)
    global z2AttackR
    z2AttackR = []
    img = pygame.image.load('zombie2/animation/Attack1.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z2AttackR.append(img)
    img = pygame.image.load('zombie2/animation/Attack2.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z2AttackR.append(img)
    img = pygame.image.load('zombie2/animation/Attack3.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z2AttackR.append(img)
    img = pygame.image.load('zombie2/animation/Attack4.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z2AttackR.append(img)
    img = pygame.image.load('zombie2/animation/Attack5.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z2AttackR.append(img)
    img = pygame.image.load('zombie2/animation/Attack6.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z2AttackR.append(img)

    loadScreen.text = 'z2DeathR'
    loadScreen.update(win)
    global z2DeathR
    z2DeathR = []
    img = pygame.image.load('zombie2/animation/Dead1.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z2DeathR.append(img)
    img = pygame.image.load('zombie2/animation/Dead2.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z2DeathR.append(img)
    img = pygame.image.load('zombie2/animation/Dead3.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z2DeathR.append(img)
    img = pygame.image.load('zombie2/animation/Dead4.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z2DeathR.append(img)
    img = pygame.image.load('zombie2/animation/Dead5.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z2DeathR.append(img)
    img = pygame.image.load('zombie2/animation/Dead6.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z2DeathR.append(img)
    img = pygame.image.load('zombie2/animation/Dead7.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z2DeathR.append(img)
    img = pygame.image.load('zombie2/animation/Dead8.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z2DeathR.append(img)

    loadScreen.text = 'z2HurtR'
    loadScreen.update(win)
    global z2HurtR
    z2HurtR = []
    img = pygame.image.load('zombie2/animation/Hurt1.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z2HurtR.append(img)
    img = pygame.image.load('zombie2/animation/Hurt2.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z2HurtR.append(img)
    img = pygame.image.load('zombie2/animation/Hurt3.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z2HurtR.append(img)
    img = pygame.image.load('zombie2/animation/Hurt4.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z2HurtR.append(img)
    img = pygame.image.load('zombie2/animation/Hurt5.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z2HurtR.append(img)

    loadScreen.text = 'z2IdleR'
    loadScreen.update(win)
    global z2IdleR
    z2IdleR = []
    img = pygame.image.load('zombie2/animation/Idle1.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z2IdleR.append(img)
    img = pygame.image.load('zombie2/animation/Idle2.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z2IdleR.append(img)
    img = pygame.image.load('zombie2/animation/Idle3.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z2IdleR.append(img)
    img = pygame.image.load('zombie2/animation/Idle4.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z2IdleR.append(img)

    loadScreen.text = 'z2JumpR'
    loadScreen.update(win)
    global z2JumpR
    z2JumpR = []
    img = pygame.image.load('zombie2/animation/Jump1.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z2JumpR.append(img)
    img = pygame.image.load('zombie2/animation/Jump2.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z2JumpR.append(img)
    img = pygame.image.load('zombie2/animation/Jump3.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z2JumpR.append(img)
    img = pygame.image.load('zombie2/animation/Jump4.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z2JumpR.append(img)
    img = pygame.image.load('zombie2/animation/Jump5.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z2JumpR.append(img)
    img = pygame.image.load('zombie2/animation/Jump6.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z2JumpR.append(img)
    img = pygame.image.load('zombie2/animation/Jump7.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z2JumpR.append(img)

    loadScreen.text = 'z2RunR'
    loadScreen.update(win)
    global z2RunR
    z2RunR = []
    img = pygame.image.load('zombie2/animation/Run1.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z2RunR.append(img)
    img = pygame.image.load('zombie2/animation/Run2.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z2RunR.append(img)
    img = pygame.image.load('zombie2/animation/Run3.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z2RunR.append(img)
    img = pygame.image.load('zombie2/animation/Run4.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z2RunR.append(img)
    img = pygame.image.load('zombie2/animation/Run5.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z2RunR.append(img)
    img = pygame.image.load('zombie2/animation/Run6.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z2RunR.append(img)
    img = pygame.image.load('zombie2/animation/Run7.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z2RunR.append(img)
    img = pygame.image.load('zombie2/animation/Run8.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z2RunR.append(img)
    img = pygame.image.load('zombie2/animation/Run9.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z2RunR.append(img)
    img = pygame.image.load('zombie2/animation/Run10.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z2RunR.append(img)

    loadScreen.text = 'z2WalkR'
    loadScreen.update(win)
    global z2WalkR
    z2WalkR = []
    img = pygame.image.load('zombie2/animation/Walk1.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z2WalkR.append(img)
    img = pygame.image.load('zombie2/animation/Walk2.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z2WalkR.append(img)
    img = pygame.image.load('zombie2/animation/Walk3.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z2WalkR.append(img)
    img = pygame.image.load('zombie2/animation/Walk4.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z2WalkR.append(img)
    img = pygame.image.load('zombie2/animation/Walk5.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z2WalkR.append(img)
    img = pygame.image.load('zombie2/animation/Walk6.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z2WalkR.append(img)

    loadScreen.text = 'z3AttackR'
    loadScreen.update(win)
    global z3AttackR
    z3AttackR = []
    img = pygame.image.load('zombie3/animation/Attack1.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z3AttackR.append(img)
    img = pygame.image.load('zombie3/animation/Attack2.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z3AttackR.append(img)
    img = pygame.image.load('zombie3/animation/Attack3.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z3AttackR.append(img)
    img = pygame.image.load('zombie3/animation/Attack4.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z3AttackR.append(img)
    img = pygame.image.load('zombie3/animation/Attack5.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z3AttackR.append(img)
    img = pygame.image.load('zombie3/animation/Attack6.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z3AttackR.append(img)

    loadScreen.text = 'z3DeathR'
    loadScreen.update(win)
    global z3DeathR
    z3DeathR = []
    img = pygame.image.load('zombie3/animation/Dead1.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z3DeathR.append(img)
    img = pygame.image.load('zombie3/animation/Dead2.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z3DeathR.append(img)
    img = pygame.image.load('zombie3/animation/Dead3.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z3DeathR.append(img)
    img = pygame.image.load('zombie3/animation/Dead4.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z3DeathR.append(img)
    img = pygame.image.load('zombie3/animation/Dead5.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z3DeathR.append(img)
    img = pygame.image.load('zombie3/animation/Dead6.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z3DeathR.append(img)
    img = pygame.image.load('zombie3/animation/Dead7.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z3DeathR.append(img)
    img = pygame.image.load('zombie3/animation/Dead8.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z3DeathR.append(img)

    loadScreen.text = 'z3HurtR'
    loadScreen.update(win)
    global z3HurtR
    z3HurtR = []
    img = pygame.image.load('zombie3/animation/Hurt1.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z3HurtR.append(img)
    img = pygame.image.load('zombie3/animation/Hurt2.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z3HurtR.append(img)
    img = pygame.image.load('zombie3/animation/Hurt3.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z3HurtR.append(img)
    img = pygame.image.load('zombie3/animation/Hurt4.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z3HurtR.append(img)
    img = pygame.image.load('zombie3/animation/Hurt5.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z3HurtR.append(img)

    loadScreen.text = 'z3IdleR'
    loadScreen.update(win)
    global z3IdleR
    z3IdleR = []
    img = pygame.image.load('zombie3/animation/Idle1.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z3IdleR.append(img)
    img = pygame.image.load('zombie3/animation/Idle2.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z3IdleR.append(img)
    img = pygame.image.load('zombie3/animation/Idle3.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z3IdleR.append(img)
    img = pygame.image.load('zombie3/animation/Idle4.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z3IdleR.append(img)

    loadScreen.text = 'z3JumpR'
    loadScreen.update(win)
    global z3JumpR
    z3JumpR = []
    img = pygame.image.load('zombie3/animation/Jump1.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z3JumpR.append(img)
    img = pygame.image.load('zombie3/animation/Jump2.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z3JumpR.append(img)
    img = pygame.image.load('zombie3/animation/Jump3.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z3JumpR.append(img)
    img = pygame.image.load('zombie3/animation/Jump4.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z3JumpR.append(img)
    img = pygame.image.load('zombie3/animation/Jump5.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z3JumpR.append(img)
    img = pygame.image.load('zombie3/animation/Jump6.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z3JumpR.append(img)
    img = pygame.image.load('zombie3/animation/Jump7.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z3JumpR.append(img)

    loadScreen.text = 'z3RunR'
    loadScreen.update(win)
    global z3RunR
    z3RunR = []
    img = pygame.image.load('zombie3/animation/Run1.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z3RunR.append(img)
    img = pygame.image.load('zombie3/animation/Run2.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z3RunR.append(img)
    img = pygame.image.load('zombie3/animation/Run3.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z3RunR.append(img)
    img = pygame.image.load('zombie3/animation/Run4.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z3RunR.append(img)
    img = pygame.image.load('zombie3/animation/Run5.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z3RunR.append(img)
    img = pygame.image.load('zombie3/animation/Run6.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z3RunR.append(img)
    img = pygame.image.load('zombie3/animation/Run7.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z3RunR.append(img)
    img = pygame.image.load('zombie3/animation/Run8.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z3RunR.append(img)
    img = pygame.image.load('zombie3/animation/Run9.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z3RunR.append(img)
    img = pygame.image.load('zombie3/animation/Run10.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z3RunR.append(img)

    loadScreen.text = 'z3WalkR'
    loadScreen.update(win)
    global z3WalkR
    z3WalkR = []
    img = pygame.image.load('zombie3/animation/Walk1.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z3WalkR.append(img)
    img = pygame.image.load('zombie3/animation/Walk2.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z3WalkR.append(img)
    img = pygame.image.load('zombie3/animation/Walk3.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z3WalkR.append(img)
    img = pygame.image.load('zombie3/animation/Walk4.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z3WalkR.append(img)
    img = pygame.image.load('zombie3/animation/Walk5.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z3WalkR.append(img)
    img = pygame.image.load('zombie3/animation/Walk6.png')
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))
    z3WalkR.append(img)

    global attackL
    global attackR
    global idleL
    global idleR
    global jumpR
    global jumpL
    global hurtL
    global hurtR
    global dieL
    global dieR
    global runL
    global runR
    global walkL
    global walkR
    walkL = [z1WalkL, z2WalkL, z3WalkL]
    walkR = [z1WalkR, z2WalkR, z3WalkR]
    attackL = [z1AttackL, z2AttackL, z3AttackL]
    attackR = [z1AttackR, z2AttackR, z3AttackR]
    idleL = [z1IdleL, z2IdleL, z3IdleL]
    idleR = [z1IdleR, z2IdleR, z3IdleR]
    jumpR = [z1JumpR, z2JumpR, z3JumpR]
    jumpL = [z1JumpL, z2JumpL, z3JumpL]
    hurtL = [z1HurtL, z2HurtL, z3HurtL]
    hurtR = [z1HurtR, z2HurtR, z3HurtR]
    dieR = [z1DeathR, z2DeathR, z3DeathR]
    dieL = [z1DeathL, z2DeathL, z3DeathL]
    runL = [z1RunL, z2RunL, z3RunL]
    runR = [z1RunR, z2RunR, z3RunR]
loadScreen.text = 'Player Images'
loadScreen.update(win)
loadShit()
loadScreen.text = 'Whole lot of Zombies'
loadScreen.update(win)
loadZombies()

print('Loading Time:', time.time()-timeStart, 'seconds')
loading = False

def drawTop(man, win, score, money):
    scoreText = myFont.render('Score '+str(score), True, (255,255,255))
    win.blit(scoreText, (10, 10))
    if man.health > 0:
        pygame.draw.rect(win, (0,255,0), pygame.Rect(100, 10, man.health*2,20))
    if man.health< 200:
        pygame.draw.rect(win, (255,0,0), pygame.Rect(100+man.health*2,10, 400-man.health*2, 20))
    moneyText = myFont.render('Money '+str(money), True, (0,255,0))
    w, ignore = moneyText.get_rect().size
    win.blit(moneyText, (screenWidth-10-w, 10))

def drawPlayStuff():
    global gameScreen, homeButtons, playing, end, wave, waveTimer, waveText
    if playing:
        win.blit(background, (0, 0))
        if waveTimer > 0:
            waveText[wave-1].set_alpha(waveTimer)
            win.blit(waveText[wave-1], (100,100))
            waveTimer -= 1
        for zombie in zombies:
            if zombie.draw(win):
                zombies.remove(zombie)
        for i in bullets:
            if i.draw(win):
                bullets.remove(i)
        man.draw(win)
        drawTop(man, win, score, money)
    else:
        gameOver = font.render('Game Over', False, (255,0,0))
        win.blit(gameOver, (50,50))

def drawHomeStuff(homeButtons):
    global playing, end, gameScreen
    win.blit(background, (0,0))
    text = titleFont.render('Zombie Survival', True, (255,50,50))
    w, h = text.get_rect().size
    win.blit(text, ((screenWidth-w)/2, 50))
    for button in homeButtons:
        button.update(win)
    if homeButtons[0].clicked():
        gameScreen = 'play'
    if homeButtons[1].clicked():
        gameScreen = 'play'
        end = False
        playing = False

shopDispCounter = 255
notEnoughMoney = False
maxHealth = False

def drawShopStuff():
    global gameScreen, shopButtons, money, shopDispCounter, notEnoughMoney, maxHealth
    win.blit(background, (0,0))
    drawTop(man, win, score, money)
    backBtn.update(win)
    if maxHealth:
        shopDispCounter -= 2
        text = font.render('Already Max Health', True, (255,255,255))
        surface = pygame.Surface(text.get_rect().size)
        surface.fill((0,0,0))
        surface.blit(text, (0,0))
        surface.set_alpha(shopDispCounter)
        win.blit(surface, (110, screenHeight-50))
    elif notEnoughMoney:
        shopDispCounter -= 2
        text = font.render('Not Enough Money', True, (255,0,0))
        surface = pygame.Surface(text.get_rect().size)
        surface.fill((0,0,0))
        surface.blit(text, (0,0))
        surface.set_alpha(shopDispCounter)
        win.blit(surface, (110, screenHeight-50))
    if shopDispCounter <= 1:
        shopDispCounter = 255
        maxHealth = False
        notEnoughMoney = False
    for button in shopButtons:
        button.update(win)
    if shopButtons[0].clicked(): #Health
        if man.health < 200:
            if money >= 20:
                man.health += 10
                money -= 20
            else:
                notEnoughMoney = True
                shopDispCounter = 255
        else:
            maxHealth = True
            shopDispCounter = 255
        time.sleep(.2) #So that it doesn't register multiple clicks
    if backBtn.clicked():
        gameScreen = 'betweenWave'

def drawBetweenThings():
    global betweenBtns, man, score, gameScreen, playing, end
    win.blit(background, (0,0))
    text = titleFont.render('Wave Complete', True, (255,0,0))
    w, h = text.get_rect().size
    win.blit(text, ((screenWidth-w)/2, 50))
    for button in betweenBtns:
        button.update(win)
    if betweenBtns[0].clicked():
        gameScreen = 'play'
    if betweenBtns[1].clicked():
        gameScreen = 'shop'
    if betweenBtns[2].clicked():
        gameScreen = 'play'
        end = False
        playing = False
    drawTop(man, win, score, money)

def redraw():
    global gameScreen, homeButtons, playing, end, wave, waveTimer, waveText
    screenWidth, screenHeight = pygame.display.get_surface().get_size()
    if not pygame.mixer.music.get_busy():
        pygame.mixer.music.load(songs[randint(0,len(songs)-1)])
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play()
    if gameScreen == 'play':
        drawPlayStuff()
    elif gameScreen == 'home':
        drawHomeStuff(homeButtons)
    elif gameScreen == 'shop':
        drawShopStuff()
    elif gameScreen == 'betweenWave':
        drawBetweenThings()
    pygame.display.update()

class Person:
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

    def draw(self, win):
        if self.walkCount + 1 >= 28:
            self.walkCount = 0

        if not self.standing:
            if self.left:
                win.blit(walkLeft[self.walkCount // 4], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount // 4], (self.x, self.y))
                self.walkCount += 1
        else:
            if self.left:
                win.blit(walkLeft[0], (self.x, self.y))
            else:
                win.blit(walkRight[0], (self.x, self.y))

class Zombie: #Can run, walk, jump, idle, attack, be hurt, die
    global man, bullets, zombies, zombieCount, score, playing, end
    def __init__(self, x,y, type): #Need to add type for the 3 zombies
        self.x = x
        self.y = y
        self.type = type
        self.width = 97
        self.height = 144
        self.left = False
        self.right = False
        self.angry = False
        self.frameCount = 0
        self.frameCountMax = 0
        self.frameStart = 0
        self.health=100
        self.actions = ['run', 'walk', 'jump', 'idle', 'attack', 'hurt', 'die']
        self.actions = ActionOrganizer(self.actions)
        self.speed = 12
        self.numUps = 0
        self.isDead = False
        if x == -100:
            self.right = True
        else:
            self.left = True
    def die(self):
        action = self.actions.getTrue()
        self.actions.bool[self.actions.actions.index(action)] = False
        self.actions.bool[6] = True
        self.isDead = True
        self.frameCount = 0
    def hurt(self):
        action = self.actions.getTrue()
        self.actions.bool[self.actions.actions.index(action)] = False
        self.actions.bool[5] = True
        self.frameCount = 0
    def setAction(self):
        action = self.actions.getTrue()
        if not self.isDead and action not in ['attack', 'hurt', 'jump']:
            if self.x < man.x:
                self.right = True
                self.left = False
            else:
                self.left = True
                self.right = False
            if abs((self.x + self.width//2) - (man.x+man.width//2)) < 75:
                self.actions.bool[self.actions.actions.index(action)] = False
                self.actions.bool[4] = True #Sets action to attack
                self.frameCount = 0 #Resets framecount so it's at beginning of attack
            elif randint(1,200) == 1: #Jump
                self.actions.bool[self.actions.actions.index(action)] = False
                self.actions.bool[2] = True #Sets action to jump
                self.frameCount = 0
            #    print('begin jump')
            else: #Sets back to either walk or run, whatever it initially was
                self.actions.bool[self.actions.actions.index(action)] = False
                self.actions.bool[self.actions.initial] = True
    def draw(self, win):
        action = self.actions.getTrue()

        if self.frameCount+1 >= self.frameCountMax * self.speed:
        #    print(self.frameCount)
            self.frameCount = self.frameStart
            if action == 'die':
                return True
        if action == 'run':
            self.frameCountMax =  len(z1RunL)-1
            self.frameStart = 5*self.speed
            if self.right:
                img = runR[self.type][self.frameCount//self.speed]
                ignore, imgY = img.get_rect().size
                self.x += 2
                win.blit(img, (self.x, self.y-imgY))
            else:
                img = runL[self.type][self.frameCount//self.speed]
                ignore, imgY = img.get_rect().size
                self.x -= 2
                win.blit(img, (self.x, self.y-imgY))
            self.frameCount += 1
        elif action == 'walk':
            self.frameCountMax = len(z1WalkL)-1
            self.frameStart = 0
            if self.right:
                img = walkR[self.type][self.frameCount//self.speed]
                ignore, imgY = img.get_rect().size
                self.x += .5
                win.blit(img, (self.x, self.y-imgY))
            else:
                img = walkL[self.type][self.frameCount//self.speed]
                ignore, imgY = img.get_rect().size
                self.x -= .5
                win.blit(img, (self.x, self.y-imgY))
            self.frameCount += 1
        elif action == 'jump':
            self.frameCountMax = len(z1JumpL)-1
            self.frameStart = 0
            if self.frameCount//self.speed >= 1 and self.frameCount//self.speed <= 3:
                self.y -= 5
                self.numUps += 1
            else:
                if self.numUps > 0:
                    self.y += 5
                    self.numUps -= 1
                if self.frameCount == 70:
                    while self.numUps > 0:
                        self.y += 5
                        self.numUps -= 1
                    self.actions.bool[2] = False
                    self.frameCount = -1
            #        print("end jump")
            if self.right:
                img = jumpR[self.type][self.frameCount//self.speed]
                ignore, imgY = img.get_rect().size
                self.x += 3
                win.blit(img, (self.x, self.y-imgY))
            else:
                img = jumpL[self.type][self.frameCount//self.speed]
                ignore, imgY = img.get_rect().size
                self.x -= 3
                win.blit(img, (self.x, self.y-imgY))
            self.frameCount += 1
        elif action == 'idle':
            self.frameCountMax = len(z1IdleL)-1
            self.frameStart = 0
            if self.right:
                img = idleR[self.type][self.frameCount//self.speed]
                ignore, imgY = img.get_rect().size
                win.blit(img, (self.x, self.y-imgY))
            else:
                img = idleL[self.type][self.frameCount//self.speed]
                ignore, imgY = img.get_rect().size
                win.blit(img, (self.x, self.y-imgY))
            self.frameCount += 1
        elif action == 'attack':
            self.frameCountMax = len(z1AttackL)-1
            self.frameStart = 0
            if self.frameCount//self.speed == 1 and abs((self.x + self.width//2) - (man.x+man.width//2)) < 90 and man.y > screenHeight - 250:
                man.health -= 1
            if self.right:
                img = attackR[self.type][self.frameCount//self.speed]
                ignore, imgY = img.get_rect().size
                win.blit(img, (self.x, self.y-imgY))
            else:
                img = attackL[self.type][self.frameCount//self.speed]
                ignore, imgY = img.get_rect().size
                win.blit(img, (self.x, self.y-imgY))
            self.frameCount += 1
            if self.frameCount//self.speed == 4:
                self.actions.bool[4] = False #Sets attack to False
        elif action == 'hurt':
            self.frameCountMax = len(z1HurtL)-1
            self.frameStart = 0
            if self.right:
                img = hurtR[self.type][self.frameCount//self.speed]
                ignore, imgY = img.get_rect().size
                win.blit(img, (self.x, self.y-imgY))
            else:
                img = hurtL[self.type][self.frameCount//self.speed]
                ignore, imgY = img.get_rect().size
                win.blit(img, (self.x, self.y-imgY))
            self.frameCount += 1
            if self.frameCount == 47:
                self.actions.bool[5] = False
        elif action == 'die':
            self.frameCountMax = len(z1DeathL)-1
            self.frameStart = 0
            if self.right:
                img = dieR[self.type][self.frameCount//self.speed]
                ignore, imgY = img.get_rect().size
                win.blit(img, (self.x, self.y-imgY))
            else:
                img = dieL[self.type][self.frameCount//self.speed]
                ignore, imgY = img.get_rect().size
                win.blit(img, (self.x, self.y-imgY))
            self.frameCount += 1
        if self.health < 100 and action != 'die':
            pygame.draw.rect(win, (0,255,0), pygame.Rect(self.x, self.y-self.height-20,self.health, 10))
            pygame.draw.rect(win, (255,0,0), pygame.Rect(self.x+self.health, self.y-self.height-20,100-self.health,10))

class ActionOrganizer:
    def __init__(self,actions):
        self.actions = actions
        self.bool = []
        for i in actions:
            self.bool.append(False)
        self.initial = randint(0,1)
        self.bool[self.initial] = True
    def getTrue(self):
        for i in range(0,len(self.actions)-1):
            if self.bool[i]:
                return self.actions[i]
        return self.actions[-1] #Used for zombies

class Bullet:
    def __init__(self, x, y, left):
        self.x = x
        self.y = y
        self.left = left

    def draw(self, win):
        if self.left:
            self.x -= 10
            win.blit(bulletLeft, (self.x, self.y))
        else:
            self.x += 10
            win.blit(bulletRight, (self.x, self.y))
        if self.x > screenWidth or self.x < 0:
            return True

def initV():
    global man, bullets, zombies, score, playing, end, wave, waveTimer, money

    man = Person(screenWidth // 2 - 48 / 2, screenHeight - 175, 96, 112)
    bullets = []
    zombies = []
    score = 39
    money = 0
    playing = True
    end = True
    wave = 1
    waveTimer = 255

def newWave(wave):
    global gameScreen, zombies, man, bullets
    zombies = []
    bullets = []
    man.x = screenWidth // 2 - 48
    man.y = screenHeight - 175
    wave += 1
    waveTimer = 255
    gameScreen = 'betweenWave'
    return wave, waveTimer
# MAIN LOOP
def main():
    global man, bullets, zombies, score, playing, end, wave, waveTimer, gameScreen, money

    shotTimer = 0
    zombieTimer = 0
    zombieTimerEnd = 50
    zombieCount = 1

    while playing:
        clock.tick(56)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
                end = False

        if gameScreen == 'play':
            if wave == 1:
                if score < 3:
                    zombieCount = 1
                elif score < 10:
                    zombieCount = 3
                elif score < 30:
                    zombieCount = 5
                elif score == 40:
                    wave, waveTimer = newWave(wave)
            if wave == 2:
                if score < 50:
                    zombieCount = 5
                elif score < 60:
                    zombieTimerEnd = 30
                elif score < 70:
                    zombieCount = 6
                elif score == 80:
                    wave, waveTimer = newWave(wave)
            if wave == 3:
                if score < 50:
                    zombieCount = 5
                elif score < 60:
                    zombieTimerEnd = 30
                elif score < 70:
                    zombieCount = 6
                elif score == 80:
                    wave, waveTimer = newWave(wave)
            if len(zombies) < zombieCount and zombieTimer >= zombieTimerEnd:
                x = randint(1,2)
                if x == 1:
                    zombie = Zombie(-100,screenHeight-30, randint(0,2))
                    zombies.append(zombie)
                if x == 2:
                    zombie = Zombie(screenWidth, screenHeight-30, randint(0,2))
                    zombies.append(zombie)
                zombieTimer = 0
            zombieTimer += 1
            for bullet in bullets:
                for zombie in zombies:
                    if bullet.x > zombie.x and bullet.x < zombie.x+zombie.width and bullet.y < zombie.y and bullet.y > zombie.y-zombie.height and zombie.isDead == False:
                        #hit
                        sounds['hit'].play()
                        bullets.remove(bullet)
                        if zombie.health <= 20:
                            zombie.die()
                            score += 1
                            money += 5
                        else:
                            zombie.health -= 20
                            if randint(1,5) == 1 and not zombie.actions.bool[2]: #Makes sure not in middle of jumping
                                zombie.hurt()
                        break
            for zombie in zombies:
                zombie.setAction()
            if man.health <= 0:
                playing = False

            keys = pygame.key.get_pressed()

            if keys[pygame.K_SPACE]:
                if shotTimer > man.shotDelay:
                    sounds['shot'].play()
                    bullets.append(Bullet(man.x + man.width / 2, man.y + 50, man.left))
                    shotTimer = 0
            if shotTimer < 200:
                shotTimer += 1
            if keys[pygame.K_LEFT] and man.x > man.vel:
                man.left = True
                man.right = False
                man.standing = False
                man.x -= man.vel
            elif keys[pygame.K_RIGHT] and man.x < screenWidth - man.width - man.vel:
                man.right = True
                man.left = False
                man.x += man.vel
                man.standing = False
            else:
                man.standing = True
                man.walkCount = 0
            if not man.isJump:
                if keys[pygame.K_UP]:
                    man.isJump = True
            else:
                man.y -= man.jumpAcc
                if man.jumpAcc > -20:
                    man.jumpAcc -= 1
                else:
                    man.jumpAcc = 20
                    man.isJump = False
        redraw()

    while end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            end = False
        redraw()
initV()
main()
pygame.quit()
