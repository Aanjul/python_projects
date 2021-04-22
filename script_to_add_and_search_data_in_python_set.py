#For refernce https://linuxhint.com/python_scripts_beginners_guide/#post-67157-20


#Define the number set
numbers = {23, 90 , 56 , 78, 12, 34, 67}

#Add a new data
numbers.add(50)
# Print the set values
print(numbers)

message = "Number is not found"

#Take a number value for search
search_number = int(input("Enter a number:"))

#Search the number in the set

for val in numbers:
    if val == search_number:
        message = "Number is found"
        break

    print(message)

    