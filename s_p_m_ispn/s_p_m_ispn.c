#include <stdio.h>

void sum(float arr[])
{
	float s = 0;
	for (int i = 0; i < 5; i++)
	{
	s = s + arr[i];
	}
	printf("the sum is %.2f\n", s);
}
void prd(float arr[])
{
	float k = 1;
	for (int i = 0; i < 5; i++)
	{
		k = k * arr[i];
	}
	printf("the multip %.2f\n", k);
}
void avrg(float arr[])
{
	float s = 0;
	for (int i = 0; i < 5; i++)
	{
		s = s + arr[i];
	}
	printf("the average is %.2f\n", s/5);
}
void is_pn(float arr[])
{
	for (int i = 0; i < 5; i++)
	{
		if (arr[i] >= 0)
			printf("the number %.2f is positive \n",arr[i]);
		else
			printf("the number %f i.2s negative \n",arr[i]);
	}
}
int main(void)
{
	float arr[100];
	for (int i = 0; i < 5; i++)
	{
		printf("enter a arr[%d] = ", i);
		scanf("%f", &arr[i]);
	}
	sum(arr);
	prd(arr);
	avrg(arr);
	is_pn(arr);
	return 0;
}
