#include <stdio.h>

int paper[100][100] = {0}; // 도화지 (초기화)

int main() {
    int num, x, y, area = 0;
    scanf("%d", &num);

    // 색종이 붙이기
    for (int i = 0; i < num; i++) {
        scanf("%d %d", &x, &y);
        for (int j = x; j < x + 10; j++) {      // x 범위
            for (int k = y; k < y + 10; k++) {  // y 범위
                paper[j][k] = 1; // 색종이가 붙은 부분을 1로 표시
            }
        }
    }

    // 검은색 영역 계산
    for (int i = 0; i < 100; i++) {
        for (int j = 0; j < 100; j++) {
            if (paper[i][j] == 1) {
                area++;
            }
        }
    }

    printf("%d\n", area);
    return 0;
}
