__author__ = 'Jake'

from pyechonest import config
from pyechonest import song
import os, csv, math

config.ECHO_NEST_API_KEY = "DLBFUV54VPZIDBJO7"

""" rkp_results = song.search(mood="happy, excited", artist_min_familiarity=.75)

 """

def categorize_tweets_csv():
    for tweetsfile in os.listdir(os.getcwd()):
        excitements = []
        happy = 0
        exclamations = 0
        counter_num = 0
        if tweetsfile.endswith(".csv"):
            print tweetsfile
            with open(tweetsfile, 'r') as csvfile:
                csvreader = csv.reader(csvfile)
                for tweet, sentiment, accuracy in csvreader:
                    counter_num += 1
                    # parseme = nltk.word_tokenize(tweet)
                    # parseme = nltk.pos_tag(parseme)
                    # for word, classification in parseme:
                    #     counter = 0
                    #     if classification == "JJ":
                    #         counter += 1
                    #     tweet_excitement = counter / len(parseme)
                    #     excitements.append(tweet_excitement)
                    #     print tweet_excitement
                    if sentiment == "positive" and accuracy >= 50:
                        happy += 1
                    if tweet.count("!") > 1 and tweet.count(".") <= 1:
                       exclamations += 1

            exclamation_percentage = exclamations / float(counter_num)
            # excitement = (sum(excitements) + exclamations) / float(len(excitements))
            happy /= float(counter_num)
            if exclamation_percentage > .15:
                if happy > .4:
                    mood = "happy"
                else:
                    mood = "angry"
            else:
                if happy > .4:
                    mood = "relaxed"
                else:
                    mood = "sad"
            rkp_results = song.search(mood=mood, min_energy=exclamation_percentage, artist_min_familiarity=.6, style="pop", artist_start_year_after="1999")
            resultant_song = rkp_results[0]
            print resultant_song.title + " - " + resultant_song.artist_name + " happy " + str(happy) + " excite " + str(exclamation_percentage)

categorize_tweets_csv()




