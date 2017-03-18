import json
from sklearn.feature_extraction.text import TfidfTransformer


class RandomTweets:

    def __init__(self, source='tweets/random.json'):
        self.source = source
        self.tweets = self.loadTweets()

    def loadTweets(self):
        tweetList = []
        with open(self.source, 'r') as f:
            tweets = json.load(f)
        f.closed
        for tweet in tweets:
            tweetList.append(tweet['text'])
        return tweetList

    def transform(self):
        tfidf_transformer = TfidfTransformer()
        tw = tfidf_transformer.fit_transform(self.tweets)
        tname = tfidft_transformer.get_features_names()
        for i in range(0, 10):
            print(tname[i])
        print(tw.shape)
