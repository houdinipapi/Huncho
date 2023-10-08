#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//C File handling
//1. Stream-oriented data files - the data is stored in the same manner as it appears on the screen.
//2. System-oriented data files - the data files are more closely associated with the OS.


//C file Operations
//creation of a new file, opening, reading, writing data in a file, closing a file.


//Steps for Processing a File
//1. Declare a file pointervariable
//2. Open a file using fopen()
//3. Process the file using the suitable function.
//4. Close the file using fclose() function.


// File Handlers available in stdio.h
// fopen -> 
// fclose ->
// getc -> Read a character from a file
// putc -> Write a character into a file
// getw -> Read an integer from a file
// putw -> Write an integer into a file
// fprintf -> Prints formatted output into a file.
// fscanf -> Reads formatted input from a file.
// fgets -> Reads a string of characters from a file.
// fputs -> Writes a string of characters into a file.
// feof -> Detects end of file marker in a single file.

int main()
{
	//FILE *fopen( const char * filePath, const char * mode );
	FILE *fp;
	fp = fopen("filename.txt", "W");
	//processing of the files
	fprintf(fp, "%s", "Hello World");
	//end of processing
	fclose(fp);

	return 0;
}
