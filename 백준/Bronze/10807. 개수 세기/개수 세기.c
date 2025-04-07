#include <stdio.h>
int main() {
    int array, find, cnt;
    scanf("%d", &array);
    
    int arr[array];
    for(int i=0 ; i<array ; i++){
        scanf("%d", &arr[i]);
    }
    
    scanf("%d", &find);
    for(int i=0 ; i<array ; i++){
        if(arr[i] == find) cnt++;
    }
    
    printf("%d\n", cnt);
    
    return 0;
    
}