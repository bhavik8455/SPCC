%option noyywrap
%{
	#include<stdio.h>
	#include<String.h>
	int count = 0;
	char keywords[100][50];


%}

%%
"while"|"if"|"else"|"for"|"int"|"float"  {
	
	strcpy(keywords[count++],yytext);

}

%%

int main(){
	int i;
	printf("Enter the Code\n");
	yylex();
	
	for( i = 0 ; i < count;i++){
	printf(" %s ",keywords[i]);
	
	}
	


}
