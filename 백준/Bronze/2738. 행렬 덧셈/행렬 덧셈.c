#include <stdio.h>
int main()
{
  int n, m;
  scanf("%d %d", &n, &m);

  int matrix_a[n][m];
  int matrix_b[n][m];

  for (int i = 0; i < n; i++)
  {
    for (int j = 0; j < m; j++)
    {
      scanf("%d", &matrix_a[i][j]);
    }
  }

  for (int i = 0; i < n; i++)
  {
    for (int j = 0; j < m; j++)
    {
      scanf("%d", &matrix_b[i][j]);
    }
  }

  for (int i = 0; i < n; i++)
  {
    for (int j = 0; j < m; j++)
    {
      printf("%d ", matrix_a[i][j] + matrix_b[i][j]);
    }
    printf("\n");
  }
}