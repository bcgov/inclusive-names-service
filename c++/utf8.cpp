#include <iostream>
#include <string>
#include <fstream>
#include <codecvt>

using namespace std;

std::wstring utf8_to_ws(std::string const& utf8)
{
    std::wstring_convert<std::codecvt_utf8<wchar_t>, wchar_t> cnv;
    std::wstring s = cnv.from_bytes(utf8);
    if(cnv.converted() < utf8.size())
        throw std::runtime_error("incomplete conversion");
    return s;
}


int main (){
  
  ifstream fin("../utf8.txt");
  ofstream fout("output.txt");
  string line;
  
  while (getline(fin, line)) {
    string l = "String: " + line + "\n";
    auto w = utf8_to_ws(line); // convert to wide (UTF-32/UCS-2)

    cout << l;
    fout << l;

    l = "Type: string\n";
    cout << l;
    fout << l;

    l = "List: ";
    cout << l;
    fout << l;
    for (int i=0; i<line.length(); i++){
      if (i > 0){
        cout << ", ";
        fout << ", ";
      }
      cout << line[i];
      fout << line[i];
    }
    cout << "\n";
    fout << "\n";


    l = "Line Length: ";
    cout << l << line.length() << "\n";
    fout << l << line.length() << "\n";
    //note line length
    l = "Codepoint Length: ";
    cout << l << w.length() << "\n";
    fout << l << w.length() << "\n";

    l = "Seventh Character: ";
    cout << l << line[6] << "\n";
    fout << l << line[6] << "\n";

    // cout << "Grapheme(s): ");
    // fout << fout, "Grapheme(s): ");
    // cout << "\n");
    // fout << fout, "\n");

    // cout << "Grapheme(s) Length: %d\n", len);
    // fout << fout, "Grapheme(s) Length: %d\n", len);

    cout << "\n";
    fout << "\n";

  }
  fin.close();
  fout.close();
  cout << "File has been created...\n";
  return 0;
}