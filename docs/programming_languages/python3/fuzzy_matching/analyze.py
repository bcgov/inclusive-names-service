import regex
import unicodedata
import grapheme
from anyascii import anyascii
import Levenshtein
import csv
from metaphone import doublemetaphone

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


output1 = open("NFD.txt","w",encoding="utf-8")
output2 = open("NFKD.txt","w",encoding="utf-8")
output3 = open("anyascii.txt","w",encoding="utf-8")
output4 = open("metaphone.txt","w",encoding="utf-8")
output5 = open("metaphone_secondary.txt","w",encoding="utf-8")
output6 = open("compare.txt","w",encoding="utf-8")
output7 = open("composite.txt","w",encoding="utf-8")

with open("./strings.txt",encoding="utf-8",mode="r") as exampleFile:
    for line in exampleFile:
        output3.write(anyascii(line) )
        output4.write(doublemetaphone(line)[0]+"\n")
        output5.write(doublemetaphone(line)[1]+"\n")
        NFDString = unicodedata.normalize('NFD',line)
        NFKDString = unicodedata.normalize('NFKD',line)
        output1.write(NFDString)
        output2.write(NFKDString)
        output7.write("original:"+line)
        output7.write("NFKD:"+NFKDString)
        output7.write("anyascii:"+anyascii(line))
        output7.write("metaphone:"+doublemetaphone(line)[0] + "\n")
        output7.write("unicode string"+string_to_unicode_notation(NFKDString)+"\n")
        output7.write("\n")
        
output1.close()
output2.close()
output3.close()
output4.close()
output5.close()
exampleFile.close()

with open('compare.csv', encoding="utf-8",mode="r") as csvfile:
    myreader = csv.reader(csvfile,delimiter=',')
    for row in myreader:
        output6.write("Levenshtein"+":"+row[0]+":"+row[1]+":"+str(Levenshtein.distance(row[0], row[1]))+':'+str(Levenshtein.ratio(row[0], row[1]))+"\n")
csvfile.close()
output6.close()