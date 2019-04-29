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

The plugin style makes completing the task easier, as having completed code
written for you in the form of a plugin translates to a lack of needing to
write and understand the code structure and content. Furthermore, by using
plugins, it makes accomplishing the task of counting the frequencies of the
words in the given input as simple as adding the plugin(s) as a dependency,
rather than having to write the module yourself. If the plugin has no red
flags or bugs, then you can rest assured that your code will also be
appropriate.

## Explain the challenges that you encountered and how you overcame them

This assignment was relatively easy. I am extremely pleased with only having to
write 50 words instead of 100 for the reflection, so I don't have to add poor or
unnecessary verbiage to pass the checks. The hardest part was understanding the
relationships between the given `.sh` file, the `config.ini` file, and the
source code itself.
