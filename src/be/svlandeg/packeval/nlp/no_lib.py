import re

from be.svlandeg.packeval.nlp.nlp_lib import NLPlib
from typing import List


class NoLib(NLPlib):

    def __init__(self):
        super().__init__("NoLib")

    def ngrams(self, n, tokens):
        """ kudos to http://locallyoptimal.com/blog/2013/01/20/elegant-n-gram-generation-in-python/ """
        return list(zip(*[tokens[i:] for i in range(n)]))

    def everygrams(self, n, tokens) -> List[str]:
        """ TODO: currently not implemented """
        return list()

    def tokenize_words(self, text) -> List[str]:
        """ Ridiculous (and frequently used) tokenization method """
        return text.split()

    def tokenize_sentences(self, text) -> List[str]:
        return re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!)\s', text)

