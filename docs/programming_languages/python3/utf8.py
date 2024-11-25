import regex
import unicodedata
import grapheme
from anyascii import anyascii

output = open("output.txt","w",encoding="utf-8")
with open("../utf8.txt",encoding="utf-8",mode="r") as exampleFile:
    for line in exampleFile:
        output.write("\n\nString: "+line)        
        output.write("anyascii version: "+anyascii(line) )

        # Normalize the string 4 ways: NFC, NFKC, NFD, and NFKD
        # Use the ascii function to ensure non-ASCII codepoints are printed using escape syntax
        # See https://stackoverflow.com/questions/16467479/normalizing-unicode
        NFCString = unicodedata.normalize('NFC',line)
        NFDString = unicodedata.normalize('NFD',line)
        NFKCString = unicodedata.normalize('NFKC',line)
        NFKDString = unicodedata.normalize('NFKD',line)
        NFCStringAscii = ascii(unicodedata.normalize('NFC',line))
        NFDStringAscii = ascii(unicodedata.normalize('NFD',line))
        NFKCStringAscii = ascii(unicodedata.normalize('NFKC',line))
        NFKDStringAscii = ascii(unicodedata.normalize('NFKD',line))
        NFCStrList = "".join(list(NFCString))
        NFDStrList = "".join(list(NFDString))
        NFKCStrList = "".join(list(NFKCString))
        NFKDStrList = "".join(list(NFKDString))
        output.write('NFC string: '+NFCString)
        output.write('NFD string: '+NFDString)
        output.write('NFKC string: '+NFKCString)
        output.write('NFKD string: '+NFKDString)
        output.write('NFC string ascii: '+NFCStringAscii+"\n")
        output.write('NFD string ascii: '+NFDStringAscii+"\n")
        output.write('NFKC string ascii: '+NFKCStringAscii+"\n")
        output.write('NFKD string ascii: '+NFKDStringAscii+"\n")
        output.write('NFC character list: '+", ".join(NFCStrList))
        output.write('NFD character list: '+", ".join(NFDStrList))
        output.write('NFKC character list: '+", ".join(NFKCStrList))
        output.write('NFKD character list: '+", ".join(NFKDStrList))

        output.write("Length - NFC: "+str(len(NFCStrList))+"\n")
        output.write("Length - NFD: "+str(len(NFDStrList))+"\n")
        output.write("Length - NFKC: "+str(len(NFKCStrList))+"\n")
        output.write("Length - NFKD: "+str(len(NFKDStrList))+"\n")

        if len(NFCStrList) > 6:
            output.write("Seventh character (NFC): "+ NFCStrList[6]+"\n")
        if len(NFDStrList) > 6:
            output.write("Seventh character (NFD): "+ NFDStrList[6]+"\n")
        if len(NFKCStrList) > 6:
            output.write("Seventh character (NFKC): "+ NFKCStrList[6]+"\n")
        if len(NFKDStrList) > 6:
            output.write("Seventh character (NFKD): "+ NFKDStrList[6]+"\n")

#        graphemeArr = regex.findall(r'\X', line, regex.U)
#        graphemes = u", ".join(graphemeArr)
        graphemeArr = grapheme.graphemes(line)
        graphemes = u", ".join(graphemeArr)
        output.write("Grapheme(s): " + graphemes)
         
#        output.write("Grapheme(s) Length: " + str(len(graphemeArr)-1) + "\n")
        output.write("Grapheme(s) Length: " + str(grapheme.length(line)) + "\n")
        
        output.write("Sixth Grapheme: "+grapheme.slice(line, start=5, end=6) + "\n")
        
output.close()
exampleFile.close()

print("Output is written to output.txt")
