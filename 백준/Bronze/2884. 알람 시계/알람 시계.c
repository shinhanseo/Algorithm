#include <stdio.h>
int main(){
    int hour, min;
    int ch_hour, ch_min;
    
    scanf("%d %d", &hour, &min);
    
    
    if(min < 45){
        ch_min = min - 45 + 60;
        if(hour==0){
            ch_hour = 23;
        }
        else{    
            ch_hour = hour - 1;
        }    
    }
    else{
        ch_hour = hour;
        ch_min = min - 45;
    }
    
    printf("%d %d\n", ch_hour, ch_min);
    
    return 0;
}