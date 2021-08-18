# For refrence https://github.com/hastagAB/Awesome-Python-Scripts/blob/master/Fibonacci_Sequence_Generator/Fibonacci.py

def Fibbo_Sequence_Generator():
        # Generates a fibonacci sequence with the size of ngi
		runFib = True
		while(runFib):
		    n = int(input('How many numbers do you need? '))
			if n > 0 :
				runFib = False
				series = [1]
				
				while len(series) < n:
				    if len(series) == 1:
					    series.append(1)
					else:
					    series.append(series[-1] + series[-2])
						
				for i in range(len(series)): #Convert the numbers to strings
				 series[i] = str(series[i])
				 else:
				   print('Enter a Valid Number')
				   
				   return(', '.join(series)) # Return the separated sequence by comas
print(Fibbo_Sequence_Generator())   
