from twython import Twython

twitter = Twython()

api_url = 'https://api.twitter.com/1.1/tweets/search/30days/ProgettoG1.json'

constructed_url = twitter.construct_api_url(api_url, q='from:matteosalvinimi', result_type='recent')

print(constructed_url)