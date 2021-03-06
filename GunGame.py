# Shooting game
# Needs to be named GunGame.py or same length
# I'm pretty sure somewhere is hardcoded to chop off the name "GunGame"
import pygame
import time
import threading
from random import randint, choice
from sys import platform
import os
import math

from config import SCREEN_WIDTH, SCREEN_HEIGHT, PATH
from LoadingScreen import LoadingScreen

#Start scoreboard/google sheets stuff
try:
    import gspread
    from oauth2client.service_account import ServiceAccountCredentials
except ModuleNotFoundError:
    print("Something went wrong. Online leaderboard will not work.")

#End scoreboard/google sheets stuff

timeStart = time.time()

loading = True

pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.mixer.init()
pygame.init()

loadFont = pygame.font.Font(PATH+os.path.join('data', 'fonts', '28DaysLater.ttf'), 36)
loadFont2 = pygame.font.Font(PATH+os.path.join('data', 'fonts','28DaysLater.ttf'), 76)

clock = pygame.time.Clock()

win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #, pygame.RESIZABLE

pygame.display.set_caption('Zombie Survival')

loadZombie = [pygame.image.load(PATH+os.path.join('data', 'zombieLoading','tile000.png')), pygame.image.load(PATH+os.path.join('data', 'zombieLoading','tile001.png')),
                pygame.image.load(PATH+os.path.join('data', 'zombieLoading','tile002.png')), pygame.image.load(PATH+os.path.join('data', 'zombieLoading','tile003.png')),
                pygame.image.load(PATH+os.path.join('data', 'zombieLoading','tile004.png')), pygame.image.load(PATH+os.path.join('data', 'zombieLoading','tile005.png')),
                pygame.image.load(PATH+os.path.join('data', 'zombieLoading','tile006.png')), pygame.image.load(PATH+os.path.join('data', 'zombieLoading','tile007.png')),
                pygame.image.load(PATH+os.path.join('data', 'zombieLoading','tile008.png')), pygame.image.load(PATH+os.path.join('data', 'zombieLoading','tile009.png'))]

def zombieLoad():
    global loading, win
    speed = 5
    frameCount = 0
    while loading:
        text = loadFont2.render('Loading', True, (255,255,255))
        w, ignore = text.get_rect().size
        pygame.draw.rect(win, (0,0,0), pygame.Rect(0,0,SCREEN_WIDTH, SCREEN_HEIGHT-100))
        win.blit(text, ((SCREEN_WIDTH-w)/2, 15))
        img = loadZombie[frameCount//speed]
        imgW, imgH = img.get_rect().size
        win.blit(img, ((SCREEN_WIDTH-imgW)/2, (SCREEN_HEIGHT-imgH)/2))
        if frameCount+1 >= speed * len(loadZombie):
            frameCount = 0
        else:
            frameCount += 1
        clock.tick(60)
        pygame.display.update()

thread1 = threading.Thread(target=zombieLoad)
thread1.start()

loadScreen = LoadingScreen(win, SCREEN_WIDTH, SCREEN_HEIGHT, loadFont)

#Self made classes
from Button import Button
from ActionOrganizer import ActionOrganizer
from Bullet import Bullet #Loads bullets
from Grenade import Grenade #Loads grenades
loadScreen.text = 'Character'
loadScreen.update(win)
loadScreen.update(win)
from Person import Person #Update loading screen twice - loads character

loadScreen.text = 'Fonts'
loadScreen.update(win)

gameScreen = 'home'

myFont = pygame.font.Font(PATH+os.path.join('data', 'fonts','28DaysLater.ttf'), 22) #Score Font
font = pygame.font.Font(PATH+os.path.join('data', 'fonts','28DaysLater.ttf'), 36) #Game Over Font
plFont = pygame.font.Font(PATH+os.path.join('data', 'fonts','28DaysLater.ttf'), 56) #play font
plFont2 = pygame.font.Font(PATH+os.path.join('data', 'fonts','28DaysLater.ttf'), 60)
gameOverplFont = pygame.font.Font(PATH+os.path.join('data', 'fonts','28DaysLater.ttf'), 36) #game over screen play font
gameOverplFont2 = pygame.font.Font(PATH+os.path.join('data', 'fonts','28DaysLater.ttf'), 40)
splFont = pygame.font.Font(PATH+os.path.join('data', 'fonts','28DaysLater.ttf'), 36) #Shop/Quit font
splFont2 = pygame.font.Font(PATH+os.path.join('data', 'fonts','28DaysLater.ttf'), 40)
titleFont = pygame.font.Font(PATH+os.path.join('data', 'fonts','ZombieSlayer.ttf'), 70)
shopFont = pygame.font.Font(PATH+os.path.join('data', 'fonts','varsityteam.otf'), 20)
shopFont2 = pygame.font.Font(PATH+os.path.join('data', 'fonts','varsityteam.otf'), 24)
gameOverQuitFont = pygame.font.Font(PATH+os.path.join('data', 'fonts','28DaysLater.ttf'), 20) #Game over quit font
gameOverQuitFont2 = pygame.font.Font(PATH+os.path.join('data', 'fonts','28DaysLater.ttf'), 24)
scoreboardFont = pygame.font.Font(PATH+os.path.join('data', 'fonts','monofonto.ttf'), 24)
scoreboardFontBig = pygame.font.Font(PATH+os.path.join('data', 'fonts','monofonto.ttf'), 30)

loadScreen.text = 'Buttons'
loadScreen.update(win)

backBtn = Button(0,SCREEN_HEIGHT-50,100,50, [100,100,100], 'Back', splFont, [255,255,255], splFont2)
resume = Button((SCREEN_WIDTH - 300)/2,(SCREEN_HEIGHT-100)/2-30,300,100,[100,200,100], 'Resume', plFont, [0,0,0], plFont2)

def homeScreenLoad():
    global homeButtons
    homeButtons = []
    playBtn = Button((SCREEN_WIDTH - 200)/2,(SCREEN_HEIGHT-100)/2-30,200,100,[200,20,20], 'Play', plFont, [0,0,0], plFont2)
    homeButtons.append(playBtn)
    quitBtn = Button((SCREEN_WIDTH-200)/2, (SCREEN_HEIGHT-50)/2+50,200,50, [20,20,20], 'Quit', splFont, [150,150,150], splFont2)
    homeButtons.append(quitBtn)
homeScreenLoad()
loadScreen.update(win)
def betweenScreensLoad():
    global betweenBtns
    betweenBtns = []
    playBtn = Button((SCREEN_WIDTH - 220)/2,(SCREEN_HEIGHT-100)/2-30,220,100,[200,20,20], 'Continue', plFont, [0,0,0], plFont2)
    betweenBtns.append(playBtn)
    shopBtn = Button((SCREEN_WIDTH-100)/2-60, (SCREEN_HEIGHT-50)/2+50,100,50, [20,255,20], 'Shop', splFont, [0,0,0], splFont2)
    betweenBtns.append(shopBtn)
    quitBtn = Button((SCREEN_WIDTH-100)/2+60, (SCREEN_HEIGHT-50)/2+50,100,50, [20,20,20], 'Quit', splFont, [150,150,150], splFont2)
    betweenBtns.append(quitBtn)
betweenScreensLoad()
loadScreen.update(win)
def shopScreenLoad():
    global shopButtons
    shopButtons = []
    healthInc = Button((SCREEN_WIDTH-150)/2-300,75,150,25,[96,165,243], '$20 - Health', shopFont, [255,255,255], shopFont2)
    shopButtons.append(healthInc)
    grenade = Button((SCREEN_WIDTH-150)/2-120, 75,150,25, [45, 199, 78], '$75 - Grenade', shopFont, [255,255,255], shopFont2)
    shopButtons.append(grenade)
    weapons = Button((SCREEN_WIDTH-250)/2-200,150,250,50, [200, 100, 20], 'Weapons', shopFont, [255,255,255], shopFont2)
    shopButtons.append(weapons)
def weaponShopLoad():
    global weaponBtns
    weaponBtns = { 'laser':Button((SCREEN_WIDTH-250)/2-250,130,250,50,[200,200,200], '$200 - Laser Gun', shopFont, [10,10,10], shopFont2),
    'buy':Button((SCREEN_WIDTH-100)/2+200,SCREEN_HEIGHT-50,100,30,[20,100,20], 'BUY', shopFont, [255,255,255], shopFont2),
    'original':Button((SCREEN_WIDTH-250)/2-250,75,250,50,[200,200,200], '$50 - Original Gun', shopFont, [10,10,10], shopFont2),
    'machine':Button((SCREEN_WIDTH-250)/2-250,185,250,50,[200,200,200], '$300 - Machine Gun', shopFont, [10,10,10], shopFont2),
    'plasma':Button((SCREEN_WIDTH-250)/2-250,240,250,50,[200,200,200], '$600 - Plasma Rifle', shopFont, [10,10,10], shopFont2)}
weaponShopLoad()
shopScreenLoad()
def gameOverScreenLoad():
    global gameOverBtns
    gameOverBtns = []
    playBtn = Button((SCREEN_WIDTH - 200)/2,(SCREEN_HEIGHT-50)/2+180,200,50,[200,20,20], 'Play Again', gameOverplFont, [0,0,0], gameOverplFont2)
    gameOverBtns.append(playBtn)
    quitBtn = Button((SCREEN_WIDTH-200)/2, (SCREEN_HEIGHT-25)/2+232,200,25, [20,20,20], 'Quit', gameOverQuitFont, [150,150,150], gameOverQuitFont2)
    gameOverBtns.append(quitBtn)
gameOverScreenLoad()
loadScreen.update(win)
def loadStuff():
    global grenadeImg, background, bulletImg, bulletLeft, bulletRight, walkLeft, walkRight, sounds, songs, waveText, explosion, grenade
    global gunsL, gunsR
    background = pygame.image.load(PATH+os.path.join('data', 'images','background.jpg'))
    background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

    grenadeImg = pygame.image.load(PATH+os.path.join('data', 'images','grenade.png'))
    imgx, imgy = grenadeImg.get_rect().size
    grenadeImg = pygame.transform.scale(grenadeImg, (int(.04*imgx), int(.04*imgy)))

    #convert_alpha is supposed to allow me to use set_alpha later on, but it doesn't work so fuck it.
    waveText = [pygame.image.load(PATH+os.path.join('data', 'waveText','wave1.png')).convert_alpha(), pygame.image.load(PATH+os.path.join('data', 'waveText','wave2.png')).convert_alpha(),
                pygame.image.load(PATH+os.path.join('data', 'waveText','wave3.png')).convert_alpha(), pygame.image.load(PATH+os.path.join('data', 'waveText','wave4.png')).convert_alpha(),
                pygame.image.load(PATH+os.path.join('data', 'waveText','wave5.png')).convert_alpha(), pygame.image.load(PATH+os.path.join('data', 'waveText','wave6.png')).convert_alpha(),
                pygame.image.load(PATH+os.path.join('data', 'waveText','wave7.png')).convert_alpha(), pygame.image.load(PATH+os.path.join('data', 'waveText','wave8.png')).convert_alpha(),
                pygame.image.load(PATH+os.path.join('data', 'waveText','wave9.png')).convert_alpha(), pygame.image.load(PATH+os.path.join('data', 'waveText','wave10.png')).convert_alpha()]

    loadScreen.text = 'Weapons'
    loadScreen.update(win)

    loadScreen.text = 'Songs'
    loadScreen.update(win)

    songs = [PATH+os.path.join('data', 'songs','cant-go-to-hell.mp3'), PATH+os.path.join('data', 'songs','highway-to-hell.mp3'), PATH+os.path.join('data', 'songs','bloodwater.mp3')]

    sounds = {'shot': pygame.mixer.Sound(PATH+os.path.join('data', 'sounds','bullet.wav')),
              'hit': pygame.mixer.Sound(PATH+os.path.join('data', 'sounds','hit.wav')),
              'grenade': pygame.mixer.Sound(PATH+os.path.join('data', 'sounds','grenade.wav'))}
    sounds['hit'].set_volume(0.1)
    sounds['shot'].set_volume(0.5)
    sounds['grenade'].set_volume(0.5)

zombieWidth = 0
zombieHeight = 0

def loadZombies():
    global zombieWidth, zombieHeight
    scaler = .3
    loadScreen.text = 'z1AttackL'
    loadScreen.update(win)
    global z1AttackL
    z1AttackL = []
    img = pygame.image.load(PATH+os.path.join('data', 'zombie1','animation','Attack1.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z1AttackL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie1','animation','Attack2.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    zombieWidth, zombieHeight = img.get_rect().size
    img = pygame.transform.flip(img, True, False)
    z1AttackL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie1','animation','Attack3.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z1AttackL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie1','animation','Attack4.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z1AttackL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie1','animation','Attack5.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z1AttackL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie1','animation','Attack6.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z1AttackL.append(img)

    loadScreen.text = 'z1DeathL'
    loadScreen.update(win)
    global z1DeathL
    z1DeathL = []
    img = pygame.image.load(PATH+os.path.join('data', 'zombie1','animation','Dead1.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z1DeathL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie1','animation','Dead2.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z1DeathL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie1','animation','Dead3.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z1DeathL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie1','animation','Dead4.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z1DeathL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie1','animation','Dead5.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z1DeathL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie1','animation','Dead6.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z1DeathL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie1','animation','Dead7.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z1DeathL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie1','animation','Dead8.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z1DeathL.append(img)

    loadScreen.text = 'z1HurtL'
    loadScreen.update(win)
    global z1HurtL
    z1HurtL = []
    img = pygame.image.load(PATH+os.path.join('data', 'zombie1','animation','Hurt1.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z1HurtL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie1','animation','Hurt2.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z1HurtL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie1','animation','Hurt3.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z1HurtL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie1','animation','Hurt4.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z1HurtL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie1','animation','Hurt5.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z1HurtL.append(img)

    loadScreen.text = 'z1IdleL'
    loadScreen.update(win)
    global z1IdleL
    z1IdleL = []
    img = pygame.image.load(PATH+os.path.join('data', 'zombie1','animation','Idle1.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z1IdleL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie1','animation','Idle2.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z1IdleL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie1','animation','Idle3.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z1IdleL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie1','animation','Idle4.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z1IdleL.append(img)

    loadScreen.text = 'z1JumpL'
    loadScreen.update(win)
    global z1JumpL
    z1JumpL = []
    img = pygame.image.load(PATH+os.path.join('data', 'zombie1','animation','Jump1.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z1JumpL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie1','animation','Jump2.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z1JumpL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie1','animation','Jump3.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z1JumpL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie1','animation','Jump4.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z1JumpL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie1','animation','Jump5.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z1JumpL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie1','animation','Jump6.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z1JumpL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie1','animation','Jump7.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z1JumpL.append(img)

    loadScreen.text = 'z1RunL'
    loadScreen.update(win)
    global z1RunL
    z1RunL = []
    img = pygame.image.load(PATH+os.path.join('data', 'zombie1','animation','Run1.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z1RunL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie1','animation','Run2.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z1RunL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie1','animation','Run3.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z1RunL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie1','animation','Run4.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z1RunL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie1','animation','Run5.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z1RunL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie1','animation','Run6.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z1RunL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie1','animation','Run7.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z1RunL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie1','animation','Run8.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z1RunL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie1','animation','Run9.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z1RunL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie1','animation','Run10.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z1RunL.append(img)

    loadScreen.text = 'z1WalkL'
    loadScreen.update(win)
    global z1WalkL
    z1WalkL = []
    img = pygame.image.load(PATH+os.path.join('data', 'zombie1','animation','Walk1.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z1WalkL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie1','animation','Walk2.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z1WalkL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie1','animation','Walk3.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z1WalkL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie1','animation','Walk4.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z1WalkL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie1','animation','Walk5.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z1WalkL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie1','animation','Walk6.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z1WalkL.append(img)

    loadScreen.text = 'z2AttackL'
    loadScreen.update(win)
    global z2AttackL
    z2AttackL = []
    img = pygame.image.load(PATH+os.path.join('data', 'zombie2','animation','Attack1.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z2AttackL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie2','animation','Attack2.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z2AttackL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie2','animation','Attack3.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z2AttackL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie2','animation','Attack4.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z2AttackL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie2','animation','Attack5.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z2AttackL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie2','animation','Attack6.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z2AttackL.append(img)

    loadScreen.text = 'z2DeathL'
    loadScreen.update(win)
    global z2DeathL
    z2DeathL = []
    img = pygame.image.load(PATH+os.path.join('data', 'zombie2','animation','Dead1.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z2DeathL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie2','animation','Dead2.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z2DeathL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie2','animation','Dead3.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z2DeathL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie2','animation','Dead4.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z2DeathL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie2','animation','Dead5.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z2DeathL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie2','animation','Dead6.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z2DeathL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie2','animation','Dead7.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z2DeathL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie2','animation','Dead8.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z2DeathL.append(img)

    loadScreen.text = 'z2HurtL'
    loadScreen.update(win)
    global z2HurtL
    z2HurtL = []
    img = pygame.image.load(PATH+os.path.join('data', 'zombie2','animation','Hurt1.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z2HurtL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie2','animation','Hurt2.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z2HurtL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie2','animation','Hurt3.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z2HurtL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie2','animation','Hurt4.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z2HurtL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie2','animation','Hurt5.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z2HurtL.append(img)

    loadScreen.text = 'z2IdleL'
    loadScreen.update(win)
    global z2IdleL
    z2IdleL = []
    img = pygame.image.load(PATH+os.path.join('data', 'zombie2','animation','Idle1.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z2IdleL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie2','animation','Idle2.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z2IdleL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie2','animation','Idle3.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z2IdleL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie2','animation','Idle4.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z2IdleL.append(img)

    loadScreen.text = 'z2JumpL'
    loadScreen.update(win)
    global z2JumpL
    z2JumpL = []
    img = pygame.image.load(PATH+os.path.join('data', 'zombie2','animation','Jump1.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z2JumpL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie2','animation','Jump2.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z2JumpL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie2','animation','Jump3.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z2JumpL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie2','animation','Jump4.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z2JumpL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie2','animation','Jump5.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z2JumpL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie2','animation','Jump6.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z2JumpL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie2','animation','Jump7.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z2JumpL.append(img)

    loadScreen.text = 'z2RunL'
    loadScreen.update(win)
    global z2RunL
    z2RunL = []
    img = pygame.image.load(PATH+os.path.join('data', 'zombie2','animation','Run1.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z2RunL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie2','animation','Run2.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z2RunL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie2','animation','Run3.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z2RunL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie2','animation','Run4.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z2RunL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie2','animation','Run5.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z2RunL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie2','animation','Run6.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z2RunL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie2','animation','Run7.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z2RunL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie2','animation','Run8.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z2RunL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie2','animation','Run9.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z2RunL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie2','animation','Run10.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z2RunL.append(img)

    loadScreen.text = 'z2WalkL'
    loadScreen.update(win)
    global z2WalkL
    z2WalkL = []
    img = pygame.image.load(PATH+os.path.join('data', 'zombie2','animation','Walk1.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z2WalkL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie2','animation','Walk2.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z2WalkL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie2','animation','Walk3.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z2WalkL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie2','animation','Walk4.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z2WalkL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie2','animation','Walk5.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z2WalkL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie2','animation','Walk6.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z2WalkL.append(img)

    loadScreen.text = 'z3AttackL'
    loadScreen.update(win)
    global z3AttackL
    z3AttackL = []
    img = pygame.image.load(PATH+os.path.join('data', 'zombie3','animation','Attack1.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z3AttackL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie3','animation','Attack2.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z3AttackL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie3','animation','Attack3.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z3AttackL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie3','animation','Attack4.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z3AttackL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie3','animation','Attack5.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z3AttackL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie3','animation','Attack6.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z3AttackL.append(img)

    loadScreen.text = 'z3DeathL'
    loadScreen.update(win)
    global z3DeathL
    z3DeathL = []
    img = pygame.image.load(PATH+os.path.join('data', 'zombie3','animation','Dead1.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z3DeathL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie3','animation','Dead2.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z3DeathL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie3','animation','Dead3.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z3DeathL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie3','animation','Dead4.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z3DeathL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie3','animation','Dead5.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z3DeathL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie3','animation','Dead6.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z3DeathL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie3','animation','Dead7.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z3DeathL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie3','animation','Dead8.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z3DeathL.append(img)

    loadScreen.text = 'z3HurtL'
    loadScreen.update(win)
    global z3HurtL
    z3HurtL = []
    img = pygame.image.load(PATH+os.path.join('data', 'zombie3','animation','Hurt1.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z3HurtL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie3','animation','Hurt2.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z3HurtL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie3','animation','Hurt3.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z3HurtL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie3','animation','Hurt4.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z3HurtL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie3','animation','Hurt5.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z3HurtL.append(img)

    loadScreen.text = 'z3IdleL'
    loadScreen.update(win)
    global z3IdleL
    z3IdleL = []
    img = pygame.image.load(PATH+os.path.join('data', 'zombie3','animation','Idle1.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z3IdleL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie3','animation','Idle2.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z3IdleL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie3','animation','Idle3.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z3IdleL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie3','animation','Idle4.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z3IdleL.append(img)

    loadScreen.text = 'z3JumpL'
    loadScreen.update(win)
    global z3JumpL
    z3JumpL = []
    img = pygame.image.load(PATH+os.path.join('data', 'zombie3','animation','Jump1.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z3JumpL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie3','animation','Jump2.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z3JumpL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie3','animation','Jump3.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z3JumpL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie3','animation','Jump4.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z3JumpL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie3','animation','Jump5.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z3JumpL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie3','animation','Jump6.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z3JumpL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie3','animation','Jump7.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z3JumpL.append(img)

    loadScreen.text = 'z3RunL'
    loadScreen.update(win)
    global z3RunL
    z3RunL = []
    img = pygame.image.load(PATH+os.path.join('data', 'zombie3','animation','Run1.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z3RunL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie3','animation','Run2.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z3RunL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie3','animation','Run3.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z3RunL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie3','animation','Run4.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z3RunL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie3','animation','Run5.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z3RunL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie3','animation','Run6.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z3RunL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie3','animation','Run7.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z3RunL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie3','animation','Run8.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z3RunL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie3','animation','Run9.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z3RunL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie3','animation','Run10.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z3RunL.append(img)

    loadScreen.text = 'z3WalkL'
    loadScreen.update(win)
    global z3WalkL
    z3WalkL = []
    img = pygame.image.load(PATH+os.path.join('data', 'zombie3','animation','Walk1.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z3WalkL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie3','animation','Walk2.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z3WalkL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie3','animation','Walk3.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z3WalkL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie3','animation','Walk4.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z3WalkL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie3','animation','Walk5.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z3WalkL.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie3','animation','Walk6.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    img = pygame.transform.flip(img, True, False)
    z3WalkL.append(img)

    loadScreen.text = 'z1AttackR'
    loadScreen.update(win)
    global z1AttackR
    z1AttackR = []
    img = pygame.image.load(PATH+os.path.join('data', 'zombie1','animation','Attack1.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z1AttackR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie1','animation','Attack2.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z1AttackR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie1','animation','Attack3.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z1AttackR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie1','animation','Attack4.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z1AttackR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie1','animation','Attack5.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z1AttackR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie1','animation','Attack6.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z1AttackR.append(img)

    loadScreen.text = 'z1DeathR'
    loadScreen.update(win)
    global z1DeathR
    z1DeathR = []
    img = pygame.image.load(PATH+os.path.join('data', 'zombie1','animation','Dead1.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z1DeathR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie1','animation','Dead2.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z1DeathR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie1','animation','Dead3.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z1DeathR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie1','animation','Dead4.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z1DeathR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie1','animation','Dead5.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z1DeathR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie1','animation','Dead6.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z1DeathR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie1','animation','Dead7.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z1DeathR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie1','animation','Dead8.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z1DeathR.append(img)

    loadScreen.text = 'z1HurtR'
    loadScreen.update(win)
    global z1HurtR
    z1HurtR = []
    img = pygame.image.load(PATH+os.path.join('data', 'zombie1','animation','Hurt1.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z1HurtR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie1','animation','Hurt2.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z1HurtR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie1','animation','Hurt3.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z1HurtR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie1','animation','Hurt4.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z1HurtR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie1','animation','Hurt5.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z1HurtR.append(img)

    loadScreen.text = 'z1IdleR'
    loadScreen.update(win)
    global z1IdleR
    z1IdleR = []
    img = pygame.image.load(PATH+os.path.join('data', 'zombie1','animation','Idle1.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z1IdleR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie1','animation','Idle2.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z1IdleR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie1','animation','Idle3.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z1IdleR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie1','animation','Idle4.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z1IdleR.append(img)

    loadScreen.text = 'z1JumpR'
    loadScreen.update(win)
    global z1JumpR
    z1JumpR = []
    img = pygame.image.load(PATH+os.path.join('data', 'zombie1','animation','Jump1.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z1JumpR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie1','animation','Jump2.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z1JumpR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie1','animation','Jump3.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z1JumpR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie1','animation','Jump4.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z1JumpR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie1','animation','Jump5.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z1JumpR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie1','animation','Jump6.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z1JumpR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie1','animation','Jump7.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z1JumpR.append(img)

    loadScreen.text = 'z1RunR'
    loadScreen.update(win)
    global z1RunR
    z1RunR = []
    img = pygame.image.load(PATH+os.path.join('data', 'zombie1','animation','Run1.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z1RunR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie1','animation','Run2.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z1RunR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie1','animation','Run3.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z1RunR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie1','animation','Run4.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z1RunR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie1','animation','Run5.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z1RunR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie1','animation','Run6.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z1RunR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie1','animation','Run7.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z1RunR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie1','animation','Run8.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z1RunR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie1','animation','Run9.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z1RunR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie1','animation','Run10.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z1RunR.append(img)

    loadScreen.text = 'z1WalkR'
    loadScreen.update(win)
    global z1WalkR
    z1WalkR = []
    img = pygame.image.load(PATH+os.path.join('data', 'zombie1','animation','Walk1.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z1WalkR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie1','animation','Walk2.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z1WalkR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie1','animation','Walk3.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z1WalkR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie1','animation','Walk4.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z1WalkR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie1','animation','Walk5.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z1WalkR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie1','animation','Walk6.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z1WalkR.append(img)

    loadScreen.text = 'z2AttackR'
    loadScreen.update(win)
    global z2AttackR
    z2AttackR = []
    img = pygame.image.load(PATH+os.path.join('data', 'zombie2','animation','Attack1.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z2AttackR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie2','animation','Attack2.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z2AttackR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie2','animation','Attack3.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z2AttackR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie2','animation','Attack4.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z2AttackR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie2','animation','Attack5.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z2AttackR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie2','animation','Attack6.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z2AttackR.append(img)

    loadScreen.text = 'z2DeathR'
    loadScreen.update(win)
    global z2DeathR
    z2DeathR = []
    img = pygame.image.load(PATH+os.path.join('data', 'zombie2','animation','Dead1.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z2DeathR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie2','animation','Dead2.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z2DeathR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie2','animation','Dead3.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z2DeathR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie2','animation','Dead4.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z2DeathR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie2','animation','Dead5.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z2DeathR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie2','animation','Dead6.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z2DeathR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie2','animation','Dead7.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z2DeathR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie2','animation','Dead8.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z2DeathR.append(img)

    loadScreen.text = 'z2HurtR'
    loadScreen.update(win)
    global z2HurtR
    z2HurtR = []
    img = pygame.image.load(PATH+os.path.join('data', 'zombie2','animation','Hurt1.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z2HurtR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie2','animation','Hurt2.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z2HurtR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie2','animation','Hurt3.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z2HurtR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie2','animation','Hurt4.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z2HurtR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie2','animation','Hurt5.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z2HurtR.append(img)

    loadScreen.text = 'z2IdleR'
    loadScreen.update(win)
    global z2IdleR
    z2IdleR = []
    img = pygame.image.load(PATH+os.path.join('data', 'zombie2','animation','Idle1.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z2IdleR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie2','animation','Idle2.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z2IdleR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie2','animation','Idle3.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z2IdleR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie2','animation','Idle4.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z2IdleR.append(img)

    loadScreen.text = 'z2JumpR'
    loadScreen.update(win)
    global z2JumpR
    z2JumpR = []
    img = pygame.image.load(PATH+os.path.join('data', 'zombie2','animation','Jump1.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z2JumpR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie2','animation','Jump2.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z2JumpR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie2','animation','Jump3.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z2JumpR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie2','animation','Jump4.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z2JumpR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie2','animation','Jump5.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z2JumpR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie2','animation','Jump6.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z2JumpR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie2','animation','Jump7.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z2JumpR.append(img)

    loadScreen.text = 'z2RunR'
    loadScreen.update(win)
    global z2RunR
    z2RunR = []
    img = pygame.image.load(PATH+os.path.join('data', 'zombie2','animation','Run1.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z2RunR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie2','animation','Run2.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z2RunR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie2','animation','Run3.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z2RunR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie2','animation','Run4.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z2RunR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie2','animation','Run5.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z2RunR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie2','animation','Run6.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z2RunR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie2','animation','Run7.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z2RunR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie2','animation','Run8.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z2RunR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie2','animation','Run9.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z2RunR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie2','animation','Run10.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z2RunR.append(img)

    loadScreen.text = 'z2WalkR'
    loadScreen.update(win)
    global z2WalkR
    z2WalkR = []
    img = pygame.image.load(PATH+os.path.join('data', 'zombie2','animation','Walk1.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z2WalkR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie2','animation','Walk2.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z2WalkR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie2','animation','Walk3.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z2WalkR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie2','animation','Walk4.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z2WalkR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie2','animation','Walk5.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z2WalkR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie2','animation','Walk6.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z2WalkR.append(img)

    loadScreen.text = 'z3AttackR'
    loadScreen.update(win)
    global z3AttackR
    z3AttackR = []
    img = pygame.image.load(PATH+os.path.join('data', 'zombie3','animation','Attack1.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z3AttackR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie3','animation','Attack2.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z3AttackR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie3','animation','Attack3.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z3AttackR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie3','animation','Attack4.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z3AttackR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie3','animation','Attack5.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z3AttackR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie3','animation','Attack6.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z3AttackR.append(img)

    loadScreen.text = 'z3DeathR'
    loadScreen.update(win)
    global z3DeathR
    z3DeathR = []
    img = pygame.image.load(PATH+os.path.join('data', 'zombie3','animation','Dead1.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z3DeathR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie3','animation','Dead2.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z3DeathR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie3','animation','Dead3.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z3DeathR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie3','animation','Dead4.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z3DeathR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie3','animation','Dead5.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z3DeathR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie3','animation','Dead6.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z3DeathR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie3','animation','Dead7.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z3DeathR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie3','animation','Dead8.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z3DeathR.append(img)

    loadScreen.text = 'z3HurtR'
    loadScreen.update(win)
    global z3HurtR
    z3HurtR = []
    img = pygame.image.load(PATH+os.path.join('data', 'zombie3','animation','Hurt1.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z3HurtR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie3','animation','Hurt2.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z3HurtR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie3','animation','Hurt3.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z3HurtR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie3','animation','Hurt4.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z3HurtR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie3','animation','Hurt5.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z3HurtR.append(img)

    loadScreen.text = 'z3IdleR'
    loadScreen.update(win)
    global z3IdleR
    z3IdleR = []
    img = pygame.image.load(PATH+os.path.join('data', 'zombie3','animation','Idle1.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z3IdleR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie3','animation','Idle2.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z3IdleR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie3','animation','Idle3.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z3IdleR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie3','animation','Idle4.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z3IdleR.append(img)

    loadScreen.text = 'z3JumpR'
    loadScreen.update(win)
    global z3JumpR
    z3JumpR = []
    img = pygame.image.load(PATH+os.path.join('data', 'zombie3','animation','Jump1.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z3JumpR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie3','animation','Jump2.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z3JumpR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie3','animation','Jump3.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z3JumpR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie3','animation','Jump4.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z3JumpR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie3','animation','Jump5.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z3JumpR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie3','animation','Jump6.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z3JumpR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie3','animation','Jump7.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z3JumpR.append(img)

    loadScreen.text = 'z3RunR'
    loadScreen.update(win)
    global z3RunR
    z3RunR = []
    img = pygame.image.load(PATH+os.path.join('data', 'zombie3','animation','Run1.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z3RunR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie3','animation','Run2.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z3RunR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie3','animation','Run3.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z3RunR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie3','animation','Run4.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z3RunR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie3','animation','Run5.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z3RunR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie3','animation','Run6.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z3RunR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie3','animation','Run7.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z3RunR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie3','animation','Run8.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z3RunR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie3','animation','Run9.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z3RunR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie3','animation','Run10.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z3RunR.append(img)

    loadScreen.text = 'z3WalkR'
    loadScreen.update(win)
    global z3WalkR
    z3WalkR = []
    img = pygame.image.load(PATH+os.path.join('data', 'zombie3','animation','Walk1.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z3WalkR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie3','animation','Walk2.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z3WalkR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie3','animation','Walk3.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z3WalkR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie3','animation','Walk4.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z3WalkR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie3','animation','Walk5.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
    z3WalkR.append(img)
    img = pygame.image.load(PATH+os.path.join('data', 'zombie3','animation','Walk6.png'))
    imgW, imgH = img.get_rect().size
    img = pygame.transform.scale(img, (int(scaler*imgW), int(scaler*imgH)))
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
loadStuff()
loadScreen.text = 'Whole lot of Zombies'
loadScreen.update(win)
loadZombies()
loadScreen.text = 'Leaderboard'
loadScreen.update(win)
try:
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name(PATH+os.path.join('data','credentials.json'), scope)
    gc = gspread.authorize(credentials)
    wks = gc.open('ZSurvival Scoreboard').sheet1

    global scoreboard
    scoreboard = wks.get_all_records()
except:
    print("no scoreboard rip")

print('Loading Time:', time.time()-timeStart, 'seconds')
loading = False

def drawTop(man, win, score, money):
    global grenadeImg, gametimerStart
    scoreText = myFont.render('Score '+str(score), True, (255,255,255))
    win.blit(scoreText, (10, 10))
    if man.health > 0:
        pygame.draw.rect(win, (0,255,0), pygame.Rect(100, 10, man.health*2,20))
    if man.health< 200:
        pygame.draw.rect(win, (255,0,0), pygame.Rect(100+man.health*2,10, 400-man.health*2, 20))
    xgrenade = 510
    for i in range(man.grenades):
        win.blit(grenadeImg, (xgrenade, 10))
        xgrenade += 30
    moneyText = myFont.render('Money '+str(money), True, (0,255,0))
    w, ignore = moneyText.get_rect().size
    win.blit(moneyText, (SCREEN_WIDTH-10-w, 10))

def drawPlayStuff():
    global gameScreen, homeButtons, playing, end, wave, waveTimer, waveText, grenades, gameTimerStart
    if playing:
        win.blit(background, (0, 0))
        if waveTimer > 0:
            waveText[wave-1].set_alpha(waveTimer)
            win.blit(waveText[wave-1], (100,100))
            waveTimer -= 1
        for i in bullets:
            if i.draw(win):
                bullets.remove(i)
        for i in grenades:
            if i.update(win, sounds['grenade']):
                grenades.remove(i)
        man.draw(win)
        for zombie in zombies:
            if zombie.draw(win):
                zombies.remove(zombie)
        drawTop(man, win, score, money)
        timeText = myFont.render('Time '+ str(60-int(gameTimer/60)), True, (255,255,255))
        w, h = timeText.get_rect().size
        win.blit(timeText, (SCREEN_WIDTH-10-w,SCREEN_HEIGHT-10-h))
    else:
        gameOver = font.render('Game Over', False, (255,0,0))
        win.blit(gameOver, (50,50))

def drawHomeStuff(homeButtons):
    global playing, end, gameScreen, gameTimerStart
    win.blit(background, (0,0))
    text = titleFont.render('Zombie Survival', True, (255,50,50))
    w, h = text.get_rect().size
    win.blit(text, ((SCREEN_WIDTH-w)/2, 50))
    for button in homeButtons:
        button.update(win)
    if homeButtons[0].clicked():
        gameScreen = 'play'
        gameTimerStart = time.time()
    if homeButtons[1].clicked():
        gameScreen = 'play'
        playing = False

shopDispCounter = 255
notEnoughMoney = False
maxThing = False

def drawShopStuff():
    global gameScreen, shopButtons, money, shopDispCounter, notEnoughMoney, maxThing
    win.blit(background, (0,0))
    drawTop(man, win, score, money)
    backBtn.update(win)
    if maxThing:
        shopDispCounter -= 2
        text = font.render('Already Max', True, (255,255,255))
        surface = pygame.Surface(text.get_rect().size)
        surface.fill((0,0,0))
        surface.blit(text, (0,0))
        surface.set_alpha(shopDispCounter)
        win.blit(surface, (110, SCREEN_HEIGHT-50))
    elif notEnoughMoney:
        shopDispCounter -= 2
        text = font.render('Not Enough Money', True, (255,0,0))
        surface = pygame.Surface(text.get_rect().size)
        surface.fill((0,0,0))
        surface.blit(text, (0,0))
        surface.set_alpha(shopDispCounter)
        win.blit(surface, (110, SCREEN_HEIGHT-50))
    if shopDispCounter <= 1:
        shopDispCounter = 255
        maxThing = False
        notEnoughMoney = False

    for button in shopButtons:
        button.update(win)
    if shopButtons[0].clicked(): #Health
        if man.health < 200:
            if money >= 20:
                if man.health < 190:
                    man.health += 10
                else:
                    man.health = 200
                money -= 20
            else:
                notEnoughMoney = True
                shopDispCounter = 255
        else:
            maxThing = True
            shopDispCounter = 255
        time.sleep(.2) #So that it doesn't register multiple clicks
    if shopButtons[1].clicked(): #Grenade
        if man.grenades < 6:
            if money >= 75:
                money -= 75
                man.grenades += 1
            else:
                notEnoughMoney = True
                shopDispCounter = 255
        else:
            maxThing = True
            shopDispCounter = 255
        time.sleep(.2)
    if shopButtons[2].clicked(): #Weapons
        gameScreen = 'weaponShop'
        selection = man.weapon
        time.sleep(.2)
    if backBtn.clicked():
        gameScreen = 'betweenWave'

def drawBetweenThings():
    global betweenBtns, man, score, gameScreen, playing, end, gameTimer
    win.blit(background, (0,0))
    text = titleFont.render('Wave Complete', True, (255,0,0))
    w, h = text.get_rect().size
    win.blit(text, ((SCREEN_WIDTH-w)/2, 50))
    for button in betweenBtns:
        button.update(win)
    if betweenBtns[0].clicked():
        gameScreen = 'play'
        gameTimer = 0
    if betweenBtns[1].clicked():
        gameScreen = 'shop'
    if betweenBtns[2].clicked():
        gameScreen = 'play'
        playing = False
    drawTop(man, win, score, money)

def drawGameOver():
    global gameOverBtns, gameScreen, playing, man, score, money, scoreboard
    win.blit(background, (0,0))
    text = titleFont.render('Game Over', True, (255,0,0))
    w, h = text.get_rect().size
    win.blit(text, ((SCREEN_WIDTH-w)/2, 50))
    text = scoreboardFontBig.render('SCOREBOARD', True, (255,255,0))
    w, h = text.get_rect().size
    win.blit(text, ((SCREEN_WIDTH-w)/2, 125))
    ycounter = 175
    try:
        for i in scoreboard:
            name = scoreboardFont.render(i['Name'], True, (255,255,0))
            nameLoc = name.get_rect()
            nameLoc.right = (SCREEN_WIDTH/2)-50
            nameLoc.y = ycounter
            win.blit(name, nameLoc)
            scoreText = scoreboardFont.render(str(i['Score']), True, (255,255,0))
            loc = scoreText.get_rect()
            loc.left = (SCREEN_WIDTH/2)+50
            loc.y = ycounter
            win.blit(scoreText, loc)
            ycounter += 40
    except:
        noScoreboard = scoreboardFont.render("Error - Scoreboard cannot be reached", True, (255,0,0))
        loc = noScoreboard.get_rect()
        loc.center = (SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
        win.blit(noScoreboard, loc)
    '''
    for i in scoreboard:
        name = scoreboardFont.render(i['Name'], True, (255,255,0))
        nameLoc = name.get_rect()
        nameLoc.right = (SCREEN_WIDTH/2)-50
        nameLoc.y = ycounter
        print(i)
        print(nameLoc)
        win.blit(name, nameLoc)
        scoreText = scoreboardFont.render(str(i['Score']), True, (255,255,0))
        scoreLoc = scoreText.get_rect()
        scoreLoc.left = (SCREEN_WIDTH/2)+50
        scoreLoc.y = ycounter
        print(scoreLoc)
        win.blit(scoreText, (scoreLoc.x, scoreLoc.y))
        ycounter += 40
    '''
    for button in gameOverBtns:
        button.update(win)
    if gameOverBtns[0].clicked():
        gameScreen = 'home'
        time.sleep(.2)
        initV()
        try:
            wks = gc.open('ZSurvival Scoreboard').sheet1
            scoreboard = wks.get_all_records()
        except:
            print("no scoreboard")
    if gameOverBtns[1].clicked():
        playing = False
    drawTop(man, win, score, money)

def drawWeaponShop():
    global gameScreen, weaponBtns, man, shopDispCounter, notEnoughMoney, money
    global selection, cost
    win.blit(background, (0,0))
    drawTop(man, win, score, money)
    player = Person.walkRight[0]
    w, h = player.get_rect().size
    player = pygame.transform.scale(player, (w*2, h*2))
    win.blit(player, (SCREEN_WIDTH-300, 200))
    weapon = Person.gunsR[selection]
    w, h = weapon.get_rect().size
    weapon = pygame.transform.scale(weapon, (w*2, h*2))
    win.blit(weapon, (SCREEN_WIDTH-300, 200))
    if notEnoughMoney:
        shopDispCounter -= 2
        text = font.render('Not Enough Money', True, (255,0,0))
        surface = pygame.Surface(text.get_rect().size)
        surface.fill((0,0,0))
        surface.blit(text, (0,0))
        surface.set_alpha(shopDispCounter)
        win.blit(surface, (110, SCREEN_HEIGHT-50))
    backBtn.update(win)
    if backBtn.clicked():
        gameScreen = 'shop'
        time.sleep(.2)
    for id,value in weaponBtns.items():
        value.update(win)
    if weaponBtns['original'].clicked():
        selection = 'original'
        cost = 50
    if weaponBtns['laser'].clicked():
        selection = 'laser'
        cost = 200
    if weaponBtns['machine'].clicked():
        selection = 'machine'
        cost = 300
    if weaponBtns['plasma'].clicked():
        print('clicked')
        selection = 'plasma'
        cost = 600
    if weaponBtns['buy'].clicked(): #Buy button
        if money >= cost and selection != man.weapon:
            man.weapon = selection
            money -= cost
            time.sleep(.2)
            if selection == 'machine':
                man.shotDelay = 4
            elif selection == 'plasma':
                man.shotDelay = 15
            else:
                man.shotDelay = 10
        else:
            notEnoughMoney = True
            shopDispCounter = 255

playerName = ''
def drawNewHi():
    global playerName, man, score, money
    win.blit(background, (0,0))
    drawTop(man, win, score, money)
    text = titleFont.render('New High Score', True, (255,255,0))
    loc = text.get_rect()
    loc.center = (SCREEN_WIDTH/2,100)
    win.blit(text, loc)
    enterName = scoreboardFontBig.render('Enter your name', True, (0,255,0))
    loc = enterName.get_rect()
    loc.center = (SCREEN_WIDTH/2, 175)
    win.blit(enterName, loc)
    input = scoreboardFontBig.render(playerName, True, (0,255,0))
    loc = input.get_rect()
    loc.center = (SCREEN_WIDTH/2, 300)
    win.blit(input, loc)


def redraw():
    global gameScreen, homeButtons, playing, end, wave, waveTimer, waveText
    SCREEN_WIDTH, SCREEN_HEIGHT = pygame.display.get_surface().get_size()
    if not pygame.mixer.music.get_busy():
        pygame.mixer.music.load(songs[randint(0,len(songs)-1)])
        pygame.mixer.music.set_volume(.2)
        pygame.mixer.music.play()
    if gameScreen == 'play':
        drawPlayStuff()
    elif gameScreen == 'home':
        drawHomeStuff(homeButtons)
    elif gameScreen == 'shop':
        drawShopStuff()
    elif gameScreen == 'betweenWave':
        drawBetweenThings()
    elif gameScreen == 'gameOver':
        drawGameOver()
    elif gameScreen == 'weaponShop':
        drawWeaponShop()
    elif gameScreen == 'paused':
        resume.update(win)
        if resume.clicked():
            gameScreen = 'play'
    elif gameScreen == 'newHi':
        drawNewHi()
    pygame.display.update()

class Zombie: #Can run, walk, jump, idle, attack, be hurt, die
    global man, bullets, zombies, zombieCount, score, playing, end, zombieWidth, zombieHeight
    def __init__(self, x,y, type):
        self.x = x
        self.y = y
        self.type = type
        self.width = zombieWidth
        self.height = zombieHeight
        self.left = False
        self.right = False
        self.angry = False
        self.frameCount = 0
        self.frameCountMax = 0
        self.frameStart = 0
        self.maxHealth = 100
        self.health = 100
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
            if abs((self.x + self.width//2) - (man.x+man.width//2)) < 70:
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
            if self.frameCount//self.speed == 1 and abs((self.x + self.width//2) - (man.x+man.width//2)) < 70 and man.y > SCREEN_HEIGHT - 250:
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
        if self.health < self.maxHealth and action != 'die':
            pygame.draw.rect(win, (0,255,0), pygame.Rect(self.x, self.y-self.height-25,self.health, 10))
            pygame.draw.rect(win, (255,0,0), pygame.Rect(self.x+self.health, self.y-self.height-25,self.maxHealth-self.health,10))

def initV():
    global man, bullets, zombies, score, playing, end, wave, waveTimer, money, grenades, gameTimer
    global selection, cost
    man = Person(SCREEN_WIDTH // 2 - 48/2, SCREEN_HEIGHT - 155, 96, 112)
    bullets = []
    zombies = []
    grenades = []
    score = 0
    money = 0
    playing = True
    wave = 1
    waveTimer = 255
    gameTimer = 0
    selection = 'original' #Used in weapon shop
    cost = 0 #Used in weapon shop

def distance(p0, p1):
    return math.sqrt((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2)

def newWave(wave):
    global gameScreen, zombies, man, bullets
    zombies = []
    bullets = []
    man.x = SCREEN_WIDTH // 2 - 48
    man.y = SCREEN_HEIGHT - 155
    wave += 1
    waveTimer = 255
    gameScreen = 'betweenWave'
    return wave, waveTimer
# MAIN LOOP
def main():
    global playerName, scoreboard, man, bullets, zombies, score, playing, end, wave, waveTimer, gameScreen, money, grenades, gameTimer
    shotTimer = 0
    grenadeTimer = 0
    zombieTimer = 0
    zombieTimerEnd = 50
    zombieCount = 1
    gameTimer = 0

    while playing:
        clock.tick(56)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False

            if event.type == pygame.KEYDOWN:
                if gameScreen == 'newHi':
                    if event.key == pygame.K_RETURN:
                        gameScreen = 'gameOver'
                        pygame.draw.rect(win, (0,0,0), pygame.Rect(0,0,SCREEN_WIDTH, SCREEN_HEIGHT))
                        text = titleFont.render('Loading...', True, (255,255,255))
                        loc = text.get_rect()
                        loc.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
                        win.blit(text, loc)
                        pygame.display.update()
                        wks.delete_row(6)
                        wks.delete_row(5)
                        wks.delete_row(4)
                        wks.delete_row(3)
                        wks.delete_row(2)
                        newScoreboard = []
                        for i in scoreboard:
                            newScoreboard.append([i['Name'], i['Score']])
                        newScoreboard.pop(4)
                        newScoreboard.append([playerName, score])
                        newScoreboard = sort(newScoreboard)
                        for i in newScoreboard:
                            wks.append_row(i)
                        scoreboard = []
                        for i in newScoreboard:
                            newDict = {
                                'Name':i[0],
                                'Score': i[1]
                            }
                            scoreboard.append(newDict)
                    elif event.key == pygame.K_BACKSPACE:
                        playerName = playerName[0:-1]
                    else:
                        playerName += event.unicode

        if gameScreen == 'play':
            gameTimer += 1
            if wave == 1:
                if gameTimer < 10*60:
                    zombieCount = 1
                elif gameTimer < 30*60:
                    zombieCount = 3
                elif gameTimer < 60*60:
                    zombieCount = 5
                elif gameTimer > 60*60:
                    wave, waveTimer = newWave(wave)
            elif wave == 2:
                if gameTimer < 10*60:
                    zombieCount = 3
                elif gameTimer < 30*60:
                    zombieCount = 4
                    zombieTimerEnd = 30
                elif gameTimer < 60*60:
                    zombieTimerEnd = 30
                    zombieCount = 6
                elif gameTimer > 60*60:
                    wave, waveTimer = newWave(wave)
            elif wave == 3:
                if gameTimer < 10*60:
                    zombieCount = 5
                elif gameTimer < 30*60:
                    zombieTimerEnd = 10
                elif gameTimer < 60*60:
                    zombieCount = 8
                elif gameTimer > 60*60:
                    wave, waveTimer = newWave(wave)
            elif wave == 4:
                if gameTimer < 10*60:
                    zombieTimerEnd = 50
                    zombieCount = 10
                elif gameTimer < 30*60:
                    zombieTimerEnd = 40
                elif gameTimer < 60*60:
                    zombieTimerEnd = 20
                    zombieCount = 15
                elif gameTimer > 60*60:
                    wave, waveTimer = newWave(wave)
            elif wave == 50:
                print("you win")
            else:
                if gameTimer < 10*60:
                    zombieTimerEnd = 50*((50-wave)/50)
                    zombieCount = 10+int(.7*wave)
                elif gameTimer < 30*60:
                    zombieTimerEnd = 40*((50-wave)/50)
                elif gameTimer < 60*60:
                    zombieTimerEnd = 20*((50-wave)/50)
                    zombieCount = 15+int(.7*wave)
                elif gameTimer > 60*60:
                    wave, waveTimer = newWave(wave)
            if len(zombies) < zombieCount and zombieTimer >= zombieTimerEnd:
                x = randint(1,2)
                if x == 1:
                    zombie = Zombie(-100,SCREEN_HEIGHT-30, randint(0,2))
                    zombies.append(zombie)
                if x == 2:
                    zombie = Zombie(SCREEN_WIDTH, SCREEN_HEIGHT-30, randint(0,2))
                    zombies.append(zombie)
                zombieTimer = 0
            zombieTimer += 1
            for bullet in bullets:
                for zombie in zombies:
                    if bullet.x > zombie.x and bullet.x < zombie.x+zombie.width and bullet.y < zombie.y and bullet.y > zombie.y-zombie.height and zombie.isDead == False:
                        #hit
                        sounds['hit'].play()
                        bullets.remove(bullet)
                        if bullet.type == 'original':
                            zombie.health -= 20
                        elif bullet.type == 'laser':
                            zombie.health -= 30
                        elif bullet.type == 'machine':
                            zombie.health -= 12
                        elif bullet.type == 'plasma':
                            zombie.health -= 50
                        if randint(1,5) == 1 and not zombie.actions.bool[2]: #Makes sure not in middle of jumping
                            zombie.hurt()
                        if zombie.health <= 0 and not zombie.isDead:
                            zombie.die()
                            score += 1
                            money += 5
                        break
            for grenade in grenades:
                for zombie in zombies: #Uncomment below to show hitboxes
            #        pygame.draw.circle(win, (255,0,0), (int(grenade.x+grenade.w//2), int(grenade.y+grenade.h//2)), 90, 4)
            #        pygame.draw.circle(win, (255,255,0), (int(zombie.x+zombie.width//2), int(zombie.y-zombie.height//2)), 10)
            #        pygame.display.update()
                    if distance([grenade.x+grenade.w//2, grenade.y+grenade.h//2-10], [zombie.x+zombie.width//2, zombie.y-zombie.height//2]) < 120 and grenade.exploding and grenade.frameCounter < 26:
                        zombie.health -= 5
                    if zombie.health <= 0 and not zombie.isDead:
                        zombie.die()
                        score += 1
                        money += 5

            for zombie in zombies:
                zombie.setAction()
            if man.health <= 0:
            #    playing = False
                newScore = False
                try:
                    for i in range(0,len(scoreboard)):
                        if score > scoreboard[i]['Score']:
                            newScore = True
                    #        print("new high score")
                            break
                except:
                    print("no scoreboard")
                if newScore:
                    gameScreen = 'newHi'
                else:
                    gameScreen = 'gameOver'

            keys = pygame.key.get_pressed()

            if keys[pygame.K_SPACE]:
                if shotTimer > man.shotDelay:
                    sounds['shot'].play()
                    bullets.append(Bullet(man.x + man.width / 2, man.y + 50, man.left, man.weapon))
                    shotTimer = 0
            if keys[pygame.K_g]:
                if grenadeTimer > 20:
                    if man.grenades > 0:
                        if keys[pygame.K_LEFT] or keys[pygame.K_RIGHT] or keys[pygame.K_d] or keys[pygame.K_a]:
                            temp = Grenade(man.x+man.width//2, man.y, man.left, True)
                        else:
                            temp = Grenade(man.x+man.width//2, man.y, man.left, False)
                        grenades.append(temp)
                        grenadeTimer = 0
                        man.grenades -= 1
            shotTimer += 1
            grenadeTimer += 1
            if (keys[pygame.K_p]):
                gameScreen = 'paused'
            if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and man.x > man.vel:
                man.left = True
                man.right = False
                man.standing = False
                man.x -= man.vel
            elif (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and man.x < SCREEN_WIDTH - man.width - man.vel:
                man.right = True
                man.left = False
                man.x += man.vel
                man.standing = False
            else:
                man.standing = True
                man.walkCount = 0
            if not man.isJump:
                if keys[pygame.K_UP] or keys[pygame.K_w]:
                    man.isJump = True
            else:
                man.y -= man.jumpAcc
                if man.jumpAcc > -20:
                    man.jumpAcc -= 1
                else:
                    man.jumpAcc = 20
                    man.isJump = False
                    if man.y != SCREEN_HEIGHT-155:
                        man.y = SCREEN_HEIGHT-155
        redraw()

def sort(ls): #sorts a list of lists where the 2nd item in the 2nd list is a number etc. [['asd', 1], ['asdf', 4]]
    for i in range(0,len(ls)-1):
        if ls[i][1] >= ls[i+1][1]:
            pass
        else:
            temp = ls.pop(i+1)
            ls.insert(i, temp)
    #        print(ls)
    #        print('doing again')
            ls = sort(ls)
#    print(ls)
    return ls
initV()
main()
pygame.quit()
