from random import randint
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
