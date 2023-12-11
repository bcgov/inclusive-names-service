#! /usr/bin/python2

import codecs
import regex

output = open("output.txt","w")
with codecs.open("../utf8.txt",encoding="utf-8",mode="r") as exampleFile:
    for line in exampleFile:
        encodedLine = line.encode("utf-8")
        # Has new line from file input ensure we write out the proper encoded version
        output.write("String: "+encodedLine)
        print("String: "+encodedLine[:-1])

        output.write("String type: "+str(type(encodedLine))+"\n")
        print("String type: "+str(type(encodedLine)))

        # Note that if you preface a string with u it becomes unicode instead of ascii
        strList = u", ".join(list(line)).encode('utf-8')
        output.write("List: " + strList)
        print("List: " + strList[:-1])

        output.write("Length: "+str(len(encodedLine))+"\n")
        print("Length: "+str(len(encodedLine)))

        output.write("Seventh character: "+ line[6].encode('utf-8')+"\n")
        print("Seventh character: " + line[6].encode('utf-8'))

        graphemeArr = regex.findall(r'\X', line, regex.U)
        graphemes = u", ".join(graphemeArr).encode('utf-8')
        output.write("Grapheme(s): " + graphemes + "\n\n")
        print "Grapheme(s): " + graphemes, 

        output.write("Grapheme(s) Length: " + str(len(graphemeArr)) + "\n\n")
        print("Grapheme(s) Length: " + str(len(graphemeArr)) + "\n")
output.close()
exampleFile.close()

print("This output is also available in output.txt")
