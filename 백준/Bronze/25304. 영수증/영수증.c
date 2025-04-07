#include <stdio.h>
int main(){
    int total, num, price, cnt, sum=0;
    scanf("%d", &total);
    scanf("%d", &cnt);
    for(int i=0; i<cnt ; i++){
        scanf("%d %d", &price, &num);
        sum += price * num;
    }
    
    if(total == sum){
        printf("Yes\n");
    }
    else{
        printf("No\n");
    }
}