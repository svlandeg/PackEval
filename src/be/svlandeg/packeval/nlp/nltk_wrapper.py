from be.svlandeg.packeval.nlp.nlp_lib import NLPlib
from typing import List

import nltk


class NltkWrapper(NLPlib):

    def __init__(self):
        super().__init__("NLTK")

    def ngrams(self, n, tokens) -> List[str]:
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

    def everygrams(self, max_n, tokens):
        return list(nltk.everygrams(tokens, max_len=max_n))

    def tokenize_words(self, text) -> List[str]:
        # nltk.download('punkt')
        return nltk.word_tokenize(text)

    def tokenize_sentences(self, text) -> List[str]:
        return list()
