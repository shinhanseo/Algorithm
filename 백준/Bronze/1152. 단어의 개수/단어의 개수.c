#include <stdio.h>
#include <string.h>

int main()
{
  char s[1000000];
  int arr = 0, cnt, len;
  gets(s);

  len = strlen(s);

  if (s[0] == ' ')
  {
    cnt = 0;
  }
  else
  {
    cnt = 1;
  }

  while (s[arr] != '\0')
  {
    if (s[arr] == ' ')
    {
      cnt++;
    }

    arr++;
  }

  if (s[arr - 1] == ' ')
    cnt--;

  printf("%d", cnt);

  return 0;
}