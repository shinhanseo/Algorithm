#include <stdio.h>
#include <string.h>
int main()
{
  int num, repeat, len;
  char s[21];
  scanf("%d", &num);

  for (int i = 0; i < num; i++)
  {
    scanf("%d %s", &repeat, s);
    len = strlen(s);
    for (int j = 0; j < len; j++)
    {
      for (int k = 0; k < repeat; k++)
      {
        printf("%c", s[j]);
      }
    }
    printf("\n");
  }
}