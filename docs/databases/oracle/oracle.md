## Database Character Set and Encoding

In Oracle databases, the character set is defined in the CREATE DATABASE statement, specifically in the CHARACTER SET and NATIONAL CHARACTER SET parameters. The CHARACTER SET value applies to the CHAR, VARCHAR2, and CLOB columns, while the NATIONAL CHARACTER SET applies to NCHAR, NVARCHAR2, and NCLOB columns. See the Oracle [Database Globalization Support Guide](https://docs.oracle.com/en/database/oracle/oracle-database/21/nlspg/choosing-character-set.html#GUID-BF26E01D-AB92-48FC-855A-69A5B3AF9A92) for more information.

**To support the storage of Unicode characters,**  **CHARACTER SET**  **must be set to**  **AL32UTF8,**  **and**  **NATIONAL CHARACTER SET**  **must be set to**  **AL16UTF16**.

These character sets are consistent with Unicode version 12.1.

### How can I tell what the encoding is for my Oracle database?

Use this SQL to determine the character set used by your database.

```
SELECT * FROM NLS_DATABASE_PARAMETERS 
WHERE PARAMETER LIKE 'NLS_%CHARACTERSET';
```

The value of parameter NLS_CHARACTERSET is the character set used for CHAR, VARCHAR2, and CLOB columns. The value of parameter NLS_NCHAR_CHARACTERSET is the character set used for NCHAR, NVARCHAR2, and NCLOB columns.


### What are the collation rules used in the database?

In Oracle, up to version 12.1, the collation parameters are defined at the database level. With version 12.2 and beyond, collation rules can be defined for individual columns.

#### Version 12.1:

```
SELECT PARAMETER,VALUE FROM NLS_DATABASE_PARAMETERS 
WHERE PARAMETER IN ('NLS_COMP', 'NLS_SORT'); 
```
NLS_COMP and NLS_SORT hold the collation rules for comparing character values and sorting character values, respectively.

#### Version 12.2:

```
SELECT table_name,column_id,column_name,collation
FROM user_tab_columns
WHERE table_name = 'YOUR_TABLE'
ORDER BY column_id;
```

As described in the parent [README.md](../README.md), for databases containing a mix of ASCII and Indigenous Language Unicode characters, the most appropriate collation rule to use is BINARY.

### Comparing UTF-8 (VARCHAR2) with UTF-16 (NVARCHAR2) text strings
The following code snippet illustrates comparing two text strings, both having the same characters, but one encoded in UTF-8 and the other in UTF-16. Viewed as characters the two strings are identical, even though their internal representations are different. The Oracle '=' test judges them as equal, which is good!

```
create table testutf(utf8 varchar2(100), utf16 nvarchar2(100)); -- varchar2 uses a utf-8 encoding; nvarchar2 uses a utf-16 encoding
insert into testutf values('Tk̓emlúps te Secwépemc','Tk̓emlúps te Secwépemc');
select length(utf8),length(utf16) from testutf; -- 22 characters each. Note though that there are just 21 graphemes
select length('k̓') from dual; -- this grapheme is 2 characters
select lengthb(utf8),lengthb(utf16) from testutf;  -- utf8 = 25 bytes, utf16 = 44 bytes
select * from testutf where utf8 = utf16; -- the two strings are judged equal, even though internally (bytes) they are different.
```