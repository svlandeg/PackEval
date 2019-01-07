import time
from functools import partial

from be.svlandeg.packeval.nlp.nltk_wrapper import NltkWrapper
from be.svlandeg.packeval.nlp.spacy_wrapper import SpacyWrapper, SpacyModelWrapper
from be.svlandeg.packeval.nlp.no_lib import NoLib
from be.svlandeg.packeval.io import read_ud


def experiment_crossovers(n_range, print_results=True):
    # TOKENIZATION
    tokens_nltk = time_function(partial(NltkWrapper().tokenize_words, my_text), "NLTK tokenizer")
    tokens_spacy = time_function(partial(SpacyWrapper().tokenize_words, my_text), "Spacy tokenizer")

    # NGRAMS
    for n in n_range:
        time_function(partial(NltkWrapper().ngrams, n, tokens_spacy), "NLTK " + str(n) + "-gram with spaCy tokens", ' ')
        time_function(partial(NoLib().ngrams, n, tokens_spacy), "NoLib " + str(n) + "-gram with spaCy tokens", ' ')
        time_function(partial(NltkWrapper().ngrams, n, tokens_nltk), "NLTK " + str(n) + "-gram with NLTK tokens", ' ')
        time_function(partial(NoLib().ngrams, n, tokens_nltk), "NoLib " + str(n) + "-gram with NLTK tokens", ' ')

    # EVERY GRAMS
    time_function(partial(NltkWrapper().everygrams, my_n.stop, tokens_spacy), "NLTK everygram with spaCy tokens and max " + str(my_n.stop), print_results)
    time_function(partial(NltkWrapper().everygrams, my_n.stop, tokens_nltk), "NLTK everygram with NLTK tokens and max " + str(my_n.stop), print_results)


def experiment_word_tokens(print_results=True):
    my_libs = {NoLib(), NltkWrapper(), SpacyWrapper()}

    for lib in my_libs:
        time_function(partial(lib.tokenize_words, my_text), lib.name + " tokenizer", print_results)


def experiment_sentence_boundaries(print_results=True):
    my_libs = {NoLib(), NltkWrapper(), SpacyWrapper(), SpacyModelWrapper('en_core_web_sm')}

    for lib in my_libs:
        time_function(partial(lib.segment_sentences, my_text), lib.name + " sentence tokenizer", print_results)


def time_function(f, name, print_results, join_char=''):
    """ Perform a certain function and print the timing & functional results """
    print("EXECUTING", name)

    start = time.time()
    result = f()
    end = time.time()

    print(" result length:", len(result))
    if print_results:
        print(" result:", *map(join_char.join, result), sep=' // ')
    print(" timing (ms):", end-start)
    print()

    return result


if __name__ == '__main__':
    """ Run and time a list of (combination of) different methods """

    # my_text = "An example sentence - in English - which is supposed to be used for quick ... testing of, erm, .. " \
    #          "let's see.. the generation of ..... n-grams and bag-of-words features! Oh and here's another sentence? Right."
    my_text = read_ud.read_english_training()
    my_n = range(1, 6)

    # EXPERIMENT 1 : tokens & n-grams
    # print("#### N-GRAMS ####")
    # experiment_crossovers(my_n)

    # EXPERIMENT 2 : word tokenization
    # print("#### WORD TOKENS ####")
    # experiment_word_tokens()

    # EXPERIMENT 3 : sentence tokenization
    print("#### SENTENCES ####")
    experiment_sentence_boundaries(print_results=False)
