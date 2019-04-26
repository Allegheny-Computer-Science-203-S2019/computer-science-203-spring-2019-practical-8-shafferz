"""Sort the list for the top twenty-five words in a plugin style"""

import collections


def top25(word_list):
    """Extract the most common words from list using collections"""
    counts = collections.Counter(w for w in word_list)
    return counts.most_common(25)
