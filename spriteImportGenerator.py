#image sprite importer

def makeLEFT(initName, word, num): # LEFT
    endString = 'loadScreen.text = \''+initName+'\'\n'
    endString += 'loadScreen.update(win)\n'
    endString += 'global '+initName+'\n'+initName+ ' = []\n'
    for i in range(1, num+1):
        stuff1 = 'img = pygame.image.load(\''+word+str(i)+'.png\')\n'
        stuff2 = 'imgW, imgH = img.get_rect().size\n'
        stuff3 = 'img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))\n'
        stuff4 = 'img = pygame.transform.flip(img, True, False)\n'
        stuff5 = initName+'.append(img)\n'

        endString = endString+stuff1+stuff2+stuff3+stuff4+stuff5
    print(endString)

def makeRIGHT(initName, word, num): # RIGHT
    endString = 'loadScreen.text = \''+initName+'\'\n'
    endString += 'loadScreen.update(win)\n'
    endString += 'global '+initName+'\n'+initName+ ' = []\n'
    for i in range(1, num+1):
        stuff1 = 'img = pygame.image.load(\''+word+str(i)+'.png\')\n'
        stuff2 = 'imgW, imgH = img.get_rect().size\n'
        stuff3 = 'img = pygame.transform.scale(img, (int(.4*imgW), int(.4*imgH)))\n'
       # stuff4 = 'img = pygame.transform.flip(img, True, False)\n'
        stuff5 = initName+'.append(img)\n'

        endString = endString+stuff1+stuff2+stuff3+stuff5
    print(endString)
        

def left():
    for i in range(1,4):
        makeLEFT('z'+str(i)+'AttackL', 'zombie'+str(i)+'/animation/Attack',6)
        makeLEFT('z'+str(i)+'DeathL', 'zombie'+str(i)+'/animation/Dead',8)
        makeLEFT('z'+str(i)+'HurtL', 'zombie'+str(i)+'/animation/Hurt',5)
        makeLEFT('z'+str(i)+'IdleL', 'zombie'+str(i)+'/animation/Idle',4)
        makeLEFT('z'+str(i)+'JumpL', 'zombie'+str(i)+'/animation/Jump',7)
        makeLEFT('z'+str(i)+'RunL', 'zombie'+str(i)+'/animation/Run',10)
        makeLEFT('z'+str(i)+'WalkL', 'zombie'+str(i)+'/animation/Walk',6)

def right():
    for i in range(1,4):
        makeRIGHT('z'+str(i)+'AttackR', 'zombie'+str(i)+'/animation/Attack',6)
        makeRIGHT('z'+str(i)+'DeathR', 'zombie'+str(i)+'/animation/Dead',8)
        makeRIGHT('z'+str(i)+'HurtR', 'zombie'+str(i)+'/animation/Hurt',5)
        makeRIGHT('z'+str(i)+'IdleR', 'zombie'+str(i)+'/animation/Idle',4)
        makeRIGHT('z'+str(i)+'JumpR', 'zombie'+str(i)+'/animation/Jump',7)
        makeRIGHT('z'+str(i)+'RunR', 'zombie'+str(i)+'/animation/Run',10)
        makeRIGHT('z'+str(i)+'WalkR', 'zombie'+str(i)+'/animation/Walk',6)

left()
right()
