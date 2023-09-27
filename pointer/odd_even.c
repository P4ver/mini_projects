#include <stdio.h>

int main(void)
{              
		int a;
		int *p = &a;
		
		printf("enter the numbers a and b ");
		scanf("%d", p);
		
		if (*p % 2 == 0)
			printf("the number is even");
		else
			printf("the number is odd");
		
		return 0;
}
