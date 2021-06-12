# For reference https://www.fosslinux.com/46256/python-script-examples.htm


#reverse_number_number.py


user_input=int(input("Enter the number to reverse: "))
_rev=0
while(user_input>0):
    dig=user_input%10
    _rev=_rev*10+dig
    user_input=user_input//10
    print("The reversed number is :",_rev)

    #Command to execute the script over terminal python3 script_to_reverse_user_input_number.py
    
