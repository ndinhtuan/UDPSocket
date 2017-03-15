from socket import *
import threading

def sending(clientSocket, addressDstHost):
    while 1:
        message = raw_input("\033[1;32;40m")
        clientSocket.sendto(message, addressDstHost)

def receiving(clientSocket, portReceiving):
    clientSocket.bind(('', portReceiving))
    while 1:
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
        print "\033[1;35;40m{}\033[1;32;40m".format(modifiedMessage)

try:
    serverName = '127.0.0.1'
    serverPortSending = 5000
    serverPortReceiving = 6000
    clientSocketSending = socket(AF_INET, SOCK_DGRAM)
    clientSocketReceiving = socket(AF_INET, SOCK_DGRAM)

    t1 = threading.Thread(target=sending, args=(clientSocketSending, (serverName, serverPortSending)) )
    t1.daemon = True
    t2 = threading.Thread(target=receiving, args=(clientSocketReceiving, serverPortReceiving) )
    t2.daemon = True
    t1.start()
    t2.start()
except Exception, e:
    print str(e)
    print "Error multi-threading"

while(1):
    pass
#clientSocketReceiving.close()
#clientSocketSending.close()
