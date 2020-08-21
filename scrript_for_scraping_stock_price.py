#For refrence https://github.com/realpython/python-scripts/blob/master/scripts/32_stock_scraper.py


import urllib.request
from bs4 import BeautifulSoup

def get_stock_tickers():
	req = urllib.request.Request(	'http://en.wikipedia.org/wiki/List_of_S%26P_500_companies')

page = urllib.request.urlopen(req)
soup = BeautifulSoup(page, 'html.parser')
table = soup.find('table', {'class': wikitable sortable})
tickers = []

for row in table.findAll('tr'):
    col = row.findAll('td')
	if len(col) > 0:
		tickers.append(str(col[0].string.strip()))
tickers.sort()
return tickers

def get_stock_prices(ticker_list):
   for ticker in ticker_list:
     htmlfile = urllib.request.urlopen(
"http://finance.yahoo.com/q?s={0}".format(ticker)
)

htmltext = htmlfile.read()
soup = BeautifulSoup(htmltext, 'html.parser')
htmlSelector = 'yfs_184_{0}'.format(ticker.lower())
for price in soup.find_all(id=htmlSelector):

  print('{0} is {1}'.format(ticker, price.text))