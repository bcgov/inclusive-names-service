# Techniques for Dealing with Unicode Data
This repository includes code and tips that will be useful to systems developers and maintainers who need to ensure that their computer systems can properly input, store, process, and display/export Unicode characters.

### Programming Languages
Some older programming languages assume an equivalence between characters and bytes (i.e., one character requires exactly one byte of storage). With these languages, handling multi-byte or variable length encodings such as UTF-8 requires special libraries or techniques. The following link provides the details.

[Programming Languages](.\programming_languages\README.md)

### Database Management Systems
Systems that process Unicode data and use database management systems (DBMS) need to have those DBMS's configured to store data using a Unicode encoding. The following link provides guidance for configuring a DBMS to use the UTF-8 encoding.

[Databases](.\databases\README.md)

### Some Test Data
The following link points to a directory containing data files that have Unicode data.

[Test Data](.\test_data\README.md)

### File Formats
This section provides guidance on handling Unicode data using various file formats (e.g., CSV, Excel)

[File Formats](.\file_formats\README.md)

### Data Transfer Protocols
This section provides guidance on handling Unicode data when using various data transfer protocols (e.g., ftp)
[Data Transfer Protocols](.\data_transfer_protocols\README.md)

### Data Flow Analysis Primer and Example
This section introduces the subject of data flow analysis, which can be used to evaluate whether a particular system might encounter issues when working with Unicode data.

[Data Flow Analysis](.\data_flow_analysis\README.md)