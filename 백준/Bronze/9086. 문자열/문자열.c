#include <stdio.h>
#include <string.h>
int main()
{
  int num;
  char s[101];
  scanf("%d", &num);
  for(int i=0 ; i<num ; i++){
      scanf(" %s", s);
      printf("%c%c\n", s[0], s[strlen(s)-1]);
  }
      
}