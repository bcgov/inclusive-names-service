## Database Character Set and Encoding

In MySQL, the character set for the installation is defined in the initialization file ('my.cnf' or 'my.ini'). If nothing is specified there, then the default character set in MySQL version 8.0 is "utf8mb4", which uses the UTF-8 encoding, storing characters in binary using 1 to 4 bytes. utf8mb4 supports characters in the [Basic Multilingual Plane (BMP)](https://dev.mysql.com/doc/mysql-g11n-excerpt/5.7/en/charset-unicode.html) and supplementary planes.  The character set can be overridden for individual databases, tables, columns and literals, with the value specified at a higher level (e.g., database) becoming the default when creating objects at the lower levels (e.g., table). As an example, the following SQL creates a table where ``utf8mb4`` is the encoding used for all of character data columns except for ``string_column``, for which the encoding is specified as ``ascii``. 
```
CREATE TABLE world.new_table (
  int_column INT NOT NULL,
  string_column VARCHAR(40) CHARACTER SET ascii,
  PRIMARY KEY (`int_column`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = binary;
```

**To support the storage of Indigenous language characters, the character set encoding used must be utf8mb4**

### What are the collation rules used in the database?

In MySQL, default collation rules are defined in the initialization file and, like the character set, and can be overridden for a particular database, table, column, or character expression. The database collation can be further overridden for individual columns (of tables) or SQL expressions. See [https://dev.mysql.com/doc/refman/8.0/en/charset.html](https://dev.mysql.com/doc/refman/8.0/en/charset.html). 

### How can I tell what the default character set encoding and collation are for my MySQL database?

Use this SQL to determine the default character set encoding and collation used by your database.

```
SELECT DEFAULT_CHARACTER_SET_NAME, DEFAULT_COLLATION_NAME
FROM INFORMATION_SCHEMA.SCHEMATA 
WHERE SCHEMA_NAME = '<db_name>';
```

The default character set and collation for a table can be determined by

```
SELECT TABLE_COLLATION
FROM INFORMATION_SCHEMA.TABLES 
WHERE TABLE_SCHEMA = '<database name>' AND TABLE_NAME = '<table name>'
```

The default character set and collation for a column can be determined by

```
SELECT CHARACTER_SET_NAME, COLLATION_NAME
FROM INFORMATION_SCHEMA.COLUMNS 
WHERE SCHEMA_NAME = '<db_name>' AND TABLE_NAME = '<table name>' AND COLUMN_NAME = '<column name>';
```
**To support the correct processing of Indigenous language characters, the collation used must be utf8mb4_bin**


### What happens when I try to store Unicode characters in a non-Unicode-encoded table?

As an example, when the following INSERT statement is attempted on a MySQL table that is encoded as ASCII rather than UTF8, the error below is raised.

```
CREATE TABLE world.testtable (
  testcol VARCHAR(100) NULL)
DEFAULT CHARACTER SET = ascii;

INSERT INTO testtable VALUES ('Secwe̓pemc');
```

**Error Code: 1366. Incorrect string value: '\xCC\x93pemc' for column 'testcol' at row 1**


The Unicode code point U+0313 [represents](https://unicode-table.com/en/0313/) the diacritical above the letter 'e'. This code point is not defined in the ASCII character set used by the MySQL table referenced above. The UTF-8 encoding of the e̓ character is 0xCC 0x93.

