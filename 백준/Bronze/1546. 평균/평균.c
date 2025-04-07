#include <stdio.h>
int main()
{
  int num;
  float avg, sum = 0.0, max = 0.0;

  scanf("%d", &num);
  float grade[num];
  float new_grade[num];

  for (int i = 0; i < num; i++)
  {
    scanf("%f", &grade[i]);
    if (max < grade[i])
      max = grade[i];
  }

  for (int i = 0; i < num; i++)
  {

    new_grade[i] = (grade[i] / max) * 100;
    sum += new_grade[i];
  }

  avg = sum / num;

  printf("%f", avg);
}