import os
from searchtweets.credentials import load_credentials
from searchtweets.api_utils import gen_rule_payload
from searchtweets.result_stream import collect_results
premium_search_args = load_credentials("~/.twitter_keys.yaml", yaml_key="search_tweets_premium", env_overwrite=False)

rule = gen_rule_payload("#immigrazione OR #immigrati OR #migrazione OR #migranti", results_per_call=100)

tweets = collect_results(rule,max_results=100,result_stream_args=premium_search_args)

for tweet in tweets[0:10]:
    print(tweet.created_at_datetime)