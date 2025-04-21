#include<stdio.h>
#include"FACT.h"

int main(){
	
	int f =1, i , num;
	
	printf("Enter the number");
	scanf("%d",&num);
	fact(num);
	printf("The Factorial is : %d",f);
	
	return 0;
}
