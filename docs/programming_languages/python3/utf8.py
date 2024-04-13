import regex
import unicodedata
import grapheme
from anyascii import anyascii

output = open("output.txt","w",encoding="utf-8")
with open("../utf8.txt",encoding="utf-8",mode="r") as exampleFile:
    for line in exampleFile:
        # Has new line from file input ensure we write out the proper encoded version
        output.write("\n\nString: "+line)
        print("String: "+line[:-1])
        
        output.write("anyascii version: "+anyascii(line) )
        print("anyascii version: "+anyascii(line))

        output.write("String type: "+str(type(line))+"\n")
        print("String type: "+str(type(line))+"\n")

        # Note that if you preface a string with u it becomes unicode instead of ascii
        # Normalize the string 4 ways: NFC, NFKC, NFD, and NFKD
        NFCStrList = u"".join(list(unicodedata.normalize('NFC',line)))
        NFDStrList = u"".join(list(unicodedata.normalize('NFD',line)))
        NFKCStrList = u"".join(list(unicodedata.normalize('NFKC',line)))
        NFKDStrList = u"".join(list(unicodedata.normalize('NFKD',line)))
        print('NFC character list: '+u", ".join(NFCStrList))
        print('NFD character list: '+u", ".join(NFDStrList))
        print('NFKC character list: '+u", ".join(NFKCStrList))
        print('NFKD character list: '+u", ".join(NFKDStrList))
        output.write('NFC character list: '+u", ".join(NFCStrList))
        output.write('NFD character list: '+u", ".join(NFDStrList))
        output.write('NFKC character list: '+u", ".join(NFKCStrList))
        output.write('NFKD character list: '+u", ".join(NFKDStrList))

        output.write("Length - NFC: "+str(len(NFCStrList))+"\n")
        print("Length - NFC: "+str(len(NFCStrList)-1)+"\n")
        output.write("Length - NFD: "+str(len(NFDStrList))+"\n")
        print("Length - NFD: "+str(len(NFDStrList)-1)+"\n")

        output.write("Seventh character (NFC): "+ NFCStrList[6]+"\n")
        print("Seventh character (NFC): "+ NFCStrList[6]+"\n")
        output.write("Seventh character (NFD): "+ NFDStrList[6]+"\n")
        print("Seventh character (NFD): "+ NFDStrList[6]+"\n")

        graphemeArr = regex.findall(r'\X', line, regex.U)
        graphemes = u", ".join(graphemeArr)
        output.write("Grapheme(s): " + graphemes)
        print("Grapheme(s): " + graphemes, end = '')
        
        output.write("Grapheme(s) Length: " + str(len(graphemeArr)-1) + "\n")
        print("Grapheme(s) Length: " + str(len(graphemeArr)-1) + "\n")
        
        output.write("Sixth Grapheme: "+grapheme.slice(line, start=5, end=6) + "\n")
        print("Sixth Grapheme: "+grapheme.slice(line, start=5, end=6) + "\n")
        
output.close()
exampleFile.close()

print("This output is also available in output.txt")
