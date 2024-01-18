# Unicode Support in Various Programming Languages

The following table summarizes the support that several popular programming languages provide for their native strings, Unicode strings, and strings of graphemes:

### String, Unicode Character, and Grapheme Support in Popular Computer Programming Languages
| Language                                                                      | Native string type | Unicode character library | Unicode grapheme library |
|---|---|---|---
| [C](c/README.md)                                                                             | array of char | [wchar.h](https://pubs.opengroup.org/onlinepubs/007908799/xsh/wchar.h.html) | [utf8proc](https://juliastrings.github.io/utf8proc/) |
| [C++](c++/README.md)                                                                           | array of char | [wchar.h](https://pubs.opengroup.org/onlinepubs/007908799/xsh/wchar.h.html) | [utf8proc](https://juliastrings.github.io/utf8proc/) |
| C#                                                                          | String (Stored internally as an array of UTF-16 Unicode characters) | Supported natively | [GraphemeSplitter (There are several alternatives)](https://github.com/ufcpp/GraphemeSplitter) |
| [Go](go/README.md)                                                                            | [“slice” of bytes](https://blog.golang.org/slices) | [unicode](https://pkg.go.dev/unicode) | [uax29](https://github.com/clipperhouse/uax29/) |
| [Java](java/README.md)                                                                         | String (Stored internally as an array of UTF-16 Unicode characters) | Supported natively | grapheme-splitter-lite (See also ICU4J documentation) |
| [Javascript](javascript/README.md)                                                                    | String (Stored internally as an array of UTF-16 Unicode characters) | Supported natively | [Intl.Segmenter](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Segmenter) |
| [Perl](perl/README.md)                                                                          | String scalar | Supported natively (With the "use feature 'unicode_strings" directive) | [Unicode::Util](https://metacpan.org/pod/Unicode::Util) |
| [PHP](php/README.md)                                                                           | Series of bytes | [mbstring (NEED TO CONFIRM LINK)](https://www.php.net/manual/en/book.mbstring.php) | [grapheme_\*](https://www.php.net/manual/en/ref.intl.grapheme.php) |
| [Python 2](python2/README.md)                                                                      | Array of bytes | [unicode](https://pkg.go.dev/unicode) | \\X regular expression |
| [Python 3](python3/README.md)                                                                      | Array of Unicode characters | Supported natively (With the "use feature 'unicode_strings" directive) | [grapheme](https://pypi.org/project/grapheme/) |

The links in the left column point to pages that deal with the specific programming languages. For each programming language, there is a sample program, that:

* reads a line of text
* prints the line of text
* prints each character of the line of text
* prints each grapheme in the line of text
* prints the 7th character of the line of text
* prints the 7th grapheme in the line of text.

All examples use the [utf8.txt](https://github.com/bcgov/inclusive-names-service/blob/main/docs/programming_languages/utf8.txt) file for input data. Test with different data simply by adding to or updating this file.

## Other helpful notes
### Libraries 
It is important to keep in mind that some libraries do not provide full Unicode support, and use without proper testing may lead to problems. For instance, in an example application the full data flow of utf-8 was functioning correctly to and from the backend however a library was being used to allow the frontend to create a download of the utf-8 content and it was using a function in javascript that doesn't support the characters so they were being truncated in the file output. This wasn't caught for a while as it was a rarely traveled path in the application.

Consider using the Unicode International Components for Unicode (ICU) [ICU4C](https://unicode-org.github.io/icu/userguide/icu4c/) and [ICU4J](https://unicode-org.github.io/icu/userguide/icu4j/) libraries where possible. The [ICU User Guide](https://unicode-org.github.io/icu/userguide/) is a good starting point.
