#include <stdio.h>


int main(void)
{
	int k, n;
	float sum = 0;
	float min, max = 0;

	printf("The number of students : ");
	scanf("%d", &k);
	float arr[k];
	
	printf("********************************\n");
	for (n = 1; n <= k; n++)
	{
		printf("Enter the grade of student %d : ", n);
		scanf("%f", &arr[n]);
	}
	printf("********************************\n");
	min = arr[1];
	for (n = 1; n <= k; n++)
	{
		sum = sum + arr[n];
		if (arr[n] > max)
			max = arr[n];
		if (arr[n] <= min)
			min = arr[n];

		printf("The grade of (student %d) = %.2f\n", n, arr[n]);
	}
	printf("********************************\n");
	printf("The average rating is %.2f\n", sum / k);
	printf("The highest grade is %.2f\n", max);
	printf("The lowest grade is %.2f\n", min);
}
/* 4 10 8 5

*/

    /*		https://youtu.be/2EZbmBC-mN0?list=PLZpzLuUp9qXxKSkKT43ppqzb8c2ahO4VS&t=736

			printf("enter greater or equal to 1  : ");
			scanf("%d", &m);		
			printf("%d", i);
		if(i != m)
			printf(" + ");
	*/