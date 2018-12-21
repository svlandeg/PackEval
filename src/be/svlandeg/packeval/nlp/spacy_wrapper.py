from be.svlandeg.packeval.nlp.nlp_lib import NLPlib
from typing import List

from spacy.lang.en import English


class SpacyWrapper(NLPlib):

    def __init__(self):
        super().__init__("spaCy")

    def ngrams(self, n, tokens) -> List[str]:
        raise NotImplementedError('ngrams for ' + self.name)

    def everygrams(self, max_n, tokens):
        raise NotImplementedError('everygrams for ' + self.name)

    def tokenize_words(self, text) -> List[str]:
        nlp = English()
        doc = nlp(text)
        return [token.text for token in doc]
