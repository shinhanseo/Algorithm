#include <stdio.h>
#include <string.h>

int main()
{
  int alpabet[26] = {3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 10, 10, 10, 10};
  int time = 0;
  char ch[16];
  int len;

  scanf("%s", ch);
  len = strlen(ch);

  for (int i = 0; i < len; i++)
  {
    time += alpabet[(int)ch[i] - 65];
  }

  printf("%d", time);

  // 'A' => 65
}