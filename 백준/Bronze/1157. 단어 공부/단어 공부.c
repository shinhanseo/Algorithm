#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main()
{
  int alpabet[26], max = 0, state = 0, len;
  char ch[1000000];
  scanf("%s", ch);
  len = strlen(ch);
  for (int i = 0; i < 26; i++)
  {
    alpabet[i] = 0;
  }

  for (int i = 0; i < len; i++)
  {
    ch[i] = toupper(ch[i]);
    alpabet[ch[i] - 'A'] += 1;
  }

  for (int i = 1; i < 26; i++)
  {
    if (alpabet[max] < alpabet[i])
    {
      max = i;
      state = 0;
    }

    else
    {
      if ((alpabet[max] > 0) && (alpabet[i] > 0) && (alpabet[max] == alpabet[i]))
        state = 1;
    }
  }

  if (state == 1)
  {
    printf("?\n");
  }
  else
  {
    printf("%c", max + 'A');
  }
}