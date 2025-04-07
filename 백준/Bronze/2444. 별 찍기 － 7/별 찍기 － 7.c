#include <stdio.h>
int main()
{
  int num;
  int star = 1;
  scanf("%d", &num);

  for (int i = 1; i <= num; i++)
  {
    for (int j = 0; j < num - i; j++)
    {
      printf(" ");
    }
    for (int k = 0; k < star; k++)
    {
      printf("*");
    }
    star += 2;
    printf("\n");
  }

  star -= 4;
  for (int i = 1; i < num; i++)
  {
    for (int j = 0; j < i; j++)
    {
      printf(" ");
    }
    for (int k = 0; k < star; k++)
    {
      printf("*");
    }
    star -= 2;
    printf("\n");
  }
}