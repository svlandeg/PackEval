from spacy.lang.en import English


class SpacyWrapper:
    @staticmethod
    def ngrams(n, tokens):
        # TODO
        pass

    @staticmethod
    def everygrams(max_n, tokens):
        # TODO
        pass

    @staticmethod
    def tokenize_words(text):
        nlp = English()
        doc = nlp(text)
        return [token.text for token in doc]
