"""Perform the extraction of words in a plugin style"""

import re
import string


def extract_words(path_to_file):
    """Extract the words from the specified file"""
    with open(path_to_file) as f:
        str_data = f.read()
    pattern = re.compile(r"[\W_]+")
    word_list = pattern.sub(" ", str_data).lower().split()
    with open("stopwords/stop_words.txt") as f:
        stop_words = f.read().split(",")
    stop_words.extend(list(string.ascii_lowercase))
    return [w for w in word_list if w not in stop_words]
