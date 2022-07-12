//библиотека Лытов Михаил
#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "pushkin.h"
	
char* pushkin( char* text ){
	int line = 0; // это строчка, которую мы должны вернуть, если массив пришел не NULL
	int stop = 0;	
	if (text == NULL) { //если пустой пришёл
		return pushkin_text[0];
	}else if(text != NULL){	// уже был не пустой масcив
		for (int i = 0; i < 153; i++)	
			if ( strstr(text, pushkin_text[i]) ){
				line++;
			}
		}

asprintf(&text, "%s%s", text, pushkin_text[line]);
return text;
}