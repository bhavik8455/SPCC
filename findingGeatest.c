#include<stdio.h>
#include"GREATEST.H"

void main(){
	
	int a ,b;
	printf("Enter 2 Numbers \n");
	scanf("%d%d",&a,&b);
	printf("The Greatest Number is %d",max(a,b));
}
