# For refrence https://thecleverprogrammer.com/2021/11/30/useful-python-scripts/

import re
import nltk
import nltk
from nltk.corpus import stopwords
import string
nltk.download('stopwords')
stemmer = nltk.SnowballStemmer("english")
stopword=set(stopwords.words('english'))


def clean(text):
	text = str(text).lower()
	text = re.sub('\[.*?\]', '', text)
	text = re.sub('https?://\S+|www\.\S+', '', text)
	text = re.sub('<.*?>+', '', text)
	text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
	text = re.sub('\n', '', text)
	text = re.sub('\w*\d\w*', '', text)
	text = [word for word in text.split(' ') if word not in stopword]
	text=" ".join(text)
	text = [stemmer.stem(word) for word in text.split(' ')]
	text=" ".join(text)
	return text
