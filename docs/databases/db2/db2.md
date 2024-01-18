## Unicode Support in Db2

Db2 is a relational database management system offered by IBM. It includes a family of products that run on a range of operating systems, including Linux®, UNIX, Windows, IBM i, VSE, VM, and z/OS (i.e., both mainframe and workstation).

More recent versions of Db2 support Unicode, but [text segmentation](https://unicode.org/reports/tr29/) (i.e., grapheme support) and [normalization](https://unicode.org/reports/tr15/) need to be implemented outside of the database (i.e., by the application programs).

To support Unicode in a system based on Db2, the Db2 database must use a Unicode encoding. Instructions on converting a non-Unicode database (e.g., EBCDIC, ASCII) to Unicode can be found at [Converting non-Unicode databases to Unicode](https://www.ibm.com/docs/en/db2/11.5?topic=encoding-converting-non-unicode-databases-unicode) and [Converting existing Db2 data to Unicode](https://www.ibm.com/docs/en/db2-for-zos/13?topic=data-converting-existing-db2-unicode).

### References
[What is Db2 for z/OS?](https://www.ibm.com/docs/en/db2-for-zos/13?topic=getting-started-db2-zos)

[Db2 database product editions and Db2 offerings](https://www.ibm.com/docs/en/db2/11.5?topic=editions-db2-database-product-offerings)

[Unicode implementation in Db2](https://www.ibm.com/docs/en/db2/11.5?topic=encoding-unicode-implementation-in-db2)

[Unicode Character Encoding](https://www.ibm.com/docs/en/db2/11.5?topic=support-unicode-character-encoding)

[Green screen applications and Unicode data](https://www.ibm.com/docs/en/db2-for-zos/13?topic=ccsids-green-screen-applications-unicode-data)