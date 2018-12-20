class NoLib:
    @staticmethod
    def ngrams(n, tokens):
        """ kudos to http://locallyoptimal.com/blog/2013/01/20/elegant-n-gram-generation-in-python/ """
        return list(zip(*[tokens[i:] for i in range(n)]))

    @staticmethod
    def tokenize_words(text):
        """ Ridiculous (and frequently used) tokenization method """
        return text.split()

