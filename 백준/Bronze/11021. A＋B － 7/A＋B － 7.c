#include <stdio.h>
int main() {
    int cnt, num1, num2;
    scanf("%d", &cnt);
    for(int i=1 ; i<=cnt ; i++){
        scanf("%d %d", &num1, &num2);
        printf("Case #%d: %d\n", i, num1+num2);
    }
}