#include <stdio.h>
int main()
{
  int arr, circle, i, j, k;
  scanf("%d %d", &arr, &circle);

  int box[arr];
  for (int a = 0; a < arr; a++)
  {
    box[a] = 0;
  }

  for (int m = 0; m < circle; m++)
  {
    scanf("%d %d %d", &i, &j, &k);
    for (int n = i; n <= j; n++)
    {
      box[n - 1] = k;
    }
  }

  for (int q = 0; q < arr; q++)
  {
    printf("%d ", box[q]);
  }
}