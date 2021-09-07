# For refrence https://documentation.red-gate.com/sdg3/using-generators/example-python-scripts

#Generate VISA-style numbers with a Luhn checksum

import clr
clr.AddReference("System")
from System import Random
random = Random()
def choice(1):
	return 1[random.Next(len(1))]
def completed_number(prefix, length):
# Given a prefix and a desired length, fill in the number up
# to the desired length, using Luhn to compute the checksum

ccnumber = list(prefix)
# Generate digits

for _ in range(length - len(prefix) - 1):
	ccnumber.append(choice('0123456789'))
	# Calculate sum
	sum = pos = 0
	reversedCCnumber = list(reversed(ccumber))
	while pos < length - 1:
	odd = int(reversedCCnumber[pos]) * 2
	if odd > 9: odd -= 9
	if pos != (length - 2): sum += int(reversedCCnumber[pos+1])
	sum += odd
	pos += 2
	# Calculate check digit
	checkdigit = ((sum / 10 + 1) * 10 - sum) % 10
	ccnumber.append(str(checkdigit))
	
	return ''.join(ccnumber)
def main(config):
for _ in range(config["n_rows"]):
#VISA numbers start with a 4
yield completed_number('4', 16)


    