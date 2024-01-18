## Database Character Set and Encoding

In a SQL Server database, the encoding and collation rules can be defined at four levels:

1. Server
2. Database
3. Table
4. Column

Any rules for items with a narrower scope (e.g., column) override the rules defined at the broader scope (e.g., server). As described in [Collation and Unicode Support](https://learn.microsoft.com/en-us/sql/relational-databases/collations/collation-and-unicode-support?view=sql-server-ver16), a collation rule is represented by a combination of suffixes defining case-, accent-, width-, or kana-sensitivity, with the last suffix indicating if the encoding is UTF-8.

**To support the storage of Unicode characters, the collation/encoding rule used for a column must end in _ UTF8.**

### How can I tell what the encoding is for my SQL Server database?

Use this SQL to determine the character set used by your database.

```
SELECT t.name AS 'table', c.name AS 'column', c.collation_name
FROM sys.columns c, sys.tables t
WHERE c.name = '<column name>' AND t.name = '<table name>'
AND t.object_id = c.object_id;
```

### What are the collation rules used in the database?

In a SQL Server database, the collation and encoding are defined together, as described above.

### How do I create a new database with a Unicode encoding?

When creating a database, specify an encoding with a name ending in _UTF8, e.g., LATIN1_GENERAL_100_BIN2_UTF8.

### What happens when I try to store Unicode characters in a non-Unicode-encoded database?

As an example, when the following INSERT statement is attempted to a table in a SQL Server database that is encoded as SQL_Latin1_General_CP1_CI_AS (not UTF8)

```
INSERT INTO testtable VALUES ('Secwe̓pemc');
SELECT * FROM testtable;
```

the following result is returned:

`
Secwe?pemc
`


The Unicode code point U+0313 [represents](https://unicode-table.com/en/0313/) the diacritical above the letter 'e'. This code point is not defined in the SQL_Latin1_General_CP1_CI_AS collation/character set used by this SQL Server database.

The following snippet shows what happens when you insert Unicode data into a column that does not use a Unicode encoding:

CREATE TABLE TESTTAB(TESTCOL VARCHAR(100));SELECT t.name AS 'table', c.name AS 'column', c.collation\_name

FROM sys.columns c, sys.tables t

WHERE c.name = 'TESTCOL' AND t.name = 'TESTTAB'

AND t.object\_id = c.object\_id; -- answer is

-- 'SQL\_Latin1\_General\_CP1\_CI\_AS'

INSERT INTO TESTTAB VALUES(N'Secwe̓pemc'); -- The N prefix indicates that the following string is Unicode. It is necessary to include this when referring to Unicode literal strings in SQL Server.

SELECT \* FROM TESTTAB; -- answer is Secwe?pemc

As shown by this snippet, the e̓ is not stored correctly. However, if we specify a UTF-8 collation then the result is correct:

CREATE TABLE TESTTAB(TESTCOL VARCHAR(100)

collate Latin1\_General\_100\_BIN2\_UTF8 );

SELECT t.name AS 'table', c.name AS 'column', c.collation\_name

FROM sys.columns c, sys.tables t

WHERE c.name = 'TESTCOL' AND t.name = 'TESTTAB'

AND t.object\_id = c.object\_id; -- answer is

-- 'Latin1\_General\_100\_BIN2\_UTF8'

INSERT INTO TESTTAB VALUES(N'Secwe̓pemc');

SELECT \* FROM TESTTAB; -- answer is Secwe̓pemc
