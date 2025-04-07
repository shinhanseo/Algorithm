#include <stdio.h>
int main(){
    int number, a, b;
    scanf("%d", &number);
    for(int i=0 ; i<number ; i++){
        scanf("%d %d", &a, &b);
        printf("%d\n", a+b);
    }
    
    return 0;
}