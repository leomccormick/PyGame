from operacoes import *

class Player():
    def __init__(self, x, y):
        self.lane = x
        self.position = y
        self.point = 375
        self.mudancaPosition = False
        self.mudancaLane = False
        self.velocidade = 0
    
    def laneChange(self, x):
        if self.mudancaPosition == False:
            if x == 1:
                if self.lane < 1:
                    self.accl = 10
                    self.lane += 1
                    self.mudancaLane = True
            elif x == -1:
                if self.lane > -1:
                    self.accl = -10
                    self.lane -= 1
                    self.mudancaLane = True
    
    def positionChange(self, x):
        if self.mudancaLane == False:
            if x == 1:
                if self.position < 1:
                    self.accp = 10
                    self.position += 1
                    self.mudancaPosition = True
            elif x == -1:
                if self.lane > -1:
                    self.accp = -10
                    self.position -= 1
                    self.mudancaPosition = True
    
    def update(self, x):
        self.velocidade += self.accl + self.accp
        self.position += self.velocidade
        if (self.point-125) % 250 == 0:
            self.accp *= 0
            self.accl *= 0
            self.velocidade *= 0
        if (self.point) % 250 == 0:
            self.accp *= -1
            self.accl *= -1
        

class Train():
    def __init__(self, tipo, lane):
        self.position = tipo
        self.lane = lane
        self.y = 0
    def update(self, y):
        self.y += 1 #velocidade