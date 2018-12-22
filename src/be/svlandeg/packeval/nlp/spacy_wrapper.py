from be.svlandeg.packeval.nlp.nlp_lib import NLPlib
from typing import List

import spacy
from spacy.lang.en import English


class SpacyWrapper(NLPlib):

    def __init__(self):
        super().__init__("spaCy")

    def ngrams(self, n, tokens) -> List[str]:
        return list()

    def everygrams(self, max_n, tokens):
        return list()

    def tokenize_words(self, text) -> List[str]:
        nlp = English()
        doc = nlp(text)
        return [token.text for token in doc]

    def tokenize_sentences(self, text) -> List[str]:
        """ spaCy's rule-based implementation """
        nlp = English()
        sbd = nlp.create_pipe('sentencizer')
        nlp.add_pipe(sbd)
        doc = nlp(text)
        return [s.text for s in doc.sents]


class SpacyModelWrapper(SpacyWrapper):

    def __init__(self, model):
        super().__init__()
        self.name = "spaCy_" + model
        self.model = model

    def tokenize_sentences(self, text) -> List[str]:
        """ spaCy implementation using dependency parsing """
        # install this with: python -m spacy download en_core_web_sm
        nlp = spacy.load(self.model)
        doc = nlp(text)
        return [s.text for s in doc.sents]
