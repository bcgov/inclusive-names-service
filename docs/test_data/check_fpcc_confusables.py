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

if __name__ == "__main__":
    confusable_list = get_confusables_from_csv('confusables_unfolded.csv')
    fieldnames = ['string1','num_code_points_1','num_graphemes_1','string1_unicode','string2','num_code_points_2','num_graphemes_2','string2_unicode']
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
        writer.writerow({'string1':string1, 'num_code_points_1':num_code_points_1,'num_graphemes_1':num_graphemes_1,'string1_unicode':string1_unicode,'string2':string2, 'num_code_points_2':num_code_points_2,'num_graphemes_2':num_graphemes_2,'string2_unicode':string2_unicode})
    outfile.close()

