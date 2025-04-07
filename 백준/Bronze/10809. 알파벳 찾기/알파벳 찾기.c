#include <stdio.h>
#include <string.h>
int main()
{
  char ch[100], arr = 0;
  char alpabet[26];

  scanf("%s", ch);
  for (int i = 0; i < 26; i++)
  {
    alpabet[i] = -1;
  }

  for (int i = strlen(ch) - 1; i >= 0; i--)
  {
    alpabet[(int)ch[i] - 97] = i;
  }

  for (int i = 0; i < 26; i++)
  {
    printf("%d ", alpabet[i]);
  }
}