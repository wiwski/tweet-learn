import twitter


def runTest():
	checkApi()
	checkConf()

def checkApi():
	api = twitter.Api(consumer_key='DygFx4xgXvhigRsct5qTgo2pi',
			consumer_secret='X7ZIitk1lEqyDemaxnRFS4upOhyA8kjsFOadULGX8BAiDleb6l',
			access_token_key='2879744519-gWHl2JTvs9oy116ZH5bNchcAUD0CfczDc32KbSb',
			access_token_secret='HNTbPDZLAIMvlugONvaSpajW1srjkOLmXhGaHzuebUGbl')
	if api:
		print('Api loaded!')
	


def checkConf():
	with open(tweets_path+filename, 'r') as f:
		tweets = json.load(f)
	f.closed
	
	print('%i tweets in position' % len(tweets))




