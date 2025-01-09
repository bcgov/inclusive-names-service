# Some Complexities 
## Normalization and Segmentation
Some of the complexity of dealing with Unicode text comes from the relationship between what appear as single symbols in a language and the binary code that represents these symbols internally (i.e. as binary 0's and 1's). There are two issues:
1. A particular symbol, aka grapheme, may be represented by Unicode characters in different ways. For example, the grapheme “é” may be represented by a [single Unicode character](https://www.compart.com/en/unicode/U+00E9) or by a combination of two Unicode characters: ["e"](https://www.compart.com/en/unicode/U+0065) combined with an [acute accent](https://www.compart.com/en/unicode/U+0301), This calls for the need for a way of representing symbols as Unicode characters consistently; this process is called [Normalization](./normalization/README.md).
2. Given a string of text as binary data, it's not always clear where the parts corresponding to one symbol and and the parts for the next symbol begin. The mechanism for determining this is called [Segmentation](./segmentation/README.md).

## AnyAscii
Not all systems are capable of storing Unicode data, so for these systems there needs to be a way of consistenly representing Unicode text using just [ASCII](../glossary.md#ascii) characters. A commonly used mechanism for doing this is [AnyASCII](https://anyascii.com). 

## Sorting Unicode
Sorting strings of Unicode data can lead to unsatisfactory results, since many sorting mechanisms sort characters based on their [code point](../glossary.md#code-point) values. This works well for ASCII values, where code points are ordered according to the A-Z alphabet. However, binary sorting methods place non-Latin Unicode character either before A or after Z. This would make it hard to find a name starting with an Indigenous non-Latin character (e.g., λ). [This section](./UCA_sorting/) provides information on this, as well as sample code.
