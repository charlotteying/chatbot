import re
import pandas
from datetime import datetime

# Opening JSON file as dataframe
df = pandas.read_csv('que-faire-a-paris-.csv', delimiter = ';')

#cleaning description
df = df[df['Date de fin'] > str(datetime.today().strftime('%Y-%m-%d'))]
df['Description'] = df['Description'].apply(lambda x: re.sub('<[^<]+?>', '', x))