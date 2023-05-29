#include <stdio.h>
#include <stdlib.h>

/* The first byte of a UTF-8 character
 * indicates how many bytes are in
 * the character, so only check that
 */
int numberOfBytesInChar(unsigned char val) {
    if (val < 128) {
        return 1;
    } else if (val < 224) {
        return 2;
    } else if (val < 240) {
        return 3;
    } else {
        return 4;
    }
}

int main(){
    FILE *fin;
    FILE *fout;
    int character;
    fin = fopen("../utf8.txt", "r");
    fout = fopen("./output.txt","w");
    while( (character = fgetc(fin)) != EOF) {
        for (int i = 0; i < numberOfBytesInChar((unsigned char)character) - 1; i++) {
            putchar(character);
            fprintf(fout, "%c", character);
            character = fgetc(fin);
        }
        putchar(character);
        fprintf(fout, "%c", character);
    }
    fclose(fin);
    fclose(fout);
    printf("\nFile has been created...\n");
    return 0;
}