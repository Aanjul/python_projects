# For refrence https://levelup.gitconnected.com/10-interesting-python-programs-with-code-b676181a2d1a


# Requirements
#pyautogui
#pip install pyautogui

import pyautogui
num=int(input("Enter a value to divide 100"))
if num == 0:
	pyautogui.alert(" Alert!!! 100 cannot be divided by 0")
else:
	print(f'The value is {100/num}')