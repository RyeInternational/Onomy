
from nltk.sentiment.vader import *

def polarity_scores(self,text):
            """
            Return a float for sentiment strength based on the input text.
            Positive values are positive valence, negative value are negative
            valence.
            """
            # text, words_and_emoticons, is_cap_diff = self.preprocess(text)
            sentitext = SentiText(text, self.constants.PUNC_LIST,self.constants.REGEX_REMOVE_PUNCTUATION)
            sentiments = []
            words_and_emoticons = sentitext.words_and_emoticons
            for item in words_and_emoticons:
                valence = 0
                i = words_and_emoticons.index(item)
                if (
                    i < len(words_and_emoticons) - 1
                    and item.lower() == "kind"
                    and words_and_emoticons[i + 1].lower() == "of"
                ) or item.lower() in self.constants.BOOSTER_DICT:
                    sentiments.append(valence)
                    continue

                sentiments = self.sentiment_valence(valence, sentitext, item, i, sentiments)

            sentiments = self._but_check(words_and_emoticons, sentiments)
            zip_iterator = zip(words_and_emoticons, sentiments)
            D= dict(zip_iterator)

            return D,self.score_valence(sentiments,text)
