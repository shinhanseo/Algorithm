#include <stdio.h>
int main()
{
  int arr, circle, i, j, tmp;
  scanf("%d %d", &arr, &circle);
  int box[arr];
  for (int m = 0; m < arr; m++)
  {
    box[m] = m + 1;
  }

  for (int m = 0; m < circle; m++)
  {
    scanf("%d %d", &i, &j);
    tmp = box[i - 1];
    box[i - 1] = box[j - 1];
    box[j - 1] = tmp;
  }

  for (int n = 0; n < arr; n++)
  {
    printf("%d ", box[n]);
  }
}