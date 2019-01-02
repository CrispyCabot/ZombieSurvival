# Shooting game
import pygame
from random import randint

pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.mixer.init()
pygame.init()

myFont = pygame.font.Font('28DaysLater.ttf', 22) #Score Font
font = pygame.font.Font('28DaysLater.ttf', 36) #Game Over Font

screenWidth = 800
screenHeight = 500

win = pygame.display.set_mode((screenWidth, screenHeight), pygame.RESIZABLE)

pygame.display.set_caption('Zombie Survival')

clock = pygame.time.Clock()

def loadShit():
    global background
    global bulletImg
    global bulletLeft
    global bulletRight
    global walkLeft
    global walkRight
    global sounds
    background = pygame.image.load('images/background.jpg')
    background = pygame.transform.scale(background, (screenWidth, screenHeight))
    bulletImg = pygame.image.load('images/bullet.png')
    bulletLeft = pygame.transform.scale(bulletImg, (15, 7))
    bulletRight = pygame.transform.flip(bulletLeft, True, False)

    walkLeft = [pygame.image.load('char/p0.png'), pygame.image.load('char/p1.png'),
                pygame.image.load('char/p2.png'), pygame.image.load('char/p3.png'),
                pygame.image.load('char/p4.png'), pygame.image.load('char/p5.png'),
                pygame.image.load('char/p6.png')]
    walkRight = [pygame.image.load('char/r0.png'), pygame.image.load('char/r1.png'),
                 pygame.image.load('char/r2.png'), pygame.image.load('char/r3.png'),
                 pygame.image.load('char/r4.png'), pygame.image.load('char/r5.png'),
                 pygame.image.load('char/r6.png')]

    sounds = {'shot': pygame.mixer.Sound('sounds/bullet.wav'),
              'hit': pygame.mixer.Sound('sounds/hit.wav')}

#TO DO: ADD LOADING SCREEN
def loadZombies():
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
loadShit()
loadZombies()


def redraw():
    screenWidth, screenHeight = pygame.display.get_surface().get_size()
    if playing:
        win.blit(background, (0, 0))
        for zombie in zombies:
            if zombie.draw(win):
                zombies.remove(zombie)
        for i in bullets:
            if i.draw(win):
                bullets.remove(i)
        man.draw(win)

        scoreText = myFont.render('Score '+str(score), False, (255,255,255))
        win.blit(scoreText, (10, 10))
        if man.health > 0:
            pygame.draw.rect(win, (0,255,0), pygame.Rect(100, 10, man.health*2,20))
        if man.health< 100:
            pygame.draw.rect(win, (255,0,0), pygame.Rect(100+man.health*2,10, 200-man.health*2, 20))
    else:
        gameOver = font.render('Game Over', False, (255,0,0))
        win.blit(gameOver, (50,50))
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
        self.health=100

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
        if x == 0:
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
            if zombie.x < man.x:
                zombie.right = True
                zombie.left = False
            else:
                zombie.left = True
                zombie.right = False
            if abs((zombie.x + zombie.width//2) - (man.x+man.width//2)) < 75:
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
            if self.frameCount//self.speed == 1 and abs((zombie.x + zombie.width//2) - (man.x+man.width//2)) < 90 and man.y > screenHeight - 200:
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
            pygame.draw.rect(win, (0,255,0), pygame.Rect(self.x, self.y-20,self.health, 10))
            pygame.draw.rect(win, (255,0,0), pygame.Rect(self.x+self.health, self.y-20,100-self.health,10))

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
        return self.actions[-1]

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

man = Person(screenWidth // 2 - 96 / 2, screenHeight - 175, 96, 112)
bullets = []
shotTimer = 0
zombies = []
zombieCount = 1
zombieTimer = 0
score = 0

playing = True
end = True
# MAIN LOOP

while playing:
    clock.tick(56)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
            end = False

    if len(zombies) < zombieCount and zombieTimer >= 50:
        x = randint(1,2)
        if x == 1:
            zombie = Zombie(0,screenHeight-30, randint(0,2))
            zombies.append(zombie)
        if x == 2:
            zombie = Zombie(screenWidth, screenHeight-30, randint(0,2))
            zombies.append(zombie)
        zombieTimer = 0
    if zombieTimer < 110:
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
                else:
                    zombie.health -= 20
                    if randint(1,5) == 1 and not zombie.actions.bool[4]: #Makes sure not in middle of jumping
                        zombie.hurt()
                break
    for zombie in zombies:
        zombie.setAction()
    if man.health <= 0:
        playing = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        if shotTimer > 10:
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
pygame.quit()
