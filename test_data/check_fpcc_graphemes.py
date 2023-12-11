import csv
import sys
import unicodedata

def get_graphemes_from_csv(input_csv):
    input_list = []
    with open(input_csv, mode='r', encoding='utf-8-sig') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            dict = {}
            for key in row.keys():
                dict[key] = row[key]
            line_count += 1
            input_list.append(dict)
        print( "Processed "+str(line_count)+' lines.')
    return input_list

if __name__ == "__main__":
    grapheme_list = get_graphemes_from_csv('fpcc_graphemes.csv')
    fieldnames = ['grapheme','num_code_points','names','frequency','code_points','utf8_encodings','length_strings']
    outfile = open('fpcc_graphemes_encoded.csv','w',encoding='utf-8-sig',newline='')
    outfile_allchars = open('fpcc_graphemes_oneline.csv','w',encoding='utf-8-sig',newline='')
    writer = csv.DictWriter(outfile,fieldnames=fieldnames)
    writer.writeheader()
    charString = ''
    for listitem in grapheme_list:
        grapheme = listitem['grapheme']
        codePointString = ''
        lengthString = ''
        utf8String = ''
        nameString = ''
        charString = charString + grapheme
        for c in grapheme:
            if nameString == '':
                codePointString = hex(ord(c))
                lengthString = str(len(hex(ord(c))))
                utf8String = str(c.encode('utf-8'))
                try:
                    nameString = unicodedata.name(c)
                except:
                    nameString = "**not in Unicode**"
            else:    
                codePointString = codePointString + ", " + hex(ord(c))
                lengthString = lengthString + ',' + str(len(hex((ord(c)))))
                utf8String = utf8String + ", " + str(c.encode('utf-8'))
                try:
                    nameString = nameString + ", " + unicodedata.name(c)
                except:
                    nameString = nameString + ", " + "**not in Unicode**"
        writer.writerow({'grapheme':grapheme, 'names':nameString,'frequency':listitem['count'],'num_code_points':len(grapheme),'code_points':codePointString,'utf8_encodings':utf8String, 'length_strings':lengthString })
    outfile_allchars.write(charString)
    outfile_allchars.close()
    outfile.close()

