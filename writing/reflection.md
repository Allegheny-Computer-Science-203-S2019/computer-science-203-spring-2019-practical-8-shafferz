# Reflection by Zac Shaffer

## Explain in detail the steps to take to compile and install the plugins

First, add the
`mv ../plugins/frequencies2.cpython-36.pyc ../plugins/frequencies2.pyc` and
`mv ../plugins/words2.cpython-36.pyc ../plugins/words2.pyc` to the file
`plugins-compile-and-install.sh`, if you haven't already. There should also be
corresponding `mv` commands for `frequencies1` and `words1` respectively. Then,
compile the plugins with the command `./plugins-compile-and-install.sh`. This
will compile the plugins. Then, make sure your program loads the plugins with
the lines:

```
words_plugin = config.get("Plugins", "words")
frequencies_plugin = config.get("Plugins", "frequencies")
```

In the `load_plugins()` method. If the `config.ini` file has the settings for
`words` and `frequencies`, then the program should load the appropriate plugins
 and the code should work.

## What are the benefits associated with adopting the plugin programming style?

Please provide a response to this question.

## Explain the challenges that you encountered and how you overcame them

Please provide a response to this question.
