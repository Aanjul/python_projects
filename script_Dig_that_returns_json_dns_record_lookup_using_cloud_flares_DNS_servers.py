#For refrence https://github.com/hastagAB/Awesome-Python-Scripts/blob/master/DOH-Dig/doh-dig
#Requirements
#docopt
#requests

#!/usr/bin/env python3 


"""DNS OF HTTPS - DIG

Usage:
	doh-dig type <type> <record>
	doh-dig ptr <ip>
	doh-dig (-h | --help)
	doh-dig --version
	
Options:
	-h --help		Show this screen.
	--version  		Show version.

"""
from docopt import docopt
from pprint import pprint as pp
from sys import exit
import ipaddress, json

def CloudFlareLookup(type,record):
		 import requests
		 headers = {'accept': 'application/dns-json'}
		 url = "https://1.1.1.1/dns-query?name=%s&type=%s" % (record,type)
		 r = requests.get(url, headers=headers)
		 j_data = json.loads(r.text)
		 try:
				  return(j_data['Answer'])
		 except:
				  return(j_data['Question'])


valid_types = ['A','MX','PTR','SRV','TXT','NS']

if __name__ == '__main__':
	arguments = docopt(__doc__, version='doh-dig 0.1')
	if arguments['type']:
		t = arguments['<type>'].upper()
		r = arguments['<record>'].lower()
		if t not in valid_types:
			     exit('invalid type')
		x = CloudFlareLookup(t,r)
		print(json.dumps(x))
	elif arguments['ptr']:
		ip = arguments['<ip>']
		arpa = ipaddress.ip_address(ip).reverse_pointer
		x = CloudFlareLookup('PTR',arpa)
		print(json.dumps(x))
	else:
		print(arguments)
		
		 

