from nltk import bigrams, trigrams


class NLTK:
    @staticmethod
    def ngrams_split(n, text):

        # bigrams using split() on spaces
        if n == 2:
            result = list(bigrams(text.split()))
            return result

        # trigrams using split() on spaces
        if n == 3:
            result = list(trigrams(text.split()))
            return result

        # default: not supported option returning empty list
        return list()



