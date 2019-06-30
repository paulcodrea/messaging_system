import sys
from ex3utils import Server
from random import *
import time
import datetime


def randomColor(no):
	if no == 1:
		#RED
		return '\033[31m'
	elif no == 2:
		#GREEN
		return '\033[32m'
	elif no == 3:
		#BLUE
		return '\033[34m'
	elif no == 4:
		#ORANGE
		return '\033[33m'
	elif no == 5:
		#purple
		return '\033[35m'
	elif no == 6:
		#cyan
		return '\033[36m'
	elif no == 7:
		#yellow
		return '\033[93m'
	elif no == 8:
		#pink
		return '\033[95m'
	elif no == 9:
		#lightblue
		return '\033[94m'
	elif no == 10:
		#lightgreen
		return '\033[92m'

# Create an echo server class
class myEchoServer(Server):

	# use the onStart method for initialising server-wide variables
	def onStart(self):
		print "Echo server has started"
		print " "
		print "Need some help? Press HELP"
		self.count = 0
		self.clients = {}
		self.colors = {}

	def onStop(self):
		print "Echo server has stopped"

	def onConnect(self, socket):
		socket.screenName = None

		self.count += 1
		if self.count == 1:
			print "There is " + str(self.count) + " client connected"
		else:
			print "There are " + str(self.count) + " clients connected"

	def onMessage(self, socket, message):
		socket.connectionTime = time.time()
		(commands, sep, parameter) = message.strip().partition(' ')
		command = commands.upper()
		if command == 'REGISTER':
			# all names with upper letters
			name = parameter.upper()
			socket.screenName = name
			self.clients[socket.screenName] = socket
			# the dictionary gets a list of nummbers for each user in the chat
			#the numbers are random from 1 - 10 , there are 10 colors available
			self.colors[socket.screenName] = int(random()*10)
			self.colors[socket.screenName] = randomColor(self.colors[socket.screenName])
			#print self.colors[socket.screenName]
			print "New username ", socket.screenName, " connected at", datetime.datetime.now().time()
		elif command == 'MESSAGE':
			if socket.screenName:
				someName = socket.screenName
				colorUser = self.colors[socket.screenName]
				for client, socket in self.clients.iteritems():
					socket.send(colorUser+ "User " + someName + " said: " + parameter + '\033[97m')
			else :
				print "REGISTER your name first"
				socket.send("REGISTER your name first")
		elif command == 'PRIVATE':
			(receivers, sep, message) = parameter.strip().partition(' ')
			receiver = receivers.upper()
			colorUser = self.colors[socket.screenName]
			if receiver in self.clients:
				self.clients[receiver].send(colorUser + "Private message from " + socket.screenName +": " + message + "\033[97m"
				)
			else :
				socket.send("There is no " + receiver + " user in this chat")
		elif command == "HELP":
			socket.send(" ")
			socket.send("REGISTER name - Register as new user")
			socket.send("MESSAGE text - Send a new message to all users")
			socket.send("PRIVATE name text - Send a private message to a specific user")


		# Signify all is well
		return True

	def onDisconnect(self, socket):
		self.count -= 1
		if self.count == 1:
			print "There is " + str(self.count) + " client connected"
		else:
			print "There are " + str(self.count) + " clients connected"


# Parse the IP address and port you wish to listen on.
ip = sys.argv[1]
port = int(sys.argv[2])

# Create an echo server.
server = myEchoServer()
# Start server
server.start(ip, port)
