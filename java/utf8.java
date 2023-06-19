import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.OutputStreamWriter;
import java.text.BreakIterator;

public class utf8 {
  public static void main(String[] args) {
    // BufferedReader br = new BufferedReader(new InputStreamReader(
//     new FileInputStream("DirectionResponse.xml"), "UTF-8"));
    BufferedReader input = null;
    BufferedWriter output = null;
    try{  
      
      input = new BufferedReader(new InputStreamReader(new FileInputStream("../utf8.txt"), "UTF-8"));
      output = new BufferedWriter(new OutputStreamWriter(new FileOutputStream("./output.txt"), "UTF-8"));
      String s;
      while ((s=input.readLine())!=null) {
        System.out.println("String:  " + s);
        output.write("String:  " + s);
        output.newLine();

        System.out.println("String Type:  " + s.getClass().getName());
        output.write("String Type:  " + s.getClass().getName());
        output.newLine();

        System.out.print("List:  ");
        output.write("List: ");
        for (int i=0; i<s.length(); i++){
          if (i>0){
            System.out.print(", ");
            output.write(", ");
          }
          System.out.print(s.charAt(i));
          output.write(s.charAt(i));
        }
        System.out.println();
        output.newLine();

        System.out.println("Length: " + s.length());
        output.write("Length: " + s.length());
        output.newLine();

        System.out.println("Seventh Character: " + s.charAt(6));
        output.write("Seventh Character: " + s.charAt(6));
        output.newLine();

        BreakIterator it = BreakIterator.getCharacterInstance();
        it.setText(s);
        int count = 0;
        System.out.print("Graphemes: ");
        output.write("Graphemes: ");
        int start = it.first();
        for (int end = it.next(); end != BreakIterator.DONE; start = end, end = it.next()) {
          if (count > 0){
            System.out.print(", ");
            output.write(", ");
          }
          System.out.print(s.substring(start, end));
          output.write(s.substring(start, end));
          count++;
        }
        System.out.println("");
        output.newLine();

        System.out.println("Grapheme(s) Length: " + count);
        output.write("Grapheme(s) Length: " + count);
        System.out.println("");
        output.newLine();
        output.newLine();
      }
    }catch(Exception e){

    }

    try{
      input.close();
      output.close();
    }catch(IOException e){
      System.out.println("Error closing files");
    }

  }
}


// output = open("output.txt","w")
// with open("../utf8.txt",encoding="utf-8",mode="r") as exampleFile:
//     for line in exampleFile:
//         # Has new line from file input ensure we write out the proper encoded version
//         output.write("String: "+line)
//         print("String: "+line[:-1])

//         output.write("String type: "+str(type(line))+"\n")
//         print("String type: "+str(type(line)))

//         # Note that if you preface a string with u it becomes unicode instead of ascii
//         strList = u", ".join(list(line))
//         output.write("List: " + strList)
//         print("List: " + strList[:-1])

//         output.write("Length: "+str(len(line))+"\n")
//         print("Length: "+str(len(line)))

//         output.write("Seventh character: "+ line[6]+"\n")
//         print("Seventh character: " + line[6])

//         graphemeArr = regex.findall(r'\X', line, regex.U)
//         graphemes = u", ".join(graphemeArr)
//         output.write("Grapheme(s): " + graphemes)
//         print("Grapheme(s): " + graphemes, end = '')

//         output.write("Grapheme(s) Length: " + str(len(graphemeArr)) + "\n\n")
//         print("Grapheme(s) Length: " + str(len(graphemeArr)) + "\n")
// output.close()
// exampleFile.close()

// print("This output is also available in output.txt")
