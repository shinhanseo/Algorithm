#include <stdio.h>
#include <string.h> // strcmp 사용

int main()
{
  float grade[20], num, total = 0.0, total_grade = 0.0;
  char sub[20][100], score[20][3]; // score를 2차원 배열로 변경
  int p = 0;

  for (int i = 0; i < 20; i++)
  {
    scanf("%s %f %s", sub[i], &grade[i], score[i]);

    // "P" 등급 과목은 계산에서 제외
    if (strcmp(score[i], "P") != 0)
      total_grade += grade[i];
  }

  for (int i = 0; i < 20; i++)
  {
    // "P" 등급 과목은 계산에서 제외
    if (strcmp(score[i], "P") == 0)
      continue;

    if (strcmp(score[i], "A+") == 0)
      num = 4.5;
    else if (strcmp(score[i], "A0") == 0)
      num = 4.0;
    else if (strcmp(score[i], "B+") == 0)
      num = 3.5;
    else if (strcmp(score[i], "B0") == 0)
      num = 3.0;
    else if (strcmp(score[i], "C+") == 0)
      num = 2.5;
    else if (strcmp(score[i], "C0") == 0)
      num = 2.0;
    else if (strcmp(score[i], "D+") == 0)
      num = 1.5;
    else if (strcmp(score[i], "D0") == 0)
      num = 1.0;
    else if (strcmp(score[i], "F") == 0)
      num = 0.0;

    total += (grade[i] * num); // 학점 * 평점
  }

  printf("%.6f\n", total / total_grade); // 소수점 6자리까지 출력
  return 0;
}
