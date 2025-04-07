#include <stdio.h>
int main()
{
  int array, min, max;
  scanf("%d", &array);
  int arr[array];

  for (int i = 0 ; i < array ; i++)
  {
    scanf("%d", &arr[i]);
  }

  min = arr[0];
  max = arr[0];

  for (int j = 1 ; j < array ; j++)
  {
    if (arr[j] > max)
      max = arr[j];
    if (arr[j] < min)
      min = arr[j];
  }
    
  printf("%d %d", min, max);  
}