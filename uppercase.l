%option noyywrap

%{
	#include<stdio.h>
	int uppercaseCount = 0;
%}

%%
[A-Z] {uppercaseCount++;}

%%

int main(){

	printf("Enter the tokens");
	yylex();
	printf("The Uppercase Count is %d",uppercaseCount);


}
