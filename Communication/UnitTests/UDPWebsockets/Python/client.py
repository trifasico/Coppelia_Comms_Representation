
import socket

msgFromClient       = "Hello UDP Server"
bytesToSend         = str.encode(msgFromClient)
serverAddressPort   = ("localhost", 20002)
bufferSize          = 1024

# Create a UDP socket at client side
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
# Bind a specific IP and Port to make the information concistant
UDPClientSocket.bind(("localhost", 20001))

# Send to server using created UDP socket
#UDPClientSocket.sendto(bytesToSend, serverAddressPort)
clientMsgDD = str.encode("")

while clientMsgDD != "q":

    bytesAddressPair = UDPClientSocket.recvfrom(bufferSize)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]

    clientMsg = "Message from Client:{}".format(message)
    clientIP = "Client IP Address:{}".format(address)

    #print(clientMsg)
    #print(clientIP)

    clientMsgDD = message.decode('utf8', 'strict')
    print(clientMsgDD)
    
    #UDPClientSocket.sendto(message, serverAddressPort)
    #time.sleep(1)
    # Sending a reply to client
    #a = input()
    #print(a)
    #UDPServerSocket.sendto(str.encode(a), ("127.0.0.1", 20002))

#msgFromServer = UDPClientSocket.recvfrom(bufferSize)

#msg = "Message from Server {}".format(msgFromServer[0])
#print(msg)