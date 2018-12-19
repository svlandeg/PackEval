class NoLib:
    @staticmethod
    # kudos to http://locallyoptimal.com/blog/2013/01/20/elegant-n-gram-generation-in-python/
    def ngrams_split(n, text):
        return list(zip(*[text.split()[i:] for i in range(n)]))

