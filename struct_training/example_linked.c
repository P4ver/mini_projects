#include <stdio.h>
#include <stdlib.h>
#include "ysIMOSIM.h"

int main(void)
{
	typedef struct inf
	{
		int age;
		struct inf *next;
	}data_1;
	
	data_1 *head = NULL;
	data_1 *second = NULL;
	
	
	head = (data_1 *)malloc(sizeof(data_1));
	second = (data_1 *)malloc(sizeof(data_1));
	
	head->age = 27;
	head->next = second;
	
	second->age = 50;
	second->next = NULL;
	
	void printlist(data_1 *n)
	{
		while (n != NULL)
		{
			printf("your age is %d \n", n->age);
			n = n->next;
		}
	}
	printlist(head);
	
	
	return 0;
}
