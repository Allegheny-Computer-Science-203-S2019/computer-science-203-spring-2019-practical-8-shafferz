"""Sort the list for the top twenty-five words in a plugin style"""

import operator


def top25(word_list):
    """Extract the most common words from list using custom approach"""
    word_freqs = {}
    for w in word_list:
        if w in word_freqs:
            word_freqs[w] += 1
        else:
            word_freqs[w] = 1
    return sorted(word_freqs.items(), key=operator.itemgetter(1), reverse=True)[:25]
