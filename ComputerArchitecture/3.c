
컴퓨터 구조 중간고사
[3] [배점 10점] 1부터 9개의 Fibonacci 수(1, 1, 2, 3, 5, 8, 13,
21, 34)를 메모리 십진 1000번지부터 계산하여 넣는 프로그램을
작성하시오. Fibonacci 수는 첫 두 수가 1과 1이고 다음 수부터
는 그 이전 두 수의 합인 수임. 주어진 fib_example.asm에 “아래 
부분을 채우시오” 하는 부분이 있는데 그곳만 반드시 주석(;로 시
작하는 부분)이 요구하는대로 채우면 됨. 주석은 지우지 말고 주
석문 앞을 코드로 채우시오. 첫 두 수인 1과 1은 이미 메모리에
들어가도록 프로그램되어 있으며 채워야할 아래 부분에서는 반드
시 메모리에 있는 두 수를 가져다가 연산을 하고 그 결과를 다시
메모리에 넣어야 함.



<정답>

;
; STORE 9 CONSECUTIVE FIBONACCI NUMBERS IN DESIGNATED
; MEMORY LOCATIONS
; 1, 1, 2, 3, 5, 8, 13, 21, 35
;
.org 1000
x: .dw 9  ; reserve space for fibonacci numbers
.org 5000
la r0, 1  ; first fib number
la r1, 0  ; displacement for fib[i]
la r2, 4  ; displacement for fib[i+1]
st r0, x(r1)  ; store first fib number
st r0, x(r2)  ; store second fib number
la r3, 6  ; initialize counter. generate 7 more fib numbers
lar r31, loop  ; save loop address



loop: ld r4, x(r1)  ; retrieve fib[i] from memory
  ld r0, x(r2); retrieve fib[i+1] from memory
  add r0, r0, r4; compute fib[i+2]
  addi r1, r1, 4; adjust r1 to point to next fib[i]
  addi r2, r2, 4; adjust r2 to point to next fib[i+1]
  st r0, x(r2); store fib[i+2]
  addi r3, r3, -1; decrement counter
  brpl r31, r3; branch to loop and repeat 7 times

stop







