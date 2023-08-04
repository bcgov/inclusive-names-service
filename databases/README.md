### Database Character Set and Encoding

#### How are database character sets and encodings defined?

When building a database, the database administrator must specify the [character set](../glossary.md#character_set)/[encoding](../glossary.md#encoding) combination to use when storing data. How this encoding is defined differs according to the database management system product in use.

Collation rules determine the character string comparison and sorting rules, for example whether comparisons are case insensitive, whether presence or absence of accents on characters determines matching, etc. There are many language-specific collations (e.g., French and English may have different sorting rules, as described in the [Oracle Database Globalization and Support Guide](https://docs.oracle.com/en/database/oracle/oracle-database/21/nlspg/linguistic-sorting-and-matching.html#GUID-6175C023-2157-4EEF-ABAE-B47C4E307434), for example). For databases that support Unicode, collations that follow the [Unicode Collation Algorithm (UCA) standard](https://unicode.org/reports/tr10/) should be used. While there are many ways to configure UCA, the most general approach is to use binary comparisons and sorting (i.e., characters are matched/sorted according to their corresponding binary encodings. This approach should be taken for databases that include Unicode characters. as there are no other well-defined rules like there are for English, French, and other more restricted languages. The following sections provide SQL snippets for determining the sorting and matching collations used for character data in various database management systems.

How encodings and collation rules are defined differs according to the database management system product in use:

* [Oracle](./oracle/oracle.md) 
* [PostgreSQL](./postgresql/postgresql.md) 
* [SQL Server](./sqlserver/sqlserver.md)
* [MySQL](./mysql/mysql.md)
