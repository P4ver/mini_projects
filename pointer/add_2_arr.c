#include <stdio.h>

int main(void)
{
	int sa;
	int sb;

	printf ("enter the size of array sa = ");
	scanf("%d", &sa);
	printf("enter the size of array sb = ");
	scanf ("%d", &sb);
	
	int arr[100];
	int brr[100];

	int *p = arr;
	int *r = brr;
	
	for (p = arr; p < arr + sa; p++)
	{
		printf("enter the value arr[%d]= ", p - arr);
		scanf("%d", p);
	}
	for (r = brr; r < brr + sb; r++)
	{
		printf("enter the value of brr[%d]= ", r - brr);
		scanf("%d", r);
	}
	int sz = sa + sb;
	p = arr;
	for (r = brr; r < brr + sz; r++)
	{
		*(p + sa) = *r;
		sa++;
	}
	
	for (p = arr ; p < arr + sz; p++)
	{
		printf(" %d ", *p);
	}

	return 0;
}
