import indicoio, math

class Analyzer:

    def __init__(self):
        # something I may or may not want to avoid doing
        indicoio.config.api_key = 'aa6ffe32458b5e6b3c41e9b4139315ae'

    def get_weighted_average_sentiments(self, yaks):
        entries = 0.0
        sentiment_sum = 0.0

        for yak in yaks:
            message = yak.message
            upvotes = yak.likes

            entries += (1 + math.fabs(upvotes))
            sentiment_sum += indicoio.sentiment_hq(message) * upvotes

        return sentiment_sum/entries

    def get_keywords_for_yaks(self, yaks):
        keywords = {}

        for yak in yaks:
            message = yak.message

            words_for_yak = indicoio.keywords(message)

            for word in words_for_yak:
                occ = keywords.get(word, 0)
                keywords[word] = occ+1

        return keywords                