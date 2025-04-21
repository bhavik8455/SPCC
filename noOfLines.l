%option noyywrap

%{
	#include<stdio.h>
	int LinesCount = 0;
%}
%%
"\n"   {LinesCount++;}
%%

int main(){
	printf("Enter the source Code\n");
	yylex();
	printf("The No. of Lines in the Source Code is %d",LinesCount);


}
