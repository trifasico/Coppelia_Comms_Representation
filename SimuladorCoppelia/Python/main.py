import math
import time
import numpy as np
import sys
import time
import socket
from CoppeliaComunication import *
from represent import Draw

DRAW = 0                # 0 - NO DRAW | 1 - Draw here every loop | 2 - Draw on separate python code (Need to Uncomment main in represent.py)
Coppelia = Coppelia()
Ball = [0, 0]
Robots = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
lastTime = 0


if DRAW:
    App = Draw(3)

if DRAW == 2:
    serverAddressPort = ("localhost", 19999)
    ProcessingSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    ProcessingSocket.bind(("localhost", 20000))


while Ball != -1:
    loopTime = time.time()
    Ball, Robots, BalizaMine, BalizaOpo, BallHandler = Coppelia.getInfo()

    FrPython = [3, 0]
    if(BallHandler == "1"):
        FrPython = [6, 0]
    FrPythonString = ""
    for a in FrPython:
        FrPythonString = FrPythonString + str(a) + " "
    print(FrPythonString, end=" -- ", flush=True)

    Coppelia.sendInfo(FrPythonString)
    
    if Ball != -1:
        if time.time() - lastTime > 0.1 and DRAW == 2:
            ToDraw = {'Robots': Robots, 'Ball': Ball}
            ProcessingSocket.sendto(str.encode(str(ToDraw)),("localhost", 19999))
            lastTime = time.time()
        if DRAW:
            App.Background()
            for Robot in Robots:
                App.Robot(Robot)
            App.Ball(Ball)
            App.reDraw()
    else:
        break

    #print("B:", Ball, end=' | ')
    #print("R1:",Robots[0], end=' | ')
    #print("BH:",BallHandler, end=' | ')    
    print(int((time.time()-loopTime)*1000), "ms", flush=True)
