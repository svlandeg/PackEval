import nltk


class NltkWrapper:
    @staticmethod
    def ngrams(n, tokens):
        # bigrams (unnecessary specific function in NLTK)
        if n == 2:
            result = list(nltk.bigrams(tokens))
            return result

        # trigrams (unnecessary specific function in NLTK)
        if n == 3:
            result = list(nltk.trigrams(tokens))
            return result

        # default: ngrams
        return list(nltk.ngrams(tokens, n))

    @staticmethod
    def everygrams(max_n, tokens):
        return list(nltk.everygrams(tokens, max_len=max_n))

    @staticmethod
    def tokenize_words(text):
        # nltk.download('punkt')
        return nltk.word_tokenize(text)
