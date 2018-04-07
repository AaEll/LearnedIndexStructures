// Initilization
#include <stdio.h>
#include <stdlib.h>
#include <setjmp.h>
#define MAXINT 2147483647
// #define RAND_MAX MAXINT
#define TRY do{ jmp_buf ex_buf__; if( !setjmp(ex_buf__) ){
#define CATCH } else {
#define ETRY } }while(0)
#define THROW longjmp(ex_buf__, 1)
#define mem_size 8
typedef int bool;
#define true 1
#define false 0


void monte_carlo(long long num_data, int buffersize, int batch_size) {
  char *start_pos = NULL;
  FILE *fptr;
  int i = 4;
  bool T = true;
  while (T){
    batch_size = (mem_size/i) - (mem_size/i)%(sizeof(int)+buffersize);
    TRY {
      start_pos = malloc(batch_size);
      T = false;
    }
    CATCH {
      i = 2*i;
    }
    ETRY;
  }
  char *pointer = start_pos;
  long long a;
  for (a=0; a<batch_size/(sizeof(int)+buffersize) && a<num_data; a++) {
    int j = rand() % MAXINT;
    pointer = j;
    pointer = pointer+sizeof(int)+buffersize;
  }
  num_data = &num_data - a;
  //push start_pos to start_pos+batch_size to disk
  //fptr = fopen("")
  free(start_pos);
}
int main(int argc, char **argv)
{
   long long num_data = argv[1];
   while (num_data>0){
      monte_carlo(num_data,argv[2],argv[3]);
   }
   return 0;
}
