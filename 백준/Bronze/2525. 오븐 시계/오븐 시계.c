#include <stdio.h>
int main()
{
  int hour, min, time;
  scanf("%d %d", &hour, &min);
  scanf("%d", &time);

  if ((min + time) > 60)
  {
    hour += (min + time) / 60;
    min = (min + time) % 60;
    if (hour > 23)
    {
      hour -= 24;
    }
  }

  else
  {
    min += time;
    if (min > 59)
    {
      hour++;
      if (hour > 23)
      {
        hour -= 24;
      }
      min -= 60;
    }
  }

  printf("%d %d\n", hour, min);

  return 0;
}