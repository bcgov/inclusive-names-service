Graphemes are totally doable in C but the exercise is left in charge of the reader as I could not find a library to implement it quickly but as variables are just bytes you can easily implement something that follows the specification.

The library that looked the best was ICU
https://icu.unicode.org/

Compiled with gcc `gcc utf8.c`

GOTCHAS:
- If you straight print to terminal it will often look like the handling is smarter than it is because the terminal will turn the undisplayable chachters into their graphame correctly.
-  if you use a char/char*/char[] instead of wchar/wchar*/wchar[] respectively it won't have the right space as soon as you leave ASCII territory
- If you were going to write your own parser of unicode consider first that a valid utf8 character can come in any size as it's completely valid to add any number of combining marks with other characters and create an arbitrarily large character
- Even when using the right variables it's important to SET_LOCALE but that is technically leaving it a little to the whims of the OS
- Remember that a solution is always possible as you always have access to the bytes