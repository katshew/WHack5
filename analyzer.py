import indicoio, math, sys
#sys.path.append('/var/www/whack/whack/yaklient')
from yaklient import *

class Analyzer:

    def __init__(self):
        # something I may or may not want to avoid doing
        indicoio.config.api_key = 'aa6ffe32458b5e6b3c41e9b4139315ae'
        self.yaks = []

    def get_weighted_average_sentiments(self):
        sentiment_sum = 0.0

        yak_info = [[yak.message, yak.likes] for yak in self.yaks]

        upvotes = [yak[1] for yak in yak_info]
        sentiments = indicoio.sentiment_hq([yak[0] for yak in yak_info])

        entries = len(upvotes) + sum([math.fabs(upvote) for upvote in upvotes])

        for index in range(len(sentiments)):
            sentiment_sum += sentiments[index] * upvotes[index]

        return sentiment_sum/entries

    def get_keywords_for_yaks(self):
        keywords = dict()
        yak_list = [yak.message for yak in self.yaks]
        words_for_yaks = indicoio.keywords(yak_list)

        all_words = []
        for word_list in words_for_yaks:
            all_words += word_list

        all_words.sort()
        token = all_words[0]
        count = 0

        for word in all_words:
            if(word != token):
                keywords[word] = count
                count = 1
                token = word
            else:
                count += 1

        return keywords

    def get_yaks_by_coords(self, latitude, longitude):
        user = User(Location(42.2964, -71.2931), "AB9126086390455FA9DA7BAFB95B0D81")
        yaks = user.get_yaks(Location(latitude, longitude))
        self.yaks = yaks
        return yaks

    def get_political_analysis(self):
        political_sentiment = {}
