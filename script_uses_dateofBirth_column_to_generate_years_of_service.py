# For refrence https://documentation.red-gate.com/sdg3/using-generators/example-python-scripts

# This example takes a column as a date of birth
# Then work out a random number of years service
# This if this is > now the person is still working at this company

def main(config):
	dateOfBirth = InsertColumnName
	workingAge = 18
	age = (DateTime.Now - dateOfBirth).TotalDays/365
	numberofYearsWorking = age - workingAge
	#Initialize Randomness only on the first row
	if (config["row_count"] == 0):
	    # could use python random number generator
        # and store the value in the config
		session.SetupNormalGenerator(False, config["seed"], 1.0, 50, 10, 0.2)
		
		if (numberofYearsWorking > 0):
			yearsOfService = session.GetNextRandomNumber()
			if (yearsOfService > numberofYearsWorking):
			#Person still working at this company
			return numberofYearsWorking
		else:
			return yearsOfService
		return 0 #Too young

