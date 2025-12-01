# Representing Unicode Text Using ASCII

Some systems support only [ASCII](../../glossary.md#ascii) and not Unicode. For these it is sometimes helpful to be able to create a simplified (ASCII only) version of the Unicode string in a consistent manner. The [anyASCII](https://anyascii.com) algorithm provides a mechanism for doing this. This [geeksforgeeks](https://www.geeksforgeeks.org/convert-unicode-to-ascii-in-python/) article provides some good information.

## Program Example of using AnyASCII

The Python 3 program [utf8.py](../../programming_languages/python3/utf8.py) uses the [anyascii](https://pypi.org/project/anyascii/) library to determine the AnyASCII version of Unicode strings.

Similar libraries are available in other programming languages.
