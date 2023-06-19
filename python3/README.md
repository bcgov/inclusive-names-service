This example requires regex, installing them or setting up a virtual environment is left as an exercise to the reader

A note on graphemes
Depends on what you are looking for. graphemes() will return what users would perceive as single characters, even though they may contain more than one codepoint; for example a letter combined with an accent mark is a single grapheme. This is not the case with split().

Consider a + ◌́ . In this example, split() will return the two codepoints as separate characters whereas graphemes() will return a single character.

## Gotchas
- prefacing a sting with a u will switch it to unicode
- for graphemes you need the regex \X