import socket
import time

#localIP = "192.168.44.209"
localIP = "localhost"
localPort = 20000
bufferSize = 1024
#clients = [("192.168.44.134", 20001), ("192.168.44.209", 20002), ()]
#clients = [("10.0.0.28", 20001), ("10.0.0.28", 20002), ()]
clients = [("localhost", 20001), ("localhost", 20002), ()]

msgFromServer = "Hello UDP Client"
bytesToSend = str.encode(msgFromServer)

# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to address and ip
UDPServerSocket.bind((localIP, localPort))
print("UDP server up and listening")
UDPServerSocket.sendto(str.encode("START"), clients[0])
UDPServerSocket.sendto(str.encode("START"), clients[1])

counter = 0
counterMax = 1000
a = ""
# Listen for incoming datagrams

initialTime = time.time_ns()
loopInitialTime = 0

while counter < counterMax:
    #while time.time_ns() < loopInitialTime+5000000:
    #    pass
    #loopInitialTime = time.time_ns()
    #time.sleep(1)
    # Sending a reply to client

    #a = input()
    #tt = time.time_ns()
    counter = counter+1
    a = str(counter)

    #print("1",time.time()-tt)
    #tt = time.time_ns()

    UDPServerSocket.sendto(str.encode(a), clients[0])
    UDPServerSocket.sendto(str.encode(a), clients[1])
    #print("2",time.time_ns()-tt)
    #tt = time.time_ns()
    
    #bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    #print("3",time.time_ns()-tt)
    #tt = time.time_ns()
    
    #message = bytesAddressPair[0]
    #address = bytesAddressPair[1]

    #clientMsg = "Message from Client:{}".format(message)
    #clientIP = "Client IP Address:{}".format(address)

    #print(clientMsg)
    #print(clientIP)
    
    #print(message)

UDPServerSocket.sendto(str.encode("q"), clients[0])
UDPServerSocket.sendto(str.encode("q"), clients[1])
print(counterMax, "tramas em", (time.time_ns()-initialTime)/1000000 , "ms")

    