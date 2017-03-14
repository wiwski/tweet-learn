import twitter
apiTks = {
	'TWITTER_CONSUMER_KEY' : os.environ.get('TWITTER_CONSUMER_KEY'),
	'TWITTER_CONSUMER_SECRET' : os.environ.get('TWITTER_CONSUMER_SECRET'),
	'ACCESS_TOKEN_KEY' : os.environ.get('ACCESS_TOKEN_KEY'),
	'ACESS_TOKEN_SECRET' : os.environ.get('ACESS_TOKEN_SECRET')
}
api = twitter.Api(consumer_key=apiTks['TWITTER_CONSUMER_KEY'],
			consumer_secret=apiTks['TWITTER_CONSUMER_SECRET'],
			access_token_key=apiTks['ACCESS_TOKEN_KEY'],
			access_token_secret=apiTks['ACESS_TOKEN_SECRET'])


result = api.GetStreamSample()
for r in result:
	print(len(r))
