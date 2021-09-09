# For refrence https://documentation.red-gate.com/sdg3/using-generators/example-python-scripts

# Combinatoric generator
# The Python iteration and combinatorics library
import itertools
lowercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".lower()
def main(config):
 return list(combinations())
def combinations():
	#Iterate over all pairs of letters in `lowercase`
	for pair in itertools.combinations(lowercase, 2):
	# and yield them as a string
	yield "".join(pair)
	