# For refrence https://github.com/Logan1x/Python-Scripts/blob/master/bin/fetch_html.py


import urllib.request
import sys
from lxml import html

if len(sys.argv) < 2:
# put file name and http url of the website here
	print('Usage example: python script_fetch_html_response_from_provided_url_&_parse_xml_tag_to_get_only_text_content_&_print_out.py https://github.com')
	sys.exit(1)
	
url = sys.argv[1]
response = urllib.request.urlopen(url)
html_text = response.read().decode('UTF-8')
text = html.fromstring(html_text).text_content()

print(text)

