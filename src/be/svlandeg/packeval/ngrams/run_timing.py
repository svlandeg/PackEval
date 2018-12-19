import time
from functools import partial

from be.svlandeg.packeval.ngrams.nltk_wrapper import NLTK
from be.svlandeg.packeval.ngrams.no_lib import NoLib


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

    my_n = range(2, 6)

    for n in my_n:
        print()
        f_nltk = partial(NLTK.ngrams_split, n, my_text)
        time_function(f_nltk, "NLTK " + str(n) + "-gram split()")

        print()
        f_nolib = partial(NoLib.ngrams_split, n, my_text)
        time_function(f_nolib, "NoLib " + str(n) + "-gram split()")


