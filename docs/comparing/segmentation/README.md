# Segmenting Unicode strings
## Introduction
When reading a stream of [ASCII](../../glossary.md#ascii) text as binary data it's quite simple to parse the stream into characters, as each character corresponds to exactly one byte of data.

The parsing is more complicated with [UTF-8](../../glossary.md#utf-8) encoded Indigenous language text, however. This is due to two reasons:

* The UTF-8 encoding is multi-byte and variable (each character uses between 1 and 4 bytes). This complexity is handled well by standard UTF-8 read/write methods.
* Secondly, some Indigenous language symbols are made up of multiple Unicode characters, superimposed on one another. These combinations of 1 or more characters are referred to as [graphemes](../../glossary.md#grapheme). There needs to be some way of reliably and consistently splitting text into graphemes. This is known as [segmentation](https://unicode.org/reports/tr29/).

## Program Example of Segmentation

The Python 3 program [utf8.py](../../programming_languages/python3/utf8.py) uses the [grapheme](https://pypi.org/project/grapheme/) library to parse a string of text into graphemes.

Similar libraries are available in other programming languages.