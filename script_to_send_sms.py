# For refrence https://github.com/realpython/python-scripts/blob/master/scripts/27_send_sms.py

#Send SMS message via TextBelt


import request


message = raw_input('Enter a Message: ')
number = raw_input('Enter the phone number: ')


payload = {'number': 'number', 'message': message}
r = requests.post("http://textbelt.com/text", data=payload)

if r.json()['success']:
     print('Success!')
else:
 	print('Error!')
