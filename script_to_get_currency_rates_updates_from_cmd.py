# For refrence https://gist.github.com/anupamchugh/b0c732e9d1e2cf5cc3ce35ae795f6e7b

# Refrence https://towardsdatascience.com/5-python-tricks-to-make-your-life-more-productive-974ebeb54a53

#pip install yfinance

import json
import sys
import urllib.request

if len(sys.argv) != 3:
	print("Usage: ./getcurrencyrates.py search_currency base_currency. Example: ./getcurrencyrates.py usd inr")
	sys.exit()

search_currency = sys.argv[1]
base_currency = sys.argv[2]

currencyurl = "http://freecurrencyrates.com/api/action.php?do=cvals&iso=" + search_currency + "&f=" + base_currency + "&v=1&s=cbr"
request = urllib.request.urlopen(currencyurl)
obj = json.loads(request.read())
result = "1 " + search_currency.upper() + " equals "
result+="{:,.2f}".format(1/obj[search_currency.upper()]) + " " + base_currency.upper()

print(result)

	