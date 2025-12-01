from anyascii import anyascii
import Levenshtein
import csv

results = open("fuzzy_substring_results.txt","w",encoding="utf-8")
with open('parks_and_parts.csv', encoding="utf-8",mode="r") as csvfile:
    myreader = csv.reader(csvfile,delimiter=',')
    for row in myreader:
        full_string = anyascii(row[0])
        search_string = anyascii(row[1])
        print("full string "+full_string)
        print("search string "+ search_string)
        best_string =""
        best_score = 0
        for i in range(len(full_string) - len(search_string)):
            target = full_string[i:i+len(search_string)]
            lev_ratio = Levenshtein.ratio(search_string, target)
            if lev_ratio > best_score:
                best_score = lev_ratio
                best_string = target
        print("best score = "+str(best_score) + " matches "+best_string+"\n")
csvfile.close()
results.close()