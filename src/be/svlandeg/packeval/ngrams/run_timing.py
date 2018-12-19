import time
from functools import partial

from be.svlandeg.packeval.ngrams.nltk_wrapper import NLTK


# Perform a certain function and print the timing & functional results
def time_function(f, name):
    print("EXECUTING", name)

    start = time.time()
    result = f()
    end = time.time()

    print(" result length:", len(result))
    print(" result:", *map(' '.join, result), sep=' / ')
    print(" timing (ms):", end-start)


if __name__ == '__main__':
    my_text = "An example sentence, in English, which is supposed to be used for quick ... testing of, erm, " \
              "let's see.. the generation of n-grams and bag-of-words features!"

    print()
    f_nltk_2 = partial(NLTK.ngrams_split, 2, my_text)
    time_function(f_nltk_2, "NLTK 2-gram spit()")

    print()
    f_nltk_3 = partial(NLTK.ngrams_split, 3, my_text)
    time_function(f_nltk_3, "NLTK 3-gram spit()")

    print()
    f_nltk_4 = partial(NLTK.ngrams_split, 4, my_text)
    time_function(f_nltk_4, "NLTK 4-gram spit()")

    print()

