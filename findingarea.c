#include<stdio.h>
#include"AREA.H"

void main(){
	
	int l , b,option;
	
	printf("Menu\n1.AREA OF RECTANGLE\n2.AREA OF SQUARE\n3.Exit\n");
	
	while (option!=3){
		printf("\nEnter the choice\n");
		scanf("%d",&option);
		
	switch (option){
		
		
		case 1 : printf("Enter the Length and Breadth\n");
					scanf("%d%d",&l,&b);
				printf("The Area of Rectangle is %d\n",rectangle(l,b));
				break;
		case 2 : printf("Enter the Side of Square\n");
					scanf("%d",&l);
				printf("The Area of Square is %d\n",square(l));
				break;
		case 3 : 
			break;			
	}
	}
		
	}
	

