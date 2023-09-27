#include <stdio.h>

int main(void)
{              
		float a, b;
		float *p = &a;
		float *r = &b;
		
		printf("enter the numbers a and b ");
		scanf("%f %f", p, r);
		float sum, prd, sous, div;
		
		sum = *p + *r;
		sous = *p - *r;
		prd = *p * *r;
		
		if (*r != 0)
		{
			div = *p / *r;
			printf("the div is %.2f\n", div);
		}
		else
			printf("the div is Error\n");
			
		printf("the sum is %.2f\n", sum);
		printf("the sous is %.2f\n", sous);
		printf("the multi is %.2f\n", prd);
		
		
		return 0;
}
