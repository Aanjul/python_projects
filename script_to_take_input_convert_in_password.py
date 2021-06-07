# For Refrence https://www.fosslinux.com/46256/python-script-examples.htm

#get_pass.py


import getpass

# request  user to input a password
passwd = getpass.getpass('Password:')

#validate the password entered by the user against the given password

if passwd == "password":
    print("authentication successfull")
else:
 print("authentication failed")


        #to run this script in terminal python3 get_pass.py