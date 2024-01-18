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