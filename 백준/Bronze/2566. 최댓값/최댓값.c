#include <stdio.h>
int main()
{
  int num[9][9], max, col = 0, row = 0;
  for (int i = 0; i < 9; i++)
  {
    for (int j = 0; j < 9; j++)
    {
      scanf("%d", &num[i][j]);
    }
  }

  max = num[row][col];

  for (int i = 0; i < 9; i++)
  {
    for (int j = 0; j < 9; j++)
    {
      if (max < num[i][j])
      {
        max = num[i][j];
        row = i;
        col = j;
      }
    }
  }

  printf("%d\n", max);
  printf("%d %d", row + 1, col + 1);
}