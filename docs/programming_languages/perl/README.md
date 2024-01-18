## Install required libraries
perl -MCPAN -e shell
install Unicode::GCString

## Gotchas
nothing really works without `use open qw( :std :encoding(UTF-8) );`
Much documentation suggests \X will work but I couldn't get it to work for graphemes and had to use the GCString library despite being on a newer version of perl
if you want to operate on graphemes you must use the object methods ie gcstring->substr NOT substr($gcstring->as_string) because the latter works on code points still and the former on graphemes
