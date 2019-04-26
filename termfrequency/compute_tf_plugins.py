"""Compute term frequencies for an input file using a plugin style"""

import sys
import configparser
import importlib.machinery

# TODO: Make sure to complete all of the steps in the following file
# TODO: Don't forget that the program will not work until you compile and load the plugins

def load_plugins():
    """Load the compiled Python plugins specified in the configuration file"""
    config = configparser.ConfigParser()
    # TODO: Add the name of the configuration file
    config.read("")
    # TODO: Add the name of the plugin that will load
    # either words1.pyc or words2.pyc
    words_plugin = config.get("Plugins", "")
    # TODO: Add the name of the plugin that will load
    # either frequencies1.pyc or frequencies2.pyc
    frequencies_plugin = config.get("Plugins", "")
    # pylint: disable=global-variable-undefined
    global tfwords, tffreqs
    # pylint: disable=no-value-for-parameter
    # pylint: disable=deprecated-method
    tfwords = importlib.machinery.SourcelessFileLoader(
        "tfwords", words_plugin
    ).load_module()
    tffreqs = importlib.machinery.SourcelessFileLoader(
        "tffreqs", frequencies_plugin
    ).load_module()


if __name__ == "__main__":
    # TODO: Make the call to the function that will load the plugins
    word_freqs = tffreqs.top25(tfwords.extract_words(sys.argv[1]))
    for (w, c) in word_freqs:
        print(w, " - ", c)
