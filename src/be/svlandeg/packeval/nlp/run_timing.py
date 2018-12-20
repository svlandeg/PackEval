import time
from functools import partial

from be.svlandeg.packeval.nlp.nltk_wrapper import NltkWrapper
from be.svlandeg.packeval.nlp.spacy_wrapper import SpacyWrapper
from be.svlandeg.packeval.nlp.no_lib import NoLib


def time_function(f, name):
    """ Perform a certain function and print the timing & functional results """
    print("EXECUTING", name)

    start = time.time()
    result = f()
    end = time.time()

    print(" result length:", len(result))
    print(" result:", *map(' '.join, result), sep=' / ')
    print(" timing (ms):", end-start)
    print()

    return result


if __name__ == '__main__':
    """ Run and time a list of (combination of) different methods """

    my_text = "An example sentence - in English - which is supposed to be used for quick ... testing of, erm, .. " \
              "let's see.. the generation of ..... n-grams and bag-of-words features! Oh and here's another sentence."

    my_n = range(1, 6)

    # TOKENIZATION
    tokens_nolib = time_function(partial(NoLib.tokenize_words, my_text), "NoLib tokenizer")
    tokens_nltk = time_function(partial(NltkWrapper.tokenize_words, my_text), "NLTK tokenizer")
    tokens_spacy = time_function(partial(SpacyWrapper.tokenize_words, my_text), "Spacy tokenizer")

    # NGRAMS
    for n in my_n:
        time_function(partial(NltkWrapper.ngrams, n, tokens_nolib), "NLTK " + str(n) + "-gram with tokens_nolib")
        time_function(partial(NoLib.ngrams, n, tokens_nolib), "NoLib " + str(n) + "-gram with tokens_nolib")
        time_function(partial(NltkWrapper.ngrams, n, tokens_nltk), "NLTK " + str(n) + "-gram with tokens_nltk")
        time_function(partial(NoLib.ngrams, n, tokens_nltk), "NoLib " + str(n) + "-gram with tokens_nltk")

    # EVERY GRAMS
    time_function(partial(NltkWrapper.everygrams, my_n.stop, tokens_nolib), "NLTK everygram with tokens_nolib and max " + str(my_n.stop))
    time_function(partial(NltkWrapper.everygrams, my_n.stop, tokens_nltk), "NLTK everygram with tokens_nltk and max " + str(my_n.stop))
