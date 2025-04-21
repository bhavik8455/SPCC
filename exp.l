%option noyywrap
%{
	#include<stdio.h>
	int vowels = 0;
	int consonents = 0;
%}
%%
[aeiou]	{vowels++;}
[bcdfghjklmnpqrstvwxyz]   {consonents++;}
"\n"	{printf("The vowels count is %d and Consonent count is %d",vowels,consonents);}
%%

int main(){
	printf("Enter the word");
	yylex();
	return 0;


}
