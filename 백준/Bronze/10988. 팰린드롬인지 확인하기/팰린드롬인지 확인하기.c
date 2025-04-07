#include <stdio.h>
#include <string.h>

int main()
{
  char ch[100];
  char re_ch[100];
  scanf("%s", ch);

  for (int i = 0; i < strlen(ch); i++)
  {
    re_ch[strlen(ch)] = '\0';
    re_ch[strlen(ch) - i - 1] = ch[i];
  }

  if (strcmp(ch, re_ch) == 0)
    printf("1");
  else
    printf("0");
}