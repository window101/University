<어셈블리어>

Mov 레지스터이름, 값 : 해당 레지스터에 값이 넣어진다.
Mov reg, reg : 레지스터 안의 값을 다른 레지스터안에 값에 넣는다.

<레지스터>
EAX(4바이트) 공간중 2바이트 공간 중에서 높은 공간을 AH, 낮은 공간을 AL이라고 한다 (역사적인 이유)
나머지 공간까지 쓴다 그러면 EAX 라고 한다.
                                      (낮은 자리 2바이트 : AX)
                   O   ||    O     ||     AH    || AL

범용 레지스터  중 하위 2바이트는 각각 AX(AH+AL), BX(BH+DL), CX(CH+CL), DX(DH+DL)
1) EAX 
2) EBX
3) ECX
4) EDX

<mov 연산>
Mov [402000], al(al레지스터 값)
Move [402000], [402001] 은 안되고 레지스터에 값을 옮긴 다음에 메모리에 복사해야 된다.

DWORD             : 4 바이트
WORD		ptr	:2 바이트
BYTE			:1 바이트

Ex) MOV DWORD PTR DS:[402000],EAX  : [402000]부터 4바이트 공간을 이용하겠다
 Mov word ptr ds:[402000], EAX : 앞 뒤 크기가 달라서 안된다

-NOP : 만나면 CPU가 PASS 한다



<jmp> : jmp 401000 ->401000으로 점프해라
JMP SHORT 00401005 -> 현재주소가 0040100F인데 점프하는 00401005까지의 거리가 짧아서 SHORT형태로 작업하는 기계어 EB가 쓰인다.e
JMP를 실행하는 해당 EIP의 주소 값(ex. 0040100F) 이랑 jmp 하는 위치 (ex.00401005)를 빼서 eip에 더해주는 방식으로 jmp 한다

-RAM 에서 EIP의 주소를 읽어온 다음 해당 주소에 있는 기계어 데이터를 읽어온다.
-그리고, 읽어온 바이트만큼 EIP의 주소를 증가시킨다.

<inc, dec>
증가 명령어 : inc + register / memory
감소 명령어 : dec + register / memory

Ex) inc eax : eax값이 1 증가한다

<add, sub>
Add : C언어로 따지만 += 과 같다.


<조건 분기  명령어>
-	JZ 주소 : 이것의  했던 명령의 결과가 0가 되면 jump ( 상태 레지스터 Z가 0이 되면)
-	JE 주소 : (Jump if equal)
-	JNE (N:not)
-	JA, JB
-	JNA : JA의 반대(a<=b)
-	JNB : JB의 반대 (a>=b)
-	JAE (a >=b)      : JBE와 JAE는 이제 Z가 1인지 본다(equal인지)
-	JBE ( a<=b)
Com eax, 0 : 결과값이 0키면 Z(zero flag)에 1을 세팅한다.
-mov eax, 1
Com eax, 2 : com는 내부적으로 빼기  처럼 작동한다. Carray비트 1로 설정됨
Jb 401000F : com 명령어에서 앞이 뒤보다 작으면 점프 (below)
->carry 1로 되어야 점프
Ja 401000F : com 명령어에서 앞이 뒤보다 크면 점프 (above)
->carray 0 && zero 0 이어야 점프


*캐리 vs 오버플로우 서칭하기

<부호가 있는 데이터로 표현하고 비교하는 jmp 연산자>
-	JG : a > b && sign flag == overflow flag && z == 0
-	JL

<플래그 P, A>
1) P : 패리티 비트
-odd parity : 패리티 까지 합쳐서 1의 비트의 개수를 홀 수로 유지
-even parity : 패티리 까지 합쳐서 1의 비트의 개수를 짝 수로 유지

2) A : 보조 캐리 플래그


<adc, sbb>
1) adc : 8바이트 끼리 더할 때,
하위 4바이트를 먼저 더해주는데 올림이 발생하면 상위 4비트 끼리 더할 때 adc로 더해서 올림 처리를 해준다. 


-리눅스에서 vi로 작성한다음에 g++ vi이름 -S 하면 어셈블리코드 볼 수 있다
