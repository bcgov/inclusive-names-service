use strict;
use Encode;
use open qw( :std :encoding(UTF-8) );
use Unicode::GCString ;

open IN, "../utf8.txt"; # this file is UTF-8

open(my $OUT_1, ">", "output.txt");

sub PrintBoth {
   print $OUT_1 $_[1];
   print $_[1];
}

while ( <IN> ) {
    chomp;
    my $line = $_;
    my $gcstring = Unicode::GCString->new( $line );
    PrintBoth($OUT_1, "String: $line\n");
    my $refType = ref($line);
    PrintBoth($OUT_1, "String Type: ${refType}\n");
    PrintBoth($OUT_1, "List: ");
    foreach my $char (split //, $line) {
      PrintBoth($OUT_1, "$char, ");
    }
    PrintBoth($OUT_1, "\n");
    PrintBoth($OUT_1, "Length: ${\length($line)}\n");
    PrintBoth($OUT_1, "Seventh character: ${\substr($line, 6, 1)}\n");
    my $count = 0;
    PrintBoth($OUT_1, "Grapheme(s): ");
    while ( my $gcchar = $gcstring->next ) {

        $count++;
        PrintBoth($OUT_1, "$gcchar, ");
    }
    
    PrintBoth($OUT_1, "\nGrapheme(s) Length: $count\n");
    PrintBoth($OUT_1, "Seventh Grapheme: ${\$gcstring->substr(6, 1)->as_string}\n");
    PrintBoth($OUT_1, "\n");

# Grapheme(s): S, M, O, N, E, Ć, T, E, N,
# Grapheme(s) Length: 9
}

close IN;
close OUT_1;