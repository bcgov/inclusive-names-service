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
    
# Function to process the markdown file and produce a CSV file
def process_markdown_to_csv(markdown_file, csv_file):
    with open(markdown_file, 'r', encoding='utf-8') as md_file:
        lines = md_file.readlines()
    
    with open(csv_file, 'w', newline='', encoding='utf-8-sig') as csvfile:
        csvwriter = csv.writer(csvfile)
        # Write the header
        csvwriter.writerow(['Language', 'Grapheme', 'num_code_points','num_graphemes','string_unicode','string_unicode_nfc','string_unicode_nfd'])
        
        language = None
        for line in lines:
            line = line.strip()
            if line.startswith('#### '):
                language = line[4:].strip()
            elif len(line) == 0:
                language = None
            elif language and line:
                graphemes = line.split()
                for this_grapheme in graphemes:
                    if this_grapheme != "`":
                        if this_grapheme.startswith("`"):
                            this_grapheme = this_grapheme[1:]
                        num_code_points = len(this_grapheme)
                        num_graphemes = grapheme.length(this_grapheme)
                        unicode_grapheme = ''
                        unicode_string_nfc = ''
                        unicode_string_nfd = '' 
                        string_nfc = unicodedata.normalize('NFC',this_grapheme)
                        string_nfd = unicodedata.normalize('NFD',this_grapheme)
                        
                        for c in this_grapheme:
                            if unicode_grapheme == '':
                                unicode_grapheme = char_to_unicode_notation(c)
                            else:    
                                unicode_grapheme = unicode_grapheme + char_to_unicode_notation(c) 
                        for c in string_nfc:
                            if unicode_string_nfc == '':
                                unicode_string_nfc = char_to_unicode_notation(c)
                            else:    
                                unicode_string_nfc = unicode_string_nfc + char_to_unicode_notation(c) 
                        for c in string_nfd:
                            if unicode_string_nfd == '':
                                unicode_string_nfd = char_to_unicode_notation(c) 
                            else:    
                                unicode_string_nfd = unicode_string_nfd + char_to_unicode_notation(c) 

                        csvwriter.writerow([language, this_grapheme, num_code_points,num_graphemes,unicode_grapheme,unicode_string_nfc,unicode_string_nfd])

# Process the markdown file and produce the CSV file
process_markdown_to_csv('UBC_graphemes_readme.md', 'graphemes_by_language.csv')

print("CSV file has been created successfully.")