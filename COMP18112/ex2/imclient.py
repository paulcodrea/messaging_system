import im
import time
server = im.IMServerProxy('http://webdev.cs.manchester.ac.uk/~j47510pc/IMServer.php')

def recursive(boool):
    if boool:
        print "User2: " + server['newKey']
    myMessage = raw_input('Type your message: ')
    server['newKey'] = myMessage
    boool = True
    print "User1: " + server['newKey']
    time.sleep(10)
    recursive(boool)


server.clear()
recursive(False)
