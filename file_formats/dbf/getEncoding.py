import dbf
table = dbf.Table("test_data.dbf")
table.open(mode=dbf.READ_WRITE)
# get current encoding
print(table)
# set encoding to UTF8
table.codepage = dbf.CodePage('utf8')
print(table)
table.close()



