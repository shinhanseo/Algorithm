#include <stdio.h>
int main()
{
  char ch[1000];
  int cnt = 0;

  scanf("%s", ch);
  while (ch[cnt] != '\0')
  {
    cnt++;
  }

  printf("%d", cnt);
}