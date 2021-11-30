import re
import pandas
from datetime import datetime
from sklearn.model_selection import train_test_split
import nltk
import spacy
import string

# Opening JSON file as dataframe
df = pandas.read_csv('que-faire-a-paris-.csv', delimiter = ';')

#cleaning description
df = df[df['Date de fin'] > str(datetime.today().strftime('%Y-%m-%d'))]
description = df['Description'].apply(lambda x: re.sub('<[^<]+?>', ' ', x))

#text analysis

nltk.download('stopwords')
nltk.download('punkt')

def Remove_Punct(text):
  result = "".join([ch for ch in text if ch not in string.punctuation])
  return result

pct = list(string.punctuation)

description['Description'] = description['Description'].apply(lambda x: Remove_Punct(x))

#nlp = fr_core_news_md.load()
nlp = spacy.load("fr_core_news_sm")
stopwords = nlp.Defaults.stop_words

training_sentences, test_sentences = train_test_split(df['Description'], test_size=0.8)

