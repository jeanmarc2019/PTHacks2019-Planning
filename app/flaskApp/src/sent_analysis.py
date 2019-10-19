import pandas, nltk
from textblob import TextBlob
from nltk.stem.porter import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
import re
import numpy

nltk.download('wordnet')
nltk.download('stopwords')

def sentAnalysis(dataset):
    pos_sent = []
    neg_sent = []
    neutral = []

    for index, row in dataset.iterrows():
        
        summary = row["Summary"]
        body = row['Body']

        if type(summary) is not float:
            
            sum_obj = TextBlob(summary)
            sum_sentiment = sum_obj.sentiment.polarity

            body_obj = TextBlob(body)
            body_sentiment = body_obj.sentiment.polarity

            print(sum_sentiment, body_sentiment)

    return 0 


def keywords(dataset):

    dataset['word_count'] = dataset['Body'].apply(
        lambda x: len(str(x).split(" "))
    )


    stem = PorterStemmer()

    stop_words = set(stopwords.words("english"))

    corpus = []

    for i in range(0, 1933):
        
        text = str(dataset['Body'][i])
        #print(text)
        
        text = re.sub('[^a-zA-Z]', ' ', text)
        
        
        text = text.lower()
        
        text=re.sub("&lt;/?.*?&gt;"," &lt;&gt; ",text)
        text=re.sub("(\\d|\\W)+"," ",text)
        text = text.split()
        
        ps=PorterStemmer()
        lem = WordNetLemmatizer()
        text = [lem.lemmatize(word) for word in text if not word in  
                stop_words] 

        text = " ".join(text)
        corpus.append(text)
        
    dataset['Corpus'] = corpus
    dataset.to_csv('data.csv')

    return 0

dataset = pandas.read_csv('data.csv')

