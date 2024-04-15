This example requires the regex, unicodedata, anyascii, and grapheme libraries. 

* **regex**: used to split a Unicode string into graphemes.  This can also be done with the grapheme library.
* **unicodedata**: used to normalize a Unicode string four ways: NFC, NFD, NFKC, NFKD. 
* **anyascii**: used to produce an "approximate" ascii version of a specified Unicode string.
* **grapheme**: used to select the nth grapheme from a Unicode string.

The program reads Unicode strings from utf8.txt (in the parent directory)
 
To create a virtual environment to run the example:

```
python -m venv venvdir
.\venvdir\scripts\activate
python -m pip install -r requirements.txt
```
where requirements.txt contains the following lines:

```
regex
anyascii
grapheme
```

(assuming ```unicodedata``` is part of standard python)