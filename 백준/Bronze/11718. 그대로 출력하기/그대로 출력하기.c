#include <stdio.h>
int main() {
    char a[101];

    while(gets(a) != NULL) { //gets함수는 char 포인터를 반환, 
        printf("%s\n", a);   //만일 파일의 끝에 도달해 입력을 받지 못했다면 NULL을 반환할 것.
    }

    return 0;
}