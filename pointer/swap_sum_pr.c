#include <stdio.h>
void ech(int *g, int *m)
{
	if (*g * *m > 0)
	{
		int y;
		y = *m;
		*m = *g;
		*g = y;
	}
	else
	{
		int s, p;
		s = *m + *g;
		p = *m * *g;
		*g = s;
		*m = p;
	}
}
int main(void)
{
	int a, b;
	int *k = &a;
	int *g = &b;
	
	printf("enter the value of numbers ");
	scanf("%d %d", k, g);
	ech (k, g);
	printf("the value of a is %d \n", *k);
	printf("the value of b is %d \n", *g);
	return 0;
}
