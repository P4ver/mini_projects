#include <stdio.h>

int main(void)
{
	 typedef struct data
	{
		char *name;
		int age;
		char *cntr;
	}mdata;
	
	typedef struct info
	{
		char *team;
		mdata mini_data;
	}info;
	
	info *persone_1;
	
	persone_1->team = "Raja";
	persone_1->mini_data.name="mohammed";
	persone_1->mini_data.age= 27;
	persone_1-> mini_data.cntr="morocco";
	
	void full_info(info *human)
	{
		printf("Team    : %s\n", human->team);
		printf("Name    : %s\n", human->mini_data.name);
		printf("Age     : %d\n", human->mini_data.age);
		printf("Country : %s\n", human->mini_data.cntr);
		printf("____________________________\n");
	}
	
	full_info(persone_1);
	
	return 0;
}
/* struct with pointers -----------
	player p1, *p2;
	
	p1.name = "abdelghani";
	
	p2->name = "mohammed habti";
	p2->number = 9;
	p2->team = "juventus";
	
	printf("%s\n", p1.name);

	printf("name : %s \n", p2->name);
	printf("the t-shirt number : %d \n", p2->number);
	printf("the team : %s", p2->team);
*/

/* the easiest way-----------------

	struct name
	{
		char *name;
		int age;
		char cou[50];
	}s1;

	s1.name = "mohammed";
	s1.age = 59;

	printf("%s\n", s1.name);
	printf("%d\n", s1.age);

*/

/*Nested struct--------------------------
	 typedef struct data
	{
		char *name;
		int age;
		char *cntr;
	}mdata;
	
	typedef struct info
	{
		char *team;
		mdata mini_data;
	}info;
	
	info player;
	player.team = "morocco";
	player.mini_data.name = "mohammed";
	player.mini_data.age = 89;
	
	printf("%s\n", player.team);
	printf("%s\n",player.mini_data.name);
	printf("%d\n", player.mini_data.age);	

// ---
	struct data
	{
		char *name;
		int age;
		char *cntr;
	};
	
	typedef struct info
	{
		char *team;
		struct data mini_data;
	}info;
	
	info player;
	player.team = "morocco";
	player.mini_data.name = "mohammed";
	player.mini_data.age = 89;
	
	printf("%s\n", player.team);
	printf("%s\n",player.mini_data.name);
	printf("%d\n", player.mini_data.age);

//-------------------------------------------------

	typedef struct team
	{
		char *player;
		char *position;
		int num_tshirt;
		int goals;
	}data;
	
	data raja;
	raja.player = "hafidi";
	raja.num_tshirt = 18;
	raja.goals = 149;
	
	printf("%s\n", raja. player);
	printf("%d\n", raja. num_tshirt);
	printf("%d\n", raja. goals);
//---------------------------------------------------
	struct book 
	{
		char *name;
		int pages;
		float price;
		char *author;
	};
	struct book livre1;
	livre1.name = "Learn English";
	livre1.pages = 200;
	livre1.price = 55.9;
	livre1.author = "ALEX smith";
	
	printf("%s\n", livre1.name);
	printf("%s\n", livre1.author);
	printf("%d\n", livre1.pages);
	printf("%.2f\n", livre1.price);

// ----------------------------------------------
	struct student {
		char *name;
		int age;
	};
	
	struct student stu = {"mohammed habti di natale", 20};
	
	printf("%s\n", stu.name);
*/