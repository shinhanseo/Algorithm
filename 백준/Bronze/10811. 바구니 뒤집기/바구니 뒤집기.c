#include <stdio.h>
int main()
{
  int i, j, arr, input, tmp;
  scanf("%d %d", &arr, &input);
  int box[arr];
  int tmp_box[arr];

  for (int m = 0; m < arr; m++)
  {
    box[m] = m + 1;
  }

  for (int m = 0; m < input; m++)
  {
    scanf("%d %d", &i, &j);
    while (i < j)
    {
      tmp = box[i-1];
      box[i-1] = box[j-1];
      box[j-1] = tmp;

      i++;
      j--;
    }
  }

  for (int m = 0; m < arr; m++)
  {
    printf("%d ", box[m]);
  }
}