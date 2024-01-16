

# Glossary

#### <a id="ascii"></a> ASCII

ASCII is both a [character set](#character_set) and an [encoding](#encoding). This (very basic) character set includes the lower- and upper-case Latin alphabet (a-z, A-Z), the numeric digits (0-9), and some punctuation characters. There are 127 characters in the character set; a complete list of these characters can be found [here](https://en.wikipedia.org/wiki/ASCII#Character_set). ASCII characters are stored one character per [byte](#byte). They are stored in these bytes as integers between 1 and 127.

#### <a id="BMP"> Basic Multilingual Plane (BMP) </a>

The Unicode character set is divided into 16 planes, according to the value of the leading hexadecimal digit of the [code point](#code-point) value. The plane corresponding to "leading zero" code points is referred to as the [Basic Multilingual Plane](https://en.wikipedia.org/wiki/Plane_(Unicode)#Basic_Multilingual_Plane), or BMP. This plane has 65536 characters and includes all the characters used in modern languages (including Indigenous languages). With the [UTF-16](#utf16) encoding, these characters can be encoded using just 2 bytes. With the [UTF-8](#utf-8) encoding, BMP characters are encoded using 1,2,3,or 4 bytes.

#### <a id="BCSans"> [BC Sans font](https://www2.gov.bc.ca/gov/content?id=D56201B17F554B40BAB5A16FD2AB4C12)

"BC Sans is a new "living" typeface for government. It was developed to create an [Open Font License](https://opensource.org/licenses/OFL-1.1) set of fonts for improved readability and delivery of our digital services, and also contain support for multiple languages including Indigenous languages in B.C."

#### <a id="byte"> </a> byte 

A byte is the basic unit of storage in an information system. It consists of 8 bits, with each bit having the value 0 or 1. A byte can therefore store any integer with a value between 0 and 255.

#### <a id="character_set"> </a> character set

A character set is the set of characters supported by an information system. [Unicode](#unicode) and [ASCII](#ascii) are examples of character sets.

#### <a id="code_point"> </a> code point

A code point refers to a single character in the [Unicode](#unicode) character set. The set of code points provides a level of abstraction between the characters and the methods for [encoding](#encoding) them. Each code point has a numeric identifier and brief description of the associated character's general appearance. For example, Unicode code point for the small letter 'a' has a numeric identifier of '0061' (hexadecimal) and the description 'LATIN SMALL LETTER A'.

#### <a id="encoding"> </a>encoding

An encoding defines the way in which code points are stored as binary numbers (strings of 0's and 1's) in [bytes](#byte). [UTF-8](#utf8), [iso-8859-1](#latin1), [windows-1252](#windows1252) and [ASCII](#ascii) are all examples of encodings.

#### <a id="font"> </a> font

A font defines the visual appearance of code points. [BC Sans](#bc-sans-font) is one such font. Other examples of fonts are Times New Roman, Calibri, Arial, and Comic Sans.

#### <a id="glyph"> </a> glyph

A glyph is the visual representation of a[grapheme](#grapheme), as drawn using a particular [font](#font).

#### <a id="grapheme"> </a>  grapheme

A grapheme is the basic element of a language. In the English language, grapheme and character are synonymous; the letters a-z, A-Z, and the digits 0-9 are all graphemes. In other languages, though, a grapheme may correspond with a combination of two or more characters (or [code points](#code_point), in [Unicode](#unicode)). For example, in the name of the First Nations community Tk'emlúps te Secwe̓pemc, the grapheme "e̓" is a combination of the code points 'LATIN SMALL LETTER E' (code point 0065) and 'COMBINING COMMA ABOVE' (code point 0313).

#### <a id="unicode_ready"> </a> Unicode-Ready

An information system is Unicode-Ready if it is capable of ingesting, storing (as character data), and transmitting people, place, and business names that contain Unicode characters (including the Indigenous characters used in B.C. languages).

#### <a id="latin1"> </a> iso-8859-1(aka Latin1)

The iso-8859-1 encoding defines how characters in the 'Latin alphabet no. 1' character set are stored as binary numbers in [bytes](#byte) of data. There are 191 characters in this alphabet, consisting of the graphemes present in the languages used in western European countries (English, Italian, French. Spanish, German, etc.).

#### <a id="regex"> </a> Regular Expression

As defined in Wikipedia, "A  **regular expression**  … is a sequence of [characters](https://en.wikipedia.org/wiki/Character_(computing)) that specifies a [match pattern](https://en.wikipedia.org/wiki/Pattern_matching) in [text](https://en.wikipedia.org/wiki/String_(computer_science)). Usually such patterns are used by [string-searching algorithms](https://en.wikipedia.org/wiki/String-searching_algorithm) for "find" or "find and replace" operations on [strings](https://en.wikipedia.org/wiki/String_(computer_science)), or for [input validation](https://en.wikipedia.org/wiki/Data_validation). "

#### <a id="unicode"> </a> Unicode

Unicode is an internationally adopted character set with the potential to include every character present in any language that is used anywhere in the world, either currently or in the past. Since being introduced in the early 1990's, Unicode has gone through several revisions, with additional characters added every year. Unicode currently has approximately 150,000 characters, far more than what can encoded using one byte per character (as is done with the [ASCII](#ASCII), [iso-8859-1](#latin1), or [windows-1252](#windows1252). For this reason, Unicode has several multi-byte encoding options. The most popular of these encodings is [UTF-8](#utf8), which uses between 1 and 6 bytes per character.

#### <a id="utf8"> </a> UTF-8

UTF-8 is a popular option
 for encoding Unicode characters. The UTF-8 encoding is identical to the ASCII encoding for ASCII characters; these characters are encoding the same way in both encodings. However, characters outside the ASCII range are encoded using multiple bytes per character. Note that non-ASCII characters that consume just one byte in Windows-1252 or iso-8859-1 can require multiple bytes in UTF-8. For example, the "em-dash" (–) takes one byte to store using the Windows-1252 encoding, but it takes three bytes to store with UTF-8. So, changing the encoding used by a system from Windows-1252 to UTF-8 may result in more space being consumed.

Side note 1: The UTF in UTF-8 stands for "Unicode Transformation Format"; the 8 indicates that the encoding uses 8-bit numbers.

Side note 2: Other Unicode encodings are UTF-16, which uses either 2 or 4 bytes per character, and UTF-32, which uses 4 bytes (32 bits) per character. Both UTF-16 and UTF-32 will consume more space (at least 2 or 4 times as much) than UTF-8 for the characters found in ASCII.

#### <a id="utf16"> </a> UTF-16

With UTF-16 encoding, Unicode characters are stored using either 16 or 32 bits (i.e., 2 or 4 bytes). It is the internal encoding used by the Java and .Net programming languages. See [https://en.wikipedia.org/wiki/UTF-16](https://en.wikipedia.org/wiki/UTF-16)

#### <a id="utf32"> </a> UTF-32

With UTF-32 encoding, Unicode characters are always stored using 32 bits (i.e., 4 bytes). This is the only fixed-length encoding that supports the full spectrum of Unicode characters. See [https://en.wikipedia.org/wiki/UTF-32](https://en.wikipedia.org/wiki/UTF-32)

#### <a id="windows1252"> </a> windows-1252 (aka Western European)

The windows-1252 encoding provides an alternative to the [iso-8859-1](#latin1) encoding for representing Latin alphabet graphemes. It was the default encoding used in legacy Windows components.

#### <a id="word"> </a> word

Computer architectures typically group bytes into words, but not all architectures do this the same way. For example, Intel-based machines and Macs use a byte ordering called little-endian; Sparc (SUN) and mainframes use a different byte ordering, called big-endian. For this reason, systems that exchange encoded Unicode data sometimes expect a [Byte Order Mark (BOM)](https://en.wikipedia.org/wiki/Byte_order_mark) to precede the data, allowing them to understand both orderings. Excel is one such application; it expects UTF-8 data to be preceded by a BOM. UTF-8 with a BOM is sometimes referred to as UTF-8-BOM.


