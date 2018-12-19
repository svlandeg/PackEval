import time
from functools import partial

from be.svlandeg.packeval.nlp.nltk_wrapper import NLTK
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

    return result


if __name__ == '__main__':
    """ Run and time a list of (combination of) different methods """

    my_text = "An example sentence, in English, which is supposed to be used for quick ... testing of, erm, " \
              "let's see.. the generation of n-grams and bag-of-words features!"

    my_n = range(2, 6)

    print()
    f_tokenize_nolib = partial(NoLib.tokenize_words, my_text)
    tokens_nolib = time_function(f_tokenize_nolib, "NoLib tokenizer")

    print()
    f_tokenize_nltk = partial(NLTK.tokenize_words, my_text)
    tokens_nltk = time_function(f_tokenize_nltk, "NLTK tokenizer")

    for n in my_n:
        print()
        f_nltk = partial(NLTK.ngrams, n, tokens_nolib)
        time_function(f_nltk, "NLTK " + str(n) + "-gram with tokens_nolib")

        print()
        f_nolib = partial(NoLib.ngrams, n, tokens_nolib)
        time_function(f_nolib, "NoLib " + str(n) + "-gram with tokens_nolib")

        print()
        f_nltk = partial(NLTK.ngrams, n, tokens_nltk)
        time_function(f_nltk, "NLTK " + str(n) + "-gram with tokens_nltk")

        print()
        f_nolib = partial(NoLib.ngrams, n, tokens_nltk)
        time_function(f_nolib, "NoLib " + str(n) + "-gram with tokens_nltk")


