import urllib
import re

print "we will try to open this url, in order to get IP Address"

url = "http://checkip.dyndns.org"

# //we will use to check the IP for is: http://checkip.dyndns.org

print url

request = urllib.urlopen(url).read()

theIP = re.findall(r"d{1,3}.d{1,3}.d{1,3}.d{1,3}", request)

print "your IP Address is:", theIP


# See this URL for refrence https://www.pythonforbeginners.com/code-snippets-source-code/check-your-external-ip-address/