#include <stdio.h>
int main() {
    int array, num;
    scanf("%d %d", &array, &num);
    
    int arr[array];
    
    for(int i=0 ; i<array ; i++){
        scanf("%d", &arr[i]);
    }
    
    for(int i=0 ; i<array ; i++){
        if(num > arr[i]){
            printf("%d ", arr[i]);
        }
    }
}