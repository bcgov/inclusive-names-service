The first thing you need to do is to modify your php.ini file to use UTF-8 as the default character set:

default_charset = "utf-8";

You can verify with phpinfo()

NOTE my example uses php 7.4.33 the newest version of php, previous versions might require additional work however in both 8 and 7.4.33 utf-8 was already set as the default.

## Gotchas
using most of the builtin string functions will almost certainly yield unhappiness. For instance what you likely want is grapheme_strlen not strlen and grapheme_substr no substr or $str\[$ind]