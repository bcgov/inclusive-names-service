# DBF files and Unicode
The original DBF standard defines the default encoding to be [ISO-8859-1](http://en.wikipedia.org/wiki/ISO/IEC_8859-1). However, DBF files can have different encodings; the specific encoding used is stored internally in DBF files. Python and other client software are able to specify the encoding when reading or writing a DBF file.

DBF files are used to store non-spatial column data in spatial shapefiles. The encoding used by the DBF component of a shapefile is stored in a single line [.cpg](https://github.com/bcgov/inclusive-names-service/blob/main/docs/file_formats/dbf/test_data.cpg) file.  See, for example, the (multi-file) shapefile [here](https://github.com/bcgov/inclusive-names-service/tree/main/docs/test_data/ADM_INDIAN_RESERVES_BANDS_SP) and the dbf file [here](https://github.com/bcgov/inclusive-names-service/blob/main/docs/file_formats/dbf/test_data.dbf).

[This python program](https://github.com/bcgov/inclusive-names-service/blob/main/docs/file_formats/dbf/getEncoding.py) illustrates how to use python to retrieve the encoding of a DBF file and now to set it to UTF-8.
