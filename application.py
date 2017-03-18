import twitter
import pprint
import json
import sys
import inspect
import os

tweets_path = 'tweets/'


# Functions available
'''
timeline
random
'''

# API Twitter authorization process
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
#####


def main():
	OPTIONS = {
	    'timeline': (timeline, [sys.argv[i] for i in range(2, len(sys.argv))]),
	    'random' : (random, None)
	    }

	if(len(sys.argv)) < 2 or sys.argv[1] not in OPTIONS:
		print('Please, specify a valid argument')
		print('Possible argument:')
		for key, value in OPTIONS.items():
		    print(key)
		exit()

	OPTIONS[sys.argv[1]][0](OPTIONS[sys.argv[1]][1]) if OPTIONS[sys.argv[1]][1] != None else OPTIONS[sys.argv[1]][0]()



# Get the Twitter maixmum limitation of 16*200 tweets for a use
def timeline(name):
        #ensure name is a list 
	if type(name) == type(''):
	    name = [name]
	tweets = []	
	screen_names = name
	max_id=None
	for sceen_name in screen_names:
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
            filename = screen_name + '.json'
            _saveInJson(tweets, filename)	
	print('Done')

def random():

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

#Get a stream of tweet and print it as Json
#Parameters: number of tweet wanted, 0 for no limit
#TODO: function to write in json file directly
def random(count):
        count = int(count)
	result = api.GetStreamSample()
	print('[')
	for r in result:
            count -= 1
            if 'delete' in r:
                    continue
            tweetFormat = json.dumps(r) + ', ' if count > 0 else json.dumps(r) + ']'
            print(tweetFormat)
            if count == 0:
                break
            

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
