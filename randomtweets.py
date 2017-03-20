import json
from sklearn.feature_extraction.text import TfidfVectorizer


class RT:

    def __init__(self, source='tweets/random.json'):
        self.source = source
        self.tweets = self.loadTweets()

    def loadTweets(self):
        tweetList = []
        with open(self.source, 'r') as f:
            tweets = json.load(f)
        return tweets

    def transform(self):
        tfidf = TfidfVectorizer()
        tw = tfidf.fit_transform(self.tweets)
       # tname = tfidft_transformer.get_features_names()
        print(tw)
        
