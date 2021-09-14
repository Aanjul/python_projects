# For reference https://documentation.red-gate.com/sdg3/using-generators/example-python-scripts

# Specify a string stem as constant and append an incrementing number to it

def main(config):
	return list(Sequence(config["n_rows"])) # The max number of rows available
def Sequence(max):
	for i in range(1, max + 1): # Modify the range start and end points in order to offset the row number
	yield "Label {0}".format(i) # Format the output string here
