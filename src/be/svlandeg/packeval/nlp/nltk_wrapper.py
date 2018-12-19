import nltk


class NLTK:
    @staticmethod
    def ngrams(n, tokens):
        # bigrams using split() on spaces
        if n == 2:
            result = list(nltk.bigrams(tokens))
            return result

        # trigrams using split() on spaces
        if n == 3:
            result = list(nltk.trigrams(tokens))
            return result

        # default: not supported option returning empty list
        return list()

    @staticmethod
    def tokenize_words(text):
        # nltk.download('punkt')
        return nltk.word_tokenize(text)
