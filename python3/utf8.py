#! /usr/local/bin/python3

import regex

output = open("output.txt","w")
with open("../utf8.txt",encoding="utf-8",mode="r") as exampleFile:
    for line in exampleFile:
        # Has new line from file input ensure we write out the proper encoded version
        output.write("String: "+line)
        print("String: "+line[:-1])

        output.write("String type: "+str(type(line))+"\n")
        print("String type: "+str(type(line)))

        # Note that if you preface a string with u it becomes unicode instead of ascii
        strList = u", ".join(list(line))
        output.write("List: " + strList)
        print("List: " + strList[:-1])

        output.write("Length: "+str(len(line))+"\n")
        print("Length: "+str(len(line)))

        output.write("Seventh character: "+ line[6]+"\n")
        print("Seventh character: " + line[6])

        graphemeArr = regex.findall(r'\X', line, regex.U)
        graphemes = u", ".join(graphemeArr)
        output.write("Grapheme(s): " + graphemes + "\n\n")
        print("Grapheme(s): " + graphemes + "\n")
output.close()
exampleFile.close()

print("This output is also available in output.txt")
