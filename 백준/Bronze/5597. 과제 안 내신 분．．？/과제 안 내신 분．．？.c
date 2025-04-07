#include <stdio.h>
int main()
{
  int stu[28], list[30] = {0};
  for (int i = 0; i < 28; i++)
  {
    scanf("%d", &stu[i]);
    list[stu[i] - 1] = 1;
  }

  for (int i = 0; i < 30; i++)
  {
    if (list[i] == 0)
    {
      printf("%d\n", i + 1);
    }
  }
}