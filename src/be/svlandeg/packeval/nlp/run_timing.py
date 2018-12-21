import time
from functools import partial

from be.svlandeg.packeval.nlp.nltk_wrapper import NltkWrapper
from be.svlandeg.packeval.nlp.spacy_wrapper import SpacyWrapper
from be.svlandeg.packeval.nlp.no_lib import NoLib


def experiment_crossovers(n_range):
    # TOKENIZATION
    tokens_nltk = time_function(partial(NltkWrapper().tokenize_words, my_text), "NLTK tokenizer")
    tokens_spacy = time_function(partial(SpacyWrapper().tokenize_words, my_text), "Spacy tokenizer")

    # NGRAMS
    for n in n_range:
        time_function(partial(NltkWrapper().ngrams, n, tokens_spacy), "NLTK " + str(n) + "-gram with spaCy tokens")
        time_function(partial(NoLib().ngrams, n, tokens_spacy), "NoLib " + str(n) + "-gram with spaCy tokens")
        time_function(partial(NltkWrapper().ngrams, n, tokens_nltk), "NLTK " + str(n) + "-gram with NLTK tokens")
        time_function(partial(NoLib().ngrams, n, tokens_nltk), "NoLib " + str(n) + "-gram with NLTK tokens")

    # EVERY GRAMS
    time_function(partial(NltkWrapper().everygrams, my_n.stop, tokens_spacy), "NLTK everygram with spaCy tokens and max " + str(my_n.stop))
    time_function(partial(NltkWrapper().everygrams, my_n.stop, tokens_nltk), "NLTK everygram with NLTK tokens and max " + str(my_n.stop))


def experiment_word_tokens():
    my_libs = {NoLib(), NltkWrapper(), SpacyWrapper()}

    for lib in my_libs:
        tokens = time_function(partial(lib.tokenize_words, my_text), lib.name + " tokenizer")
        bow = time_function(partial(NoLib().ngrams, 1, tokens), lib.name + " BOW")
        print()


def experiment_sentence_boundaries():
    tokens_dep = time_function(partial(SpacyWrapper().tokenize_sentences_dep, my_text), " spaCy dep sentence tokenizer")
    sentences_dep = time_function(partial(NoLib().ngrams, 1, tokens_dep), " BOW")
    print()
    tokens_rules = time_function(partial(SpacyWrapper().tokenize_sentences_rules, my_text), " spaCy dep sentence tokenizer")
    sentences_rules = time_function(partial(NoLib().ngrams, 1, tokens_rules), " BOW")


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

    # EXPERIMENT 1 : tokens & n-grams
    # experiment_crossovers(my_n)

    # EXPERIMENT 2 : word tokenization
    # experiment_word_tokens()

    # EXPERIMENT 3 : sentence tokenization
    experiment_sentence_boundaries()
