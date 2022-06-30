# For refrence https://python.plainenglish.io/13-advanced-python-scripts-for-everyday-programming-1a52acb84101
# https://python.plainenglish.io/13-advanced-python-scripts-for-everyday-programming-1a52acb84101

# pip install selenium

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

bot = webdriver.Chrome("chromedriver.exe")
bot.get('http://www.google.com')

search = bot.find_element_by_name('q')
search.send_keys("@codedev101")
search.send_keys(Keys.RETURN)
time.sleep(5)
bot.quit()
