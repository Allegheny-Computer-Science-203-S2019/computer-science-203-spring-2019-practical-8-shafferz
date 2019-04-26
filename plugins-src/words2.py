"""Perform the extraction of words in a plugin style"""

import re


def extract_words(path_to_file):
    """Extract the words from the specified file"""
    words = re.findall("[a-z]{2,}", open(path_to_file).read().lower())
    stopwords = set(open("stopwords/stop_words.txt").read().split(","))
    return [w for w in words if w not in stopwords]
