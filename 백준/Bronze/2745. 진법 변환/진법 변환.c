#include <stdio.h>
#include <string.h>
#include <math.h>

int main()
{
  int num, len, sum = 0, p = 0;
  char ch[30];
  scanf("%s %d", ch, &num);
  len = strlen(ch);

  for (int i = len - 1; i >= 0; i--)
  {
    if (ch[i] < 65)
    {
      sum += (ch[i] - 48) * pow(num, p);
    }
    else
    {
      sum += (ch[i] - 'A' + 10) * pow(num, p);
    }
    p++;
  }

  printf("%d", sum);
  // A-> 65

  return 0;
}