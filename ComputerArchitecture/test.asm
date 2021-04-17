
la r0, B
la r1, C
add r2, r0, r1
st r2, A
la r3, D
la r4, E
add r5, r4, r3
la r0, C
st r5, A
stop
.org 1000
A:     .dw 1
B:     .equ -10
C:     .equ 14
D:     .equ 14
E:     .equ 18
F:	.dw 1
