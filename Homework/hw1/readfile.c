/***************************************************
 * This program reads a file specified by the user *
 * as a command line argument and display the      *
 * contents of the file on screen.                 *
 ***************************************************/

#include <stdio.h>

int main(int argc, char *argv[])
{
 FILE *fp;
 char *filename;
 char ch;

  // Check if a filename has been specified in the command
  if (argc < 2)
   {
        printf("Missing Filename\n");
        return(1);
   }
   else
  {
        filename = argv[1];
   }

   // Open file in read-only mode
   fp = fopen(filename,"r");

   // If file opened successfully, then print the contents
   if ( fp )
      {
        while ((ch = fgetc(fp)) != EOF )
           {
                printf("%c",ch);
           }

       }
   else
      {
         printf("Failed to open the file\n");
        }

return(0);
}