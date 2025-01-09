import regex
import unicodedata
import grapheme
from anyascii import anyascii

def char_to_unicode_notation(char):
    # Ensure the input is a single character
    if len(char) != 1:
        raise ValueError("Input must be a single character.")
    
    # Get the Unicode code point of the character
    unicode_code = ord(char)
    
    # Format it as a Unicode escape sequence
    unicode_notation = f'\\u{unicode_code:04x}'
    
    return unicode_notation

def string_to_unicode_notation(string):
    unicode_notation = ''
    for c in string:
        unicode_notation = unicode_notation + char_to_unicode_notation(c)
    return unicode_notation

output = open("output.txt","w",encoding="utf-8")
with open("../utf8.txt",encoding="utf-8",mode="r") as exampleFile:
    for line in exampleFile:
        output.write("\n\nString: "+line)        
        OrigStringUnicode = string_to_unicode_notation(line)
        output.write("anyascii version: "+anyascii(line) )

        # Normalize the string 4 ways: NFC, NFKC, NFD, and NFKD
        # See https://stackoverflow.com/questions/16467479/normalizing-unicode
        NFCString = unicodedata.normalize('NFC',line)
        NFDString = unicodedata.normalize('NFD',line)
        NFKCString = unicodedata.normalize('NFKC',line)
        NFKDString = unicodedata.normalize('NFKD',line)
        NFCStringUnicode = string_to_unicode_notation(NFCString)
        NFDStringUnicode = string_to_unicode_notation(NFDString)
        NFKCStringUnicode = string_to_unicode_notation(NFKCString)
        NFKDStringUnicode = string_to_unicode_notation(NFKDString)
        NFCStrList = "".join(list(NFCString))
        NFDStrList = "".join(list(NFDString))
        NFKCStrList = "".join(list(NFKCString))
        NFKDStrList = "".join(list(NFKDString))
        output.write('NFC string: '+NFCString)
        output.write('NFD string: '+NFDString)
        output.write('NFKC string: '+NFKCString)
        output.write('NFKD string: '+NFKDString)
        output.write('Orig string unicode: '+OrigStringUnicode+"\n")
        output.write('NFC string unicode: '+NFCStringUnicode+"\n")
        output.write('NFD string unicode: '+NFDStringUnicode+"\n")
        output.write('NFKC string unicode: '+NFKCStringUnicode+"\n")
        output.write('NFKD string unicode: '+NFKDStringUnicode+"\n")
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

        graphemeArr = grapheme.graphemes(line)
        graphemes = u", ".join(graphemeArr)
        output.write("Grapheme(s): " + graphemes)
         
        output.write("Grapheme(s) Length: " + str(grapheme.length(line)) + "\n")
        
        output.write("Sixth Grapheme: "+grapheme.slice(line, start=5, end=6) + "\n")
        
output.close()
exampleFile.close()

print("Output is written to output.txt")
