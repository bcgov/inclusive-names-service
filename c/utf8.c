#include <stdio.h>
#include <wchar.h>
#include <stdlib.h>
#include <locale.h>

#ifndef BUFSIZE
  #define BUFSIZE 100
#endif

int count_utf8_code_points(const char *s) {
    int count = 0;
    while (*s) {
        count += (*s++ & 0xC0) != 0x80;
    }
    return count;
}

int main (){
  //must set locale or get ? chars
  setlocale(LC_ALL, "");
  FILE * fin;
  FILE * fout;
  wint_t wc;
  wchar_t newl = L'\n';
  fin=fopen ("../utf8.txt","r");
  fout=fopen("output.txt","w");
  wchar_t st[BUFSIZE] = L"";
  int len = 0;
  while((wc=fgetwc(fin))!=WEOF){
        // work with: "wc"
        if (wc != newl){
          len += swprintf(st+len, BUFSIZE-len, L"%lc", wc);
        }else{
          printf("String: %ls\n", st);
          fprintf(fout, "String: %ls\n", st);

          printf("Type: wchar_t\n");
          fprintf(fout, "Type: wchar_t\n");

          printf("List: ");
          fprintf(fout, "List: ");
          for (int i=0; i<wcslen(st); i++){
            printf("%lc, ", st[i]);
            fprintf(fout, "%lc, ", st[i]);
          }
          printf("\n");
          fprintf(fout, "\n");

          printf("Length: %lu\n", wcslen(st));
          fprintf(fout, "Length: %lu\n", wcslen(st));

          printf("Seventh Character: %lc\n", st[6]);
          fprintf(fout, "Seventh Character: %lc\n", st[6]);

          // printf("Grapheme(s): ");
          // fprintf(fout, "Grapheme(s): ");
          // printf("\n");
          // fprintf(fout, "\n");

          // printf("Grapheme(s) Length: %d\n", len);
          // fprintf(fout, "Grapheme(s) Length: %d\n", len);

          swprintf(st, BUFSIZE, L"");
          len = 0;
        }
  }
  fclose(fin);
  fclose(fout);
  printf("File has been created...\n");
  return 0;
}