import regex
import unicodedata
import grapheme
from anyascii import anyascii

output = open("output.txt","w",encoding="utf-8")
with open("../utf8.txt",encoding="utf-8",mode="r") as exampleFile:
    for line in exampleFile:
        output.write("\n\nString: "+line)        
        output.write("anyascii version: "+anyascii(line) )

        output.write("String type: "+str(type(line))+"\n")

        # Normalize the string 4 ways: NFC, NFKC, NFD, and NFKD
        NFCStrList = "".join(list(unicodedata.normalize('NFC',line)))
        NFDStrList = "".join(list(unicodedata.normalize('NFD',line)))
        NFKCStrList = "".join(list(unicodedata.normalize('NFKC',line)))
        NFKDStrList = "".join(list(unicodedata.normalize('NFKD',line)))
        output.write('NFC character list: '+", ".join(NFCStrList))
        output.write('NFD character list: '+", ".join(NFDStrList))
        output.write('NFKC character list: '+", ".join(NFKCStrList))
        output.write('NFKD character list: '+", ".join(NFKDStrList))

        output.write("Length - NFC: "+str(len(NFCStrList))+"\n")
        output.write("Length - NFD: "+str(len(NFDStrList))+"\n")

        output.write("Seventh character (NFC): "+ NFCStrList[6]+"\n")
        output.write("Seventh character (NFD): "+ NFDStrList[6]+"\n")

        graphemeArr = regex.findall(r'\X', line, regex.U)
        graphemes = u", ".join(graphemeArr)
        output.write("Grapheme(s): " + graphemes)
         
        output.write("Grapheme(s) Length: " + str(len(graphemeArr)-1) + "\n")
        
        output.write("Sixth Grapheme: "+grapheme.slice(line, start=5, end=6) + "\n")
        
output.close()
exampleFile.close()

print("Output is written to output.txt")
