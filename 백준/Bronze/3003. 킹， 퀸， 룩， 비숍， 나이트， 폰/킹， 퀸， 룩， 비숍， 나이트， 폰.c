#include <stdio.h>

int main()
{
  int standard[6] = {1, 1, 2, 2, 2, 8};
  int input[6];
  int white[6];

  for (int i = 0; i < 6; i++)
  {
    scanf("%d", &input[i]);
    white[i] = standard[i] - input[i];
  }
  for (int i = 0; i < 6; i++)
  {
    printf("%d ", white[i]);
  }
}