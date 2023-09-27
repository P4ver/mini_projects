#include <stdio.h>

int main(void)
{              
	int a;
	int *p = &a;
	
	do
	{
		printf("enter positive number to calc the divisors ");
		scanf("%d", p);
	}while ( *p <= 0);

	printf("the divisors are : \n");
	for (int i = 1; i <= *p; i++)
	{
		if (*p % i == 0)
			printf("%d ", i);
	}
	return 0;
}
