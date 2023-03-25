#include <stdio.h>

int main(int argc, char *argv[])
{
 FILE *fp;
 char *filename;
 char ch;
 int count = 0;

  // Check if a filename has been specified in the command
    if (argc < 2){
        printf("Specify a file first\n");
        return (1);
    }
    else{
        filename = argv[1];
        fp = fopen(filename,"r");
         // If file opened successfully, then print the contents
        if ( fp ){
            //if we are not reaching the end of a file, print
            while ((ch = fgetc(fp))!= EOF ){
                if(count!=0){
                    printf("%c",ch);
                }
                if(ch == '\n'){
                    count++;
                    printf("Hello, ");
                }
            }
        }
        else{
         printf("Failed to open the file\n");
        }
    }
return (0);
}