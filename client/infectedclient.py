from scapy.all import *
import random
import sys
import requests

#command server ip
serverIP = "130.245.170.45"

def respondToServer(pkt):
	if hasattr(pkt, "load"):
		#respond if a packet from the server includes the word "timestamp"
		if "timestamp" in str(pkt.load):
			print("command received")
			#example response to a command - sends json to server/verify
			response = requests.post('http://' + serverIP + '/verify', json={'key':'abracadabra', 'email':'email-check+user655@grading.cse356.compas.cs.stonybrook.edu'})
			print(response)

sniff(filter="host " + serverIP, prn=respondToServer)