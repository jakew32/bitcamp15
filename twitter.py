__author__ = 'Jake'

from TwitterSearch import *



def hashtagSearch(hashtag):
    ts = TwitterSearch(
            consumer_key = 'UIBl6otwQD9CtbhRQSQ2GlV8H',
            consumer_secret = 'MlxVNNZDWfEDBpOTbZwOAPQ8BziP3tcQwMoU3vXdxllzsdgjLu',
            access_token = '85289745-4PknFj4zSUPd12rbIg8ZkPnAAewZCEmwXj3wyNbiO',
            access_token_secret = 'A0RNhwgoVh0okZQoL5w6UydpplyTSft1Sx6QCZ4TtvaAC'
         )
    try:
        tso = TwitterSearchOrder() # create a TwitterSearchOrder object
        tso.set_keywords([hashtag]) # let's define all words we would like to have a look for
        tso.set_include_entities(False) # and don't give us all those entity information

        # it's about time to create a TwitterSearch object with our secret tokens


         # this is where the fun actually starts :)

        return ts.search_tweets(tso)
    except TwitterSearchException as e: # take care of all those ugly errors if there are some
        print(e)

def userSearch(user):
    ts = TwitterSearch(
            consumer_key = 'UIBl6otwQD9CtbhRQSQ2GlV8H',
            consumer_secret = 'MlxVNNZDWfEDBpOTbZwOAPQ8BziP3tcQwMoU3vXdxllzsdgjLu',
            access_token = '85289745-4PknFj4zSUPd12rbIg8ZkPnAAewZCEmwXj3wyNbiO',
            access_token_secret = 'A0RNhwgoVh0okZQoL5w6UydpplyTSft1Sx6QCZ4TtvaAC'
         )
    tuo = TwitterUserOrder(user) # create a TwitterUserOrder
    # start asking Twitter about the timeline
    return ts.search_tweets(tuo)

