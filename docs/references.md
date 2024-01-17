# For Further Reading ...

The following resources may be useful to software development teams when constructing Indigenous-Names-Ready systems, and in testing those systems. Click one of the following links to go straight to a list of references for that section.

[General](https://github.com/bcgov/inclusive-names-service/blob/main/references.md#general) <br>
[C and C++](https://github.com/bcgov/inclusive-names-service/blob/main/references.md#c-and-c) <br>
[Encryption and Decryption](https://github.com/bcgov/inclusive-names-service/blob/main/references.md#encryption-and-decryption) <br>
[Excel](https://github.com/bcgov/inclusive-names-service/blob/main/references.md#excel) <br>
[Java](https://github.com/bcgov/inclusive-names-service/blob/main/references.md#java) <br>
[JavaScript](https://github.com/bcgov/inclusive-names-service/blob/main/references.md#javascript) <br>
[MySQL](https://github.com/bcgov/inclusive-names-service/blob/main/references.md#mysql) <br>
[Normalization](https://github.com/bcgov/inclusive-names-service/blob/main/references.md#normalization) <br>
[Oracle](https://github.com/bcgov/inclusive-names-service/blob/main/references.md#oracle) <br>
[Perl](https://github.com/bcgov/inclusive-names-service/blob/main/references.md#perl) <br>
[PHP](https://github.com/bcgov/inclusive-names-service/blob/main/references.md#php) <br>
[PostgreSQL](https://github.com/bcgov/inclusive-names-service/blob/main/references.md#postgresql) <br>
[Python](https://github.com/bcgov/inclusive-names-service/blob/main/references.md#python) <br>
[Security](https://github.com/bcgov/inclusive-names-service/blob/main/references.md#security) <br>
[SQL Server](https://github.com/bcgov/inclusive-names-service/blob/main/references.md#sql-server) <br>

## **General**

[Official Unicode Website](https://home.unicode.org/)

This is the home page for the Unicode Consortium, a standards body concerned with the internationalization of software and services.

[Frequently Asked Questions](http://www.unicode.org/faq/)

_"The Unicode Frequently Asked Questions (FAQ) are organized into different topic pages. Many FAQ pages contain links to other pages where you will find further information about specific topics. Check in particular the [Basic Questions](http://www.unicode.org/faq/basic_q.html) and [Specifications](http://www.unicode.org/faq/specifications.html) pages. As another option, you may find it easier to go to the [search page](https://www.unicode.org/search) and type in your topic plus "FAQ" to locate appropriate FAQ entries. For example "NFC FAQ", "BOM FAQ", "Tamil FAQ", and so forth. If you have a question not addressed by the FAQ entries, you may join the public [Unicode email list](https://www.unicode.org/consortium/distlist.html) and post your question there."_   

[fileformat.info](https://www.fileformat.info/info/unicode/)

This reference contains a complete list of Unicode code points and their corresponding encodings (UTF-8 and UTF-16).

[The Absolute Minimum Every Software Developer Absolutely, Positively Must Know About Unicode and Character Sets (No Excuses!)](http://www.joelonsoftware.com/articles/Unicode.html)

The author says: "In this article I'll fill you in on exactly what _every working programmer_ should know. All that stuff about "plain text = ascii = characters are 8 bits" is not only wrong, it's hopelessly wrong, and if you're still programming that way, you're not much better than a medical doctor who doesn't believe in germs. Please do not write another line of code until you finish reading this article."

[What Every Programmer Absolutely, Positively Needs To Know About Encodings And Character Sets To Work With Text](https://kunststube.net/encoding/)

"This article is about encodings and character sets. An article by Joel Spolsky entitled [The Absolute Minimum Every Software Developer Absolutely, Positively Must Know About Unicode and Character Sets (No Excuses!)](http://www.joelonsoftware.com/articles/Unicode.html) is a nice introduction to the topic and I greatly enjoy reading it every once in a while. I hesitate to refer people to it who have trouble understanding encoding problems though since, while entertaining, it is pretty light on actual technical details. I hope this article can shed some more light on what exactly an encoding is and just why all your text screws up when you least need it. This article is aimed at developers (with a focus on PHP), but any computer user should be able to benefit from it."


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


[The Unicode](https://numa.hypotheses.org/2542)

A series of papers on the Unicode standard, covering

1. Character encoding and canonical equivalence
2. Code points and planes
3. Unicode Transformation Formats (e.g., UTF-8)
4. Unicode Character Database (UCD) and regular expressions

[Character Model for the World Wide Web 1.0: Fundamentals](https://www.w3.org/TR/charmod/)

This Architectural Specification provides authors of specifications, software developers, and content developers with a common reference for interoperable text manipulation on the World Wide Web, building on the Universal Character Set, defined jointly by the Unicode Standard and ISO/IEC 10646. Topics addressed include use of the terms 'character', 'encoding' and 'string', a reference processing model, choice and identification of character encodings, character escaping, and string indexing.

[Character Model for the World Wide Web: String Matching](https://www.w3.org/TR/charmod-norm/)

This document builds upon [Character Model for the World Wide Web 1.0: Fundamentals](https://www.w3.org/TR/charmod/) to provide authors of specifications, software developers, and content developers a common reference on string identity matching on the World Wide Web and thereby increase interoperability.

[UTF-8 Everywhere Manifesto](https://utf8everywhere.org/)

_Our goal is to promote usage and support of the UTF-8 encoding and to convince that it should be the default choice of encoding for storing text strings in memory or on disk, for communication and all other uses. We believe that our approach improves performance, reduces complexity of software and helps prevent many Unicode-related bugs. We suggest that other encodings of Unicode (or text, in general) belong to rare edge-cases of optimization and should be avoided by mainstream users._

[Indigenous languages and technology](https://www.un.org/esa/socdev/unpfii/documents/2016/egm/Indigenous_languages_and_techology_Craig%20Cornelius_FINAL.pdf)

This presentation from 2016 illustrates the considerations in supporting Indigenous languages.

[Supporting Indigenous Names & Alphabets With Technology](https://www.youtube.com/watch?v=5FV9vcWZru4)

This video, produced by the [First Peoples' Cultural Council](https://fpcc.ca/resource/technology/), provides an excellent overview of the issues involved in supporting B.C. Indigenous languages in systems.

## **C and C++**

[ICU - International Components for Unicode](https://icu.unicode.org/)

ICU is a mature, widely used set of C/C++ and Java libraries providing Unicode and Globalization support for software applications. ICU is widely portable and gives applications the same results on all platforms and between C/C++ and Java software. ICU is released under a nonrestrictive open source license that is suitable for use with both commercial software and with other open source or free software.

Here are a few highlights of the services provided by ICU:

Code Page Conversion: Convert text data to or from Unicode and nearly any other character set or encoding. ICU's conversion tables are based on charset data collected by IBM over the course of many decades, and is the most complete available anywhere.

Collation: Compare strings according to the conventions and standards of a particular language, region or country. ICU's collation is based on the Unicode Collation Algorithm plus locale-specific comparison rules from the Common Locale Data Repository, a comprehensive source for this type of data.

Formatting: Format numbers, dates, times and currency amounts according the conventions of a chosen locale. This includes translating month and day names into the selected language, choosing appropriate abbreviations, ordering fields correctly, etc. This data also comes from the Common Locale Data Repository.

Time Calculations: Multiple types of calendars are provided beyond the traditional Gregorian calendar. A thorough set of timezone calculation APIs are provided.

Unicode Support: ICU closely tracks the Unicode standard, providing easy access to all of the many Unicode character properties, Unicode Normalization, Case Folding and other fundamental operations as specified by the Unicode Standard.

Regular Expression: ICU's regular expressions fully support Unicode while providing very competitive performance.

Bidi: support for handling text containing a mixture of left to right (English) and right to left (Arabic or Hebrew) data.

Text Boundaries: Locate the positions of words, sentences, paragraphs within a range of text, or identify locations that would be suitable for line wrapping when displaying the text.

And much more. Refer to the [ICU User Guide](https://unicode-org.github.io/icu/userguide/) for details.

Why ICU4C?
The C and C++ languages and many operating system environments do not provide full support for Unicode and standards-compliant text handling services. Even though some platforms do provide good Unicode text handling services, portable application code can not make use of them. The ICU4C libraries fills in this gap. ICU4C provides an open, flexible, portable foundation for applications to use for their software globalization requirements. ICU4C closely tracks industry standards, including Unicode and CLDR (Common Locale Data Repository).

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

[ICU - International Components for Unicode](https://icu.unicode.org/)

ICU is a mature, widely used set of C/C++ and Java libraries providing Unicode and Globalization support for software applications. ICU is widely portable and gives applications the same results on all platforms and between C/C++ and Java software. ICU is released under a nonrestrictive open source license that is suitable for use with both commercial software and with other open source or free software.

Here are a few highlights of the services provided by ICU:

Code Page Conversion: Convert text data to or from Unicode and nearly any other character set or encoding. ICU's conversion tables are based on charset data collected by IBM over the course of many decades, and is the most complete available anywhere.

Collation: Compare strings according to the conventions and standards of a particular language, region or country. ICU's collation is based on the Unicode Collation Algorithm plus locale-specific comparison rules from the Common Locale Data Repository, a comprehensive source for this type of data.

Formatting: Format numbers, dates, times and currency amounts according the conventions of a chosen locale. This includes translating month and day names into the selected language, choosing appropriate abbreviations, ordering fields correctly, etc. This data also comes from the Common Locale Data Repository.

Time Calculations: Multiple types of calendars are provided beyond the traditional Gregorian calendar. A thorough set of timezone calculation APIs are provided.

Unicode Support: ICU closely tracks the Unicode standard, providing easy access to all of the many Unicode character properties, Unicode Normalization, Case Folding and other fundamental operations as specified by the Unicode Standard.

Regular Expression: ICU's regular expressions fully support Unicode while providing very competitive performance.

Bidi: support for handling text containing a mixture of left to right (English) and right to left (Arabic or Hebrew) data.

Text Boundaries: Locate the positions of words, sentences, paragraphs within a range of text, or identify locations that would be suitable for line wrapping when displaying the text.

And much more. Refer to the [ICU User Guide](https://unicode-org.github.io/icu/userguide/) for details.

See [Why Use ICU4J](https://icu.unicode.org/home/why-use-icu4j)


## **JavaScript**

[What Every JavaScript Developer Should Know about Unicode](https://dmitripavlutin.com/what-every-javascript-developer-should-know-about-unicode/)

Introduction to Unicode, from the perspective of a JavaScript programmer.

[JavaScript / ECMAScript Internationalization (I18n)](http://www.jsi18n.com/)

"_This site is devoted to topics related to software internationalization using JavaScript (aka ECMAScript) programming language. The site was created by Craig Cummings and Tex Texin and stemmed from interest in their presentations on comparing JavaScript libraries at the _Internationalization and Unicode Conferences_ IUC37, IUC38, and IUC39._"

[Unicode – a brief introduction (advanced)](https://exploringjs.com/impatient-js/ch_unicode.html) from JavaScript for impatient programmers (ES2022 edition)

## **MySQL**

[Chapter 10 Character Sets, Collations, Unicode](https://dev.mysql.com/doc/refman/8.0/en/charset.html)

"_MySQL includes character set support that enables you to store data using a variety of character sets and perform comparisons according to a variety of collations. The default MySQL server character set and collation are utf8mb4 and utf8mb4_0900_ai_ci, but you can specify character sets at the server, database, table, column, and string literal levels._"
## **Normalization**

[What on Earth is Unicode Normalization?](https://towardsdatascience.com/what-on-earth-is-unicode-normalization-56c005c55ad0)

This article explains how some Unicode graphemes can be constructed from characters in more than one way.

## **Oracle**

[Database Globalization Support Guide - Choosing a Character Set](https://docs.oracle.com/en/database/oracle/oracle-database/19/nlspg/choosing-character-set.html#GUID-BF26E01D-AB92-48FC-855A-69A5B3AF9A92)

This chapter of the Oracle Database Globalization Support Guide explains how to choose a character set for your Oracle database.

[Why the Database Character Set Matters](https://blogs.oracle.com/timesten/post/why-databasecharacterset-matters)

Clear and simple explanation of why to choose AL32UTF8 as the Oracle character set for your Oracle database.

## **Perl**

[Unicode grapheme-level versions of core Perl functions](https://metacpan.org/pod/Unicode::Util)

"This module provides versions of core Perl string functions tailored to work on Unicode grapheme clusters, which are what users perceive as characters, as opposed to code points, which are what Perl considers characters."

[Treat Unicode strings as grapheme clusters](https://www.effectiveperlprogramming.com/2011/06/treat-unicode-strings-as-grapheme-clusters/)

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

## **Security**

[Unicode Security Considerations](https://www.unicode.org/reports/tr36/)

"_Because Unicode contains such a large number of characters and incorporates the varied writing systems of the world, incorrect usage can expose programs or systems to possible security attacks. This is especially important as more and more products are internationalized. This document describes some of the security considerations that programmers, system analysts, standards developers, and users should take into account, and provides specific recommendations to reduce the risk of problems."_

[Unicode Security Mechanisms](https://www.unicode.org/reports/tr39/)

"_Because Unicode contains such a large number of characters and incorporates the varied writing systems of the world, incorrect usage can expose programs or systems to possible security attacks. This document specifies mechanisms that can be used to detect possible security problems._"

[Unicode for Security Professionals](https://www.gosecure.net/blog/2020/08/04/unicode-for-security-professionals/)

"_Unicode is the de-facto standard for multilingual character encoding. UTF-8 is the most popular encoding used that supports its hundreds of thousands of characters. Aside from the encoding (byte representation of characters), Unicode defines multiple transformations that can be applied to characters. For instance, it describes the behavior of transformations such as Uppercase. The character known as Long S “ſ” (U+017F) will become a regular uppercase S “S” (U+0053). Unexpected behavior for developers can often lead to security issues. Today, we will dive into the case mapping and normalization transformations. You will see how they can contribute to logic flaws in code._"

"_Along with this article, we are sharing a list of API to look for in source code audit. We are also publishing an [interactive cheat sheet](https://gosecure.github.io/unicode-pentester-cheatsheet/) for character testing._"

[Unicode Security Guide](https://websec.github.io/unicode-security-guide/)

"_This guide has been designed to give Web application developers, software engineers, and application security researchers a reference for understanding Unicode-related security issues in operating systems, applications, and the Web._

_The dynamics of Unicode, and character encodings in general, are often misunderstood or poorly implemented, and lead to an array of interesting if not catastrophic security vulnerabilities._

_The content here has been sourced through testing, research, and the following two technical reports from the Unicode Consortium:_

[What are best practices for handling user Unicode in a web application?](https://security.stackexchange.com/questions/257017/what-are-best-practices-for-handling-user-unicode-in-a-web-application) 

The author writes _I've done a base level of research on the topic and have come up with the following list of recommended base practices. This isn't meant to be comprehensive; there are many, many more listed in the resources above. As always, what you need to do depends on your risk profile. For my purposes, these practices seem to fit the bill._

[Technical Report #36 : Unicode Security Considerations](http://www.unicode.org/reports/tr36/) <br>
[Technical Report #39 : Unicode Security Mechanisms](http://www.unicode.org/reports/tr39/)

_Beyond these two sources, further research has been ongoing around identifying and inventorying software behaviors. Test cases are being provided in the [source code repository](https://github.com/websec/unicode-security-guide)._"



## **SQL Server**

[Collation and Unicode Support](https://learn.microsoft.com/en-us/sql/relational-databases/collations/collation-and-unicode-support?view=sql-server-ver16)

This article describes how to configure SQL Server to support various collations, including Unicode.

