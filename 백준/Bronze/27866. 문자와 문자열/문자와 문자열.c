#include <stdio.h>
int main(){
  char ch[1000];
  int num;
  scanf("%s", ch);
  scanf("%d", &num);

  printf("%c", ch[num-1]);
}