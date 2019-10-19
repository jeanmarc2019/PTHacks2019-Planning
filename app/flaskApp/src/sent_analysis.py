import pandas, nltk
from textblob import TextBlob
from newspaper import Article


df = pandas.read_csv('data.csv')

pos_sent = []
neg_sent = []
neutral = []

for index, row in df.iterrows():
    
    summary = row["Summary"]
    body = row['Body']

    if type(summary) is not float:
        
        sum_obj = TextBlob(summary)
        sum_sentiment = sum_obj.sentiment.polarity

        body_obj = TextBlob(body)
        body_sentiment = body_obj.sentiment.polarity

        print(sum_sentiment, body_sentiment)
        