import twitter
import pprint
import json
import sys
import inspect
import os

tweets_path = 'tweets/'


##API Twitter authorization process
apiTks = {
	'TWITTER_CONSUMER_KEY' : os.environ.get('TWITTER_CONSUMER_KEY'),
	'TWITTER_CONSUMER_SECRET' : os.environ.get('TWITTER_CONSUMER_SECRET'),
	'ACCESS_TOKEN_KEY' : os.environ.get('ACCESS_TOKEN_KEY'),
	'ACESS_TOKEN_SECRET' : os.environ.get('ACESS_TOKEN_SECRET')
}
for key, value in apiTks.items():
	if value is None:
		print('Make sure to export your %s' % key)
		exit()
api = twitter.Api(consumer_key=apiTks['TWITTER_CONSUMER_KEY'],
			consumer_secret=apiTks['TWITTER_CONSUMER_SECRET'],
			access_token_key=apiTks['ACCESS_TOKEN_KEY'],
			access_token_secret=apiTks['ACESS_TOKEN_SECRET'])




def main():

	if(len(sys.argv)) < 2:
		exit('Please, specify an argumenent')

	param = sys.argv[2] if len(sys.argv) > 2 else None

	try:
		getattr(sys.modules[__name__], "%s" % sys.argv[1])(param)
	except AttributeError:
		exit('Please, specify a valid argument')
	
# Get the Twitter maixmum limitation of 16*200 tweets for a use
def timeline(name):
	tweets = []	
	screen_name= name
	#since_id=None
	max_id=None

	for i in range(0,16):
		results = api.GetUserTimeline(screen_name=screen_name, count=200,max_id=max_id)
		
		try:
			max_id = results[len(results)-1].id-1
		except IndexError:
			print('Limit reached')
			break
		for result in results:
			tweets.append(result.AsJsonString())
	
	print('%i tweets colleted' % len(tweets))
	_saveInJson(tweets)	

def random(self=None):
	result = api.GetStreamSample()
	for r in result:
		print(len(r))

def preprocess(datasource):
	data = _loadFromJson(datasource)

def check(self=None):
	tweets = _loadFromJson()	
	print(len(tweets))

def _loadFromJson(filename='tweets.json'):
	with open(tweets_path+filename, 'r') as f:
		tweets = json.load(f)
	f.closed
	return tweets

def _saveInJson(tweets, filename='tweets.json', path='tweets_path'):
	with open(path+filename, 'w') as f:
		json.dump(tweets, f)
	f.closed
	print('Tweets stored in %s' % filename)

if __name__ == '__main__':
	main()
