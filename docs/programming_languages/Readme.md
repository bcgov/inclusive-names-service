# Unicode Support in Various Programming Languages

The following table summarizes the support that several popular languages provide for their native strings, Unicode strings, and strings of graphemes:

### String, Unicode Character, and Grapheme Support in Popular Computer Languages
| Language                                                                      | Native string type | Unicode character library | Unicode grapheme library |
|---|---|---|---
| C                                                                             | array of char | [wchar.h](https://pubs.opengroup.org/onlinepubs/007908799/xsh/wchar.h.html) | [utf8proc](https://juliastrings.github.io/utf8proc/) |
| C++                                                                           | array of char | [wchar.h](https://pubs.opengroup.org/onlinepubs/007908799/xsh/wchar.h.html) | [utf8proc](https://juliastrings.github.io/utf8proc/) |
| C#                                                                            | String (Stored internally as an array of UTF-16 Unicode characters) | Supported natively | [GraphemeSplitter (There are several alternatives)](https://github.com/ufcpp/GraphemeSplitter) |
| Go                                                                            | [“slice” of bytes](https://blog.golang.org/slices) | [unicode](https://pkg.go.dev/unicode) | [uax29](https://github.com/clipperhouse/uax29/) |
| Java                                                                          | String (Stored internally as an array of UTF-16 Unicode characters) | Supported natively | grapheme-splitter-lite (See also ICU4J documentation) |
| Javascript                                                                    | String (Stored internally as an array of UTF-16 Unicode characters) | Supported natively | [Intl.Segmenter](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Segmenter) |
| Perl                                                                          | String scalar | Supported natively (With the "use feature 'unicode_strings" directive) | [Unicode::Util](https://metacpan.org/pod/Unicode::Util) |
| PHP                                                                           | Series of bytes | [mbstring (NEED TO CONFIRM LINK)](https://www.php.net/manual/en/book.mbstring.php) | [grapheme_\*](https://www.php.net/manual/en/ref.intl.grapheme.php) |
| Python 2                                                                      | Array of bytes | [unicode](https://pkg.go.dev/unicode) | \\X regular expression |
| Python 3                                                                      | Array of Unicode characters | Supported natively (With the "use feature 'unicode_strings" directive) | [grapheme](https://pypi.org/project/grapheme/) |



This directory contains several sub-directories, each dedicated to a particular programming language. The sample programs:
* read a line of text
* print the line of text
* print each character of the line of text
* print each grapheme in the line of text
* print the 7th character of the line of text
* print the 7th grapheme in the line of text.

Note that the grapheme logic is possible in only certain languages.

All examples use the [utf8.txt](utf8.txt) file in this parent directory for input data. Test with different data simply by adding to or updating this file.

## Other helpful notes
Libraries -- These are a potential source of pain that must also be investigated to ensure full utf8 support. For instance in an example application the full data flow of utf-8 was functioning correctly to and from the backend however a library was being used to allow the frontend to create a download of the utf-8 content and it was using a function in javascript that doesn't support the characters so they were being truncated in the file output. This wasn't caught for a while as it's a rarely traveled path in the application.
