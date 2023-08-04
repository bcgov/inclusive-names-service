<html>
    <head>
        <title>PHP</title>
    </head>
    <body>
        <?php
          $myfile = fopen("../utf8.txt", "r") or die("Unable to open file!");
          while(!feof($myfile)) {
            $line = trim(fgets($myfile));
            if (strlen($line) > 0){
              echo "<div>\n";
              echo "String: " . $line . "<br />\n";
              echo "String type: " . gettype($line) . "<br />\n";
              echo "List: ";
              for ($i = 0; $i<strlen($line); $i++){
                //note this is the same as $line[$i]
                echo substr($line, $i, 1) . ", ";
              }
              echo "<br />\n";
              echo "Length: " . strlen($line) . "<br />\n";
              echo "Seventh character: " . $line[6] . "<br />\n";
              
              echo "Grapheme(s): ";
              for ($i = 0; $i<grapheme_strlen($line); $i++){
                echo grapheme_substr($line, $i, 1) . ", ";
              }
              echo "<br />\n";
              echo "Grapheme(s) Length: " . grapheme_strlen($line) . "<br />\n";
              echo "</div>\n";
              echo "<br />\n";
            }
          }
          
          fclose($myfile);
        ?>
    </body>
</html>