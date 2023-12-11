## Create a new 
## Change the encoding of your database:

Dump your database
Drop your database,
Create new database with the different encoding
Reload your data.
(https://www.shubhamdipt.com/blog/how-to-change-postgresql-database-encoding-to-utf8/)

## Gotchas
Unicode escape values cannot be used for code point values above 007F when the server encoding is not UTF8.
Watch out for OS character set as it effects the sortability