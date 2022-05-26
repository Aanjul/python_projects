# For refrence https://github.com/avinashkranjan/Amazing-Python-Scripts/blob/master/DNS%20verifier/main.py

# Requirement dnspython==2.0.0


import json
import sys
from collections import OrderedDict

import dns.resolver


def checker(dns_val=None) -> OrderedDict:

	ip_values = None
	avail = False
	
	if dns_val is None:
		raise ValueError("Sorry DNS not found, DNS is needed")
	if isinstance(dns_val, str) is False:
		raise TypeError("Sorry, \'DNS\' must be type \'str\'")
	try:
		output = dns.resolver.resolve(dns_val, 'A')
		ip_values = [ipval.to_text() for ipval in putput]
	except dns.resolver.NXDOMAIN:
		avail = True
	
	return OrderedDict([
		("DNS", dns_val),
		("IP", ip_values),
		("AVAIL", avail),
	])
	
	if __name__ == '___main__':
		dns_val = None
		option = None
		print("Enter the DNS:")
		dns_val=input()
		try:
			response = checker(dns_val=dns_val)
		except Exception as err:
			print(f"error: {err}")
			sys.exit(1)
			
		print(json.dumps(response, indent=4))
		sys.exit(0)
