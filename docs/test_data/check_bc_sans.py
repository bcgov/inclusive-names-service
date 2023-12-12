from itertools import chain
import sys

from fontTools.ttLib import TTFont
from fontTools.unicode import Unicode


with TTFont(
    sys.argv[1], 0, allowVID=0, ignoreDecompileErrors=True, fontNumber=-1
) as ttf:
    chars = chain.from_iterable(
        [y + (Unicode[y[0]],) for y in x.cmap.items()] for x in ttf["cmap"].tables
    )
    outfile = 'check_bc_sans.csv'
    f = open(outfile,"w",encoding="utf-8")
    f.write('\ufeff')
    f.write("code point (dec),short name,full name,byte value,chr()\n")

    if len(sys.argv) == 2:  # print all code points
        for c in chars:
            frame = b"e"
            frame += (chr(c[0]).encode('utf-8'))
            mychar = frame.decode('utf-8')
            strval = str(c[0])+','+c[1]+','+c[2] + ',' + str((chr(c[0])).encode('utf-8')) + ',' + chr(c[0])  +  ',' + '\n'
            f.write(strval)
            
