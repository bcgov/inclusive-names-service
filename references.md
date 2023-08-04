# For Further Reading

The following resources may be useful to software development teams when constructing IN-Ready systems, and in testing those systems.

## **General**

[Official Unicode Website](https://home.unicode.org/)

This is the home page for the Unicode Consortium, a standards body concerned with the internationalization of software and services.

[fileformat.info](https://www.fileformat.info/info/unicode/)

This reference contains a complete list of Unicode code points and their corresponding encodings (UTF-8 and UTF-16).

[The Absolute Minimum Every Software Developer Absolutely, Positively Must Know About Unicode and Character Sets (No Excuses!)](http://www.joelonsoftware.com/articles/Unicode.html)

The author says: "In this article I'll fill you in on exactly what _every working programmer_ should know. All that stuff about "plain text = ascii = characters are 8 bits" is not only wrong, it's hopelessly wrong, and if you're still programming that way, you're not much better than a medical doctor who doesn't believe in germs. Please do not write another line of code until you finish reading this article."

[What Every Programmer Absolutely, Positively Needs To Know About Encodings And Character Sets To Work With Text](https://kunststube.net/encoding/)

"This article is about encodings and character sets. An article by Joel Spolsky entitled [The Absolute Minimum Every Software Developer Absolutely, Positively Must Know About Unicode and Character Sets (No Excuses!)](http://www.joelonsoftware.com/articles/Unicode.html) is a nice introduction to the topic and I greatly enjoy reading it every once in a while. I hesitate to refer people to it who have trouble understanding encoding problems though since, while entertaining, it is pretty light on actual technical details. I hope this article can shed some more light on what exactly an encoding is and just why all your text screws up when you least need it. This article is aimed at developers (with a focus on PHP), but any computer user should be able to benefit from it."

[What on Earth is Unicode Normalization?](https://towardsdatascience.com/what-on-earth-is-unicode-normalization-56c005c55ad0)

This article explains how some Unicode graphemes can be constructed from characters in more than one way.

[Critical Values for I18n Testing ("Does it hurt when I do this?")](http://www.i18nqa.com/iuc37-Texin-Critical%20values%20for%20i18n%20testing.pdf)

A Powerpoint presentation: "In this session, we recommend specific data values that are likely to identify internationalization problems in software intended for global markets."

[UTF-8 Encoding Debugging Chart](https://www.i18nqa.com/debug/utf8-debug.html)

An [Encoding Problem Chart](https://www.i18nqa.com/debug/utf8-debug.html#dbg) that aids in debugging common UTF-8 character encoding problems. See these 3 typical problem scenarios that the chart can help with.

- [Encoding Problem 1: Treating UTF-8 Bytes as Windows-1252 or ISO-8859-1](https://www.i18nqa.com/debug/bug-iso8859-1-vs-windows-1252.html)
- [Encoding Problem 2: Incorrect Double Mis-Conversion](https://www.i18nqa.com/debug/bug-double-conversion.html)
- [Encoding Problem 3: ISO-8859-1 vs Windows-1252](https://www.i18nqa.com/debug/bug-utf-8-latin1.html)

[UTF-8 and Unicode FAQ for Unix/Linux](https://www.cl.cam.ac.uk/~mgk25/unicode.html)

"This text is a very comprehensive one-stop information resource on how you can use Unicode/UTF-8 on POSIX systems (Linux, Unix). You will find here both introductory information for every user, as well as detailed references for the experienced developer."

In addition, it contains background information relevant to Windows systems, and web links to many useful resources. Although somewhat dated, it also contains extensive information that will be of interest to any C developer who needs to adapt their application to handle encoded Unicode characters .

[https://www.internalpointers.com/post/programming-unicode-gentle-introduction](https://www.internalpointers.com/post/programming-unicode-gentle-introduction)

[https://learn.microsoft.com/en-us/globalization/encoding/encoding-overview](https://learn.microsoft.com/en-us/globalization/encoding/encoding-overview)

[The Unicode Standard (version 15.0.0, September 2022)](https://www.unicode.org/versions/Unicode15.0.0/)

The most recent Unicode standard.

[Unicode Security Considerations](https://www.unicode.org/reports/tr36/)

"_Because Unicode contains such a large number of characters and incorporates the varied writing systems of the world, incorrect usage can expose programs or systems to possible security attacks. This is especially important as more and more products are internationalized. This document describes some of the security considerations that programmers, system analysts, standards developers, and users should take into account, and provides specific recommendations to reduce the risk of problems."_

[The Unicode](https://numa.hypotheses.org/2542)

A series of papers on the Unicode standard, covering

1. Character encoding and canonical equivalence
2. Code points and planes
3. Unicode Transformation Formats (e.g., UTF-8)
4. Unicode Character Database (UCD) and regular expressions

## **C and C++**

[Working with Strings](https://learn.microsoft.com/en-us/windows/win32/learnwin32/working-with-strings)

Microsoft documentation on C++ programming techniques for use when processing Unicode data.

[Unicode in C](https://linuxhint.com/unicode-c/)

This article explains how to modify a C program so that it can process Unicode data.

[Understanding text for C Programmers (UTF-8, Unicode, ASCII)](https://www.youtube.com/watch?v=70b9ineDgLU)

A YouTube video.

[Unicode in C and C++: What You Can Do About It Today](https://www.cprogramming.com/tutorial/unicode.html)

A "quick and highly pragmatic guide to digital text in the 21st century (for C programmers, of course)."

## **Encryption and Decryption**

[Cryptography with International Character Sets](https://www.di-mgt.com.au/cryptoInternational2.html)

A great introduction to cryptography, common issues faced when encrypting/decrypting Unicode text, and trouble-shooting.

## **Excel**

[Excel save behaviour of CSV file with UTF8 encoding vs UTF8-Bom encoding](https://superuser.com/questions/1204233/excel-save-behaviour-of-csv-file-with-utf8-encoding-vs-utf8-bom-encoding)

This article explains that Excel expects a byte order mark (BOM) at the start of Unicode data in a CSV file.

[Creating International CSV files with python](https://chase-seibert.github.io/blog/2014/07/30/international-csv-files-python.html)

This article explains how to create comma separated value (CSV) files, containing Unicode characters, that can be read by Excel and other Windows applications.

## **Java**

[https://www.nexsoftsys.com/articles/unicode-help-java-programmers.html](https://www.nexsoftsys.com/articles/unicode-help-java-programmers.html)

## **JavaScript**

[What Every JavaScript Developer Should Know about Unicode](https://dmitripavlutin.com/what-every-javascript-developer-should-know-about-unicode/)

Introduction to Unicode, from the perspective of a JavaScript programmer.

[JavaScript / ECMAScript Internationalization (I18n)](http://www.jsi18n.com/)

"This site is devoted to topics related to software internationalization using JavaScript (aka ECMAScript) programming language. The site was created by Craig Cummings and Tex Texin and stemmed from interest in their presentations on comparing JavaScript libraries at the _Internationalization and Unicode Conferences_ IUC37, IUC38, and IUC39."

## **Oracle**

[Database Globalization Support Guide - Choosing a Character Set](https://docs.oracle.com/en/database/oracle/oracle-database/19/nlspg/choosing-character-set.html#GUID-BF26E01D-AB92-48FC-855A-69A5B3AF9A92)

This chapter of the Oracle Database Globalization Support Guide explains how to choose a character set for your Oracle database.

[Why the Database Character Set Matters](https://blogs.oracle.com/timesten/post/why-databasecharacterset-matters)

Clear and simple explanation of why to choose AL32UTF8 as the Oracle character set for your Oracle database.

## **Perl**

[Unicode grapheme-level versions of core Perl functions](https://metacpan.org/pod/Unicode::Util)

"This module provides versions of core Perl string functions tailored to work on Unicode grapheme clusters, which are what users perceive as characters, as opposed to code points, which are what Perl considers characters."

# [Treat Unicode strings as grapheme clusters](https://www.effectiveperlprogramming.com/2011/06/treat-unicode-strings-as-grapheme-clusters/)

[Perl Unicode introduction](https://perldoc.perl.org/perluniintro)

"This document gives a general idea of Unicode and how to use Unicode in Perl."

[Perl Unicode Tutorial](https://perldoc.perl.org/perlunitut)

"There's a lot to know about character sets, and text encodings. It's probably best to spend a full day learning all this, but the basics can be learned in minutes."

[Perl Unicode FAQ](https://perldoc.perl.org/perlunifaq)

"This is a list of questions and answers about Unicode in Perl, intended to be read after [Perl Unicode Tutorial](https://perldoc.perl.org/perlunitut)"

[https://perldoc.perl.org/perlunicode](https://perldoc.perl.org/perlunicode)

A comprehensive presentation of Unicode handling in Perl.

## **PHP**

[https://www.php.net/manual/en/book.mbstring.php](https://www.php.net/manual/en/book.mbstring.php)

PHP provides support for Unicode [BMP](#_Basic_Multilingual_Plane) characters through the mbstring module.

## **PostgreSQL**

[Character Set Support](https://www.postgresql.org/docs/current/multibyte.html)

Explains how to set the character set and encoding for a PostgreSQL server cluster or an individual database.

## **Python**

[Unicode in Python 2](https://uwpce-pythoncert.github.io/SystemDevelopment/unicode.html)

"A quick description of Unicode, its use in Python 2, and some of the gotchas that arise."

[Python 2.7 Unicode "How To"](https://docs.python.org/2.7/howto/unicode.html)

"This HOWTO discusses Python 2.x's support for Unicode, and explains various problems that people commonly encounter when trying to work with Unicode."

[Python 3.x Unicode "How To"](https://docs.python.org/3/howto/unicode.html)

"This HOWTO discusses Python's support for the Unicode specification for representing textual data, and explains various problems that people commonly encounter when trying to work with Unicode."

[Python and Unicode](https://downloads.egenix.com/python/Unicode-EPC2002-Talk.pdf)

"Unicode Support in Python" – Powerpoint presentation for EuroPython Conference 2002., Charleroi, Belgium

## **SQL Server**

[Collation and Unicode Support](https://learn.microsoft.com/en-us/sql/relational-databases/collations/collation-and-unicode-support?view=sql-server-ver16)

This article describes how to configure SQL Server to support various collations, including Unicode.

