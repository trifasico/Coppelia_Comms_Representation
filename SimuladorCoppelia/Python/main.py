import math
import time
import numpy as np
import sys
import time
from CoppeliaComunication import *
from represent import *
import socket

serverAddressPort   = ("localhost", 20002)

DRAW = 1
Coppelia = Coppelia()
Ball = [0, 0]
Robots = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]

def draw_Processing(Log):
    if DRAW:
        App = Draw(3)
    while 1:
        ToDraw = Log.recv()
        Robots = ToDraw['Robots']
        Ball = ToDraw['Ball']

        App.Background()
        for Robot in Robots:
            App.Robot(Robot)
        App.Ball(Ball)
        App.reDraw()

def main(Rep):
    global Coppelia, Ball, Robots
    while Ball != -1:
        tempo = time.time()
        Ball, Robots, BalizaMine, BalizaOpo, BallHandler = Coppelia.getInfo()

        FrPython = [0, 0]
        if(BallHandler == "1"):
            FrPython = [6, 0]
        FrPythonString = ""
        for a in FrPython:
            FrPythonString = FrPythonString + str(a) + " "
        print(FrPythonString, end=" -- ", flush=True)

        Coppelia.sendInfo(FrPythonString)
        
        ToDraw = {'Robots': Robots, 'Ball': Ball}

        print(int((time.time()-tempo)*1000), "ms", end=' ', flush=True)
        Rep.send(ToDraw)

        #if DRAW:
        #    App.Background()
        #    for Robot in Robots:
        #        App.Robot(Robot)
        #    App.Ball(Ball)
        #    App.reDraw()

        
        #print("B:", Ball, end=' | ')
        #print("R1:",Robots[0], end=' | ')
        #print("BH:",BallHandler, end=' | ')
        
        print(int((time.time()-tempo)*1000), "ms", flush=True)


if __name__ == '__main__':
    RepCom, LogCom = multiprocessing.Pipe(duplex=True)
    player1 = multiprocessing.Process(target=main, args=(RepCom,))
    player2 = multiprocessing.Process(target=draw_Processing, args=(LogCom,))
    player1.start()
    player2.start()
    player1.join()
    #player2.join()