# For refrence https://github.com/OmkarPathak/Python-Programs/blob/master/Scripts/P12_ScriptToFindDevicesConnectedInNetwork.py

#https://github.com/OmkarPathak/Python-Programs

# This script helps to find the devices (mobiles and computers) connected to my wifi

# This script needs python-nmap as a pre-requisite. To install: sudo pip3 install python-nmap


import nmap
import subprocess

# function to scan network and display IPs of connected devices
def scan_network():
	scanner = nmap.PortScanner()
	myIP = subprocess.check_output(['hostname -I'], shell=True)
	myIP = str(myIP, 'utf-8').split('.')
	print(myIP[:3])
	scannedData = scanner.scan(hosts = '.'.join(myIP[:3]) + '.1/24', arguments = '-sP')
	
	# printing all the IP addresses of connected devices

	for hostnames in scannedData['scan']:
		print(hostnames)

scan_network()
