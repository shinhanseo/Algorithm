#include <stdio.h>

int main()
{
  char ch[101];
  int arr = 0;
  int cnt = 0;

  scanf("%s", ch);

  while (ch[arr] != '\0')
  {
    cnt++;
    if (ch[arr] == '=')
    {
      if (ch[arr - 1] == 'z' && ch[arr - 2] == 'd')
      {
        cnt -= 2;
      }
      else
      {
        cnt--;
      }
    }

    if (ch[arr] == '-')
    {
      cnt--;
    }

    if (ch[arr] == 'j')
    {
      if (ch[arr - 1] == 'n' || ch[arr - 1] == 'l')
      {
        cnt--;
      }
    }
    arr++;
  }

  printf("%d", cnt);
}