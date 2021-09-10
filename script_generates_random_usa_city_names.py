#For refrence https://documentation.red-gate.com/sdg3/using-generators/example-python-scripts

#Open a file and filter the results
filename = r"cities.txt"
def main(config):
	filepath = config["config_path"] + "\\" + filename
	return list(cities(filepath))
def cities(filepath):
	with open(filepath) as cities:
	 for city in cities:
		 if city.startswith(tuple("ABCDEFG")):
			yield city.strip()