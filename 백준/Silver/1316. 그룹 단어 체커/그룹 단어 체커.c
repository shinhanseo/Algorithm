#include <stdio.h>
int main()
{
  int num, cnt = 0;
  char ch[100];
  scanf("%d", &num);

  for (int i = 0; i < num; i++)
  { // abba
    char alpabet[26] = {0};
    int arr = 0;

    scanf("%s", ch);

    while (ch[arr] != '\0')
    {
      if (alpabet[ch[arr] - 'a'] == 1)
      {
        if (ch[arr] != ch[arr - 1])
        {
          cnt++;
          break;
        }
      }

      alpabet[ch[arr] - 'a'] = 1;
      arr++;
    }
  }

  printf("%d", num - cnt);
  return 0;
}