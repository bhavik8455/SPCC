#include<Stdio.h>
#include<String.h>
#include<Stdlib.h>
#include"CONVERSION.H"

void main(){
	int choice,i;
	char input[64];
	long decimal;
	
	printf("\n===== NUMBER CONVERSION MENU =====\n");
    printf("1. Binary to Decimal\n");
    printf("2. Decimal to Binary\n");
    printf("3. Binary to Hexadecimal\n");
    printf("4. Hexadecimal to Binary\n");
    printf("5. Exit\n");
    printf("Enter your choice (1-5): ");
	
	
	while(choice!=5){
		printf("Enter the Choice");
		scanf("%d",&choice);
		
		
		switch(choice){
			case 1 : printf("Enter the Binary number : ");
			scanf("%s",&input);
			decimal =BIN_TO_DEC(input);
			printf("The Decimal value is : %ld",decimal);
			printf("\n");
			break;
			
			case 2 : printf("Enter the Decimal number : ");
			scanf("%ld",&decimal);
			printf("The Binary value is \n");
			 DEC_TO_BIN(decimal);
			 printf("\n");
			break;
		
			case 3 : printf("Enter the Binary number : ");
			scanf("%s",&input);
			decimal = BIN_TO_HEX(input);
			printf("The hexadecimal value is : %lx",decimal);
			printf("\n");
			break;
		
			case 4 : printf("Enter the Haxdecimal number : ");
			scanf("%s",&input);
			printf("The Binary value is \n");
			 HEX_TO_BIN(input);
			 printf("\n");
			break;
			
			case 5 : break;
		
			

		}
	} 

}
