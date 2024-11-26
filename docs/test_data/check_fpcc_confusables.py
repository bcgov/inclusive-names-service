import csv
import sys
import unicodedata
import grapheme

def get_confusables_from_csv(input_csv):
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

def char_to_unicode_notation(char):
    # Ensure the input is a single character
    if len(char) != 1:
        raise ValueError("Input must be a single character.")
    
    # Get the Unicode code point of the character
    unicode_code = ord(char)
    
    # Format it as a Unicode escape sequence
    unicode_notation = f'\\u{unicode_code:04x}'
    
    return unicode_notation

if __name__ == "__main__":
    confusable_list = get_confusables_from_csv('confusables_unfolded.csv')
    fieldnames = ['string1','num_code_points_1','num_graphemes_1','string1_unicode','string2','num_code_points_2','num_graphemes_2','string2_unicode','string1_unicode_nfc','string1_unicode_nfd','string2_unicode_nfc','string2_unicode_nfd','string1_unicode_nfkc','string1_unicode_nfkd','string2_unicode_nfkc','string2_unicode_nfkd']
    outfile = open('fpcc_confusables_encoded.csv','w',encoding='utf-8-sig',newline='')
    writer = csv.DictWriter(outfile,fieldnames=fieldnames)
    writer.writeheader()
    charString = ''
    for listitem in confusable_list:
        string1 = listitem['char']
        string2 = listitem['confusable']
        string1_unicode = listitem['char_unicode']
        string2_unicode = listitem['confusable_unicode']
        num_code_points_1 = len(string1)
        num_graphemes_1 = grapheme.length(string1)
        num_code_points_2 = len(string2)
        num_graphemes_2 = grapheme.length(string2)
        unicode_string1_nfc = ''
        unicode_string2_nfc = '' 
        unicode_string1_nfd = ''
        unicode_string2_nfd = ''
        unicode_string1_nfkc = ''
        unicode_string2_nfkc = '' 
        unicode_string1_nfkd = ''
        unicode_string2_nfkd = ''
        string1_nfc = unicodedata.normalize('NFC',string1)
        string2_nfc = unicodedata.normalize('NFC',string2)
        string1_nfd = unicodedata.normalize('NFD',string1)
        string2_nfd = unicodedata.normalize('NFD',string2)
        string1_nfkc = unicodedata.normalize('NFKC',string1)
        string2_nfkc = unicodedata.normalize('NFKC',string2)
        string1_nfkd = unicodedata.normalize('NFKD',string1)
        string2_nfkd = unicodedata.normalize('NFKD',string2)
        
        for c in string1_nfc:
            if unicode_string1_nfc == '':
                unicode_string1_nfc = char_to_unicode_notation(c)
            else:    
                unicode_string1_nfc = unicode_string1_nfc + char_to_unicode_notation(c) 
        for c in string2_nfc:
            if unicode_string2_nfc == '':
                unicode_string2_nfc = char_to_unicode_notation(c) 
            else:    
                unicode_string2_nfc = unicode_string2_nfc + char_to_unicode_notation(c) 
        for c in string1_nfd:
            if unicode_string1_nfd == '':
                unicode_string1_nfd = char_to_unicode_notation(c) 
            else:    
                unicode_string1_nfd = unicode_string1_nfd + char_to_unicode_notation(c) 
        for c in string2_nfd:
            if unicode_string2_nfd == '':
                unicode_string2_nfd = char_to_unicode_notation(c) 
            else:    
                unicode_string2_nfd = unicode_string2_nfd + char_to_unicode_notation(c) 
        for c in string1_nfkc:
            if unicode_string1_nfkc == '':
                unicode_string1_nfkc = char_to_unicode_notation(c)
            else:    
                unicode_string1_nfkc = unicode_string1_nfkc + char_to_unicode_notation(c) 
        for c in string2_nfkc:
            if unicode_string2_nfkc == '':
                unicode_string2_nfkc = char_to_unicode_notation(c) 
            else:    
                unicode_string2_nfkc = unicode_string2_nfkc + char_to_unicode_notation(c) 
        for c in string1_nfkd:
            if unicode_string1_nfkd == '':
                unicode_string1_nfkd = char_to_unicode_notation(c) 
            else:    
                unicode_string1_nfkd = unicode_string1_nfkd + char_to_unicode_notation(c) 
        for c in string2_nfkd:
            if unicode_string2_nfkd == '':
                unicode_string2_nfkd = char_to_unicode_notation(c) 
            else:    
                unicode_string2_nfkd = unicode_string2_nfkd + char_to_unicode_notation(c) 

        writer.writerow({'string1':string1, 'num_code_points_1':num_code_points_1,'num_graphemes_1':num_graphemes_1,'string1_unicode':string1_unicode,'string2':string2, 'num_code_points_2':num_code_points_2,'num_graphemes_2':num_graphemes_2,'string2_unicode':string2_unicode,'string1_unicode_nfc':unicode_string1_nfc,'string1_unicode_nfd':unicode_string1_nfd,'string2_unicode_nfc':unicode_string2_nfc,'string2_unicode_nfd':unicode_string2_nfd,'string1_unicode_nfkc':unicode_string1_nfkc,'string1_unicode_nfkd':unicode_string1_nfkd,'string2_unicode_nfkc':unicode_string2_nfkc,'string2_unicode_nfkd':unicode_string2_nfkd})
    outfile.close()

