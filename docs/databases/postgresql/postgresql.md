## Database Character Set and Encoding

In PostgreSQL databases, the character set for the server cluster is defined with the -E parameter to the initdb command, and can be overridden for a single database when creating the database. The encoding value applies to the CHAR, VARCHAR, and TEXT columns. See Character Set Support in the [PostgreSQL documentation](https://www.postgresql.org/docs/current/multibyte.html) for more information.

**To support the storage of Unicode characters, the encoding used must be**  **UTF8.**

### How can I tell what the encoding is for my PostgreSQL database?

IMPORTANT: do not use the Windows console application psql with Unicode data; it's better to use pgadmin. With psql, you may see the following message:

`psql (15.2) WARNING: Console code page (437) differs from Windows code page (1252) 8-bit characters might not work correctly. See psql reference page "Notes for Windows users" for details.`

Use this SQL to determine the character set used by your database.

```
SELECT * from INFORMATION_SCHEMA.CHARACTER_SETS;
```


### What are the collation rules used in the database?

In PostgreSQL, collation rules are defined when initializing the server cluster (with initdb) and can be overridden for a particular database when creating the database. The database collation can be further overridden for individual columns (of tables) or SQL expressions. See [https://www.postgresql.org/docs/current/collation.html](https://www.postgresql.org/docs/current/collation.html). The following SQL will show the collation setting for each database in the cluster:

```
select datname,datcollate from pg_database;
```

The value of datcollate for a database that includes Unicode character text should be en\_ca.UTF8 (English Canada Unicode).

### What happens when I try to store Unicode characters in a non-Unicode-encoded database?

As an example, when the following INSERT statement is attempted to a table in a PostgreSQL database that is encoded as SQL_ASCII rather than UTF8,

```
SELECT * from INFORMATION_SCHEMA.CHARACTER_SETS;
CREATE TABLE testtable (testcol VARCHAR(100));
INSERT INTO testtable VALUES ('Secwe̓pemc');
SELECT substr(testcol,1,6) FROM testtable;
SELECT substr(testcol,1,7) FROM testtable;
```

The first SELECT returns "Secwe�".

The second SELECT returns

`
'rawunicodeescape' codec can't decode bytes in position 5-6: truncated \uXXXX escape
`


The Unicode code point U+0313 [represents](https://unicode-table.com/en/0313/) the diacritical above the letter 'e'. This code point is not defined in the ASCII character set used by the PostgreSQL database referenced above.

You may also see this error message:

`Unicode escape values cannot be used for code point values above 007F when the server encoding is not UTF8.`

### How do I change the encoding of a database?

1) Dump the database
2) Drop the database
3) Recreate the database
4) Reload the data

See [https://www.shubhamdipt.com/blog/how-to-change-postgresql-database-encoding-to-utf8/](https://www.shubhamdipt.com/blog/how-to-change-postgresql-database-encoding-to-utf8/) for full details.

