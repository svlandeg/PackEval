from abc import ABC, abstractmethod
from typing import List


class NLPlib(ABC):

    def __init__(self, name):
        self.name = name
        super().__init__()

    @abstractmethod
    def ngrams(self, n, tokens) -> List[str]:
        raise NotImplementedError('ngrams for ' + self.name)

    @abstractmethod
    def everygrams(self, n, tokens) -> List[str]:
        raise NotImplementedError('everygrams for ' + self.name)

    @abstractmethod
    def tokenize_words(self, text) -> List[str]:
        raise NotImplementedError('tokenize_words for ' + self.name)

    @abstractmethod
    def segment_sentences(self, text) -> List[str]:
        raise NotImplementedError('tokenize_sentences for ' + self.name)


