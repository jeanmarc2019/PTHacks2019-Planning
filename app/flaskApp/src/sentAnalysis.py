from textblob import TextBlob
import re
import pandas


class sentAnalysis:
    def __init__(self, body):
        self.body = body

    def analyze(self):
        text = re.sub('[^a-zA-Z]', ' ', self.body)
        text = text.lower()
        text=re.sub("&lt;/?.*?&gt;"," &lt;&gt; ",text)
        text=re.sub("(\\d|\\W)+"," ",text)

        obj = TextBlob(text)
        sent = obj.sentiment.polarity
        return(sent)

"""
dataset = pandas.read_csv('data.csv')
body = dataset['Body'][1]
analysis = sentAnalysis(body)
sent = analysis.analyze()
print(sent)
"""