#include <stdio.h>
int main() {
    int a, b;
    int r1, r2, r3, result;
    scanf("%d %d", &a, &b);
    
    r1 = a*(b%10);
    r2 = a*((b%100)/10);
    r3 = a*(b/100);
    result = r1 + 10*r2 +100*r3;
    printf("%d\n", r1);
    printf("%d\n", r2);
    printf("%d\n", r3);
    printf("%d\n", result);
    
    return 0;
}