# Sorting Unicode Text

The following table shows the result of sorting a set of Unicode character strings using a variety of methods. Many of the strings in the ORIGINAL column are simply pairs of Latin script (A-Z) characters. These are included to make clear where the sorting mechanisms put the non-Latin script Indigenous language characters that have been included.

|ORIGINAL|SORTED - DOS|SORTED - EXCEL|SORTED - POWERSHELL|SORTED - PYTHON3|SORTED - GITBASH|SORTED-pyUCA|
|---| --- | --- | --- | --- | --- | --- |
|AA|ĆL NFC|AA|AA|AA|AA|AA|
|AB|ə|AB|AB|AB|AB|AB|
|AZ|ʷ|AZ|AZ|AZ|AZ|AZ|
|CA|ŋ|CA|CA|CA|CA|CA|
|CB|AA|CB|CB|CB|CB|CB|
|CZ|AB|ĆL NFC|ĆL NFC|CZ|CZ|ĆL NFC|
|DA|AZ|ĆL NFD|ĆL NFD|ĆL NFD|ĆL NFD|ĆL NFD|
|EA|ĆL NFD|CZ|CZ|DA|DA|CZ|
|MA|CA|DA|DA|EA|EA|DA|
|NA|CB|ə|ə|MA|MA|EA|
|OA|CZ|EA|EA|NA|NA|ə|
|VA|DA|MA|MA|OA|OA|MA|
|WA|EA|NA|NA|VA|VA|NA|
|XA|MA|ŋ|ŋ|WA|WA|ŋ|
|ZA|NA|OA|OA|XA|XA|OA|
|ZB|OA|VA|VA|ZA|ZA|VA|
|ZZ|VA|ʷ|ʷ|ZB|ZB|ʷ|
|ĆL NFC|WA|WA|WA|ZZ|ZZ|WA|
|ĆL NFD|XA|XA|XA|ĆL NFC|ĆL NFC|XA|
|ə|ZA|ZA|ZA|ŋ|ŋ|ZA|
|ŋ|ZB|ZB|ZB|ə|ə|ZB|
|ʷ|ZZ|ZZ|ZZ|ʷ|ʷ|ZZ|

The `sort` command in DOS and gitbash, and the list.sort() method in python3 use a binary collation mechanism, sorting according to the numeric [code point](../../glossary.md#code-point) values of the characters. The code point for Ć, when normalized using the NFC normalization, comes after the code points for A-Z, so that's where python3 and gitbash place Ć.  Similarly, the Indigenous language characters are also placed after Z. For some reason, DOS places these characters before A. Note that the decomposed (NFD) form of Ć gets placed with the C's since the first character of the decomposed form is actually a C. 

On the other hand, Excel, Powershell, and python3 with the [pyUCA](https://pypi.org/project/pyuca/) library use the [Unicode Collation Algorithm](http://unicode.org/reports/tr10/), which does a reasonable job of sorting Unicode characters according to their general appearance. Note that there do appear to be some variations in where some characters are placed. For example, pyUCA places ə after the E's; Powershell and Excel place it before the E's.

## Sample Code

|File|Link|
|----|----|
|DOS| [sortstrings.bat](./sortstrings.bat)|
|Excel|[see Excel column in sorted.xlsx](./sorted.xlsx) |
|Powershell|[sortstrings.ps1](./sortstrings.ps1)|
|Python 3 default|[sortstrings_simple.py](./sortstrings_simple.py) |
|Gitbash|[sortstrings.bsh](./sortstrings.bsh)|
|Python 3 with UCA|[sortstrings_uca.py](sortstrings_uca.py)|


