#include <stdio.h>
int main()
{
  int num, sum = 0;
  scanf("%d", &num);
  char s[num];

  scanf("%s", s);
  for (int i = 0; i < num; i++)
  {
    sum += (int)s[i] - 48;
  }

  printf("%d", sum);
}