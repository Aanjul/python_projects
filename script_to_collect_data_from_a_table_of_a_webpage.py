# For refrence https://thecleverprogrammer.com/2021/11/30/useful-python-scripts/

import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

html = urlopen("https://en.wikipedia.org/wiki/List_of_circulating_currencies")
soup = BeautifulSoup(html, "html.parser")
table = soup.findAll("table", {"class":"wikitable"})[0]
rows = table.findAll("tr")

with open("Dataset.csv", "wt+", newline="") as f:
	writer = csv.writer(f)
	for i in rows:
		row = []
		for cell in i.findAll(["td", "th"]):
			row.append(cell.get_text())
		writer.writerow(row)
data = pd.read_csv("Dataset.csv")
data.head()