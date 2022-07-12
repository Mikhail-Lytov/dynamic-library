# dynamic-library
## General description
Dynamic library in C
## Dynamic Library Requirement

A procedure with the following prototype should be implemented in the library.
```c
char* pushkin(char* text);
```

As an input parameter, the procedure takes a pointer to an array that contains the first N 
lines of the work of A.S. Pushkin ["Ruslan and Lyudmila"] (https://www.culture.ru/poems/5061/ruslan-i-lyudmila-poema )
or NULL.

As an output value, the procedure returns a pointer to an array containing N+1 lines
of the product, or the first line if the input parameter is NULL.

Memory allocation should be performed in the procedure.
## Requirement for the executable program

When the program starts, it searches in the current directory and in all its subdirectories
for dynamic libraries (files with the .so extension). Each of the found libraries is a program
loads and receives from it (if possible) the pushkin procedure. If the procedure is received,
then a pointer to an array is passed to her as input (when the program starts, the pointer is NULL).

After calling the procedure from the last library, the resulting array should be output to the terminal as text.

## Makefile Requirement

The Makefile must contain rules with the following names.
- build — builds a program (if required) and a library
- run — starts the program
- clean — cleans the project directory from temporary files