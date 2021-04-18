
// 1.c 와 다르게 부호만 다르게 했다

#include <stdio.h>

int main() {
   for (int i = 1; i <= 7; i++) {
      int sum = 0;
      sum += i;
      for (int j = 1; j <= i * 2; j++) {
         sum += j;
         for (int w = 1; w <= j * 2; w++) {
            sum += w;
         }
      }
      printf("sum : %d", sum);
      printf("\n");
   }
}


.org 3000
la r1, 0
la r2, 0
la r3, 0
la r4, 0
la r5, 0
la r6, 0
la r25, 0
la r26, 1000

la r28, outerloop
la r29, inerloop
la r30, innerloop

outerloop: addi r1, r1, 1
la r2, 0
la r25, 0
add r25, r25, r1

inerloop: addi r2, r2, 1
la r3, 0
add r25, r25, r2

innerloop: addi r3, r3, 1
add r25, r25, r3

la r6, C
neg r6, r6
add r6, r6, r3
brnz r30, r6

la r5, B
neg r5, r5
add r5, r5, r2
brnz r29, r5

st r25, 0(r26)
addi r26, r26, 4

la r4, A
neg r4, r4
add r4, r4, r1
brnz r28, r4


.org 1000
A:       .equ 7
B:       .equ 6
C:       .equ 5
