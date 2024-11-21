from pyuca import Collator
c = Collator()
unsorted_list = ['AA', 'AB','AZ','CA','CB','CZ','DA','EA','MA','NA','OA','VA','WA','XA','ZA','ZB','ZZ','ĆL NFC','ĆL NFD','ə','ŋ','ʷ']
sorted_list = sorted(unsorted_list,key=c.sort_key)
print("Sorted list:", sorted_list
