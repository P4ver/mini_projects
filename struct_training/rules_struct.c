#include <stdio.h>

int main(void)
{
	struct student {
		char *name;
		int age;
	};
	
	struct student stu = {"mohammed habti di natale", 20};
	
	printf("%s\n", stu.name);
	return 0;
}
