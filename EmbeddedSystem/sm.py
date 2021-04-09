<3주차>

반도체 : 규소에 불순물을 집어 넣으면서 전기적인 성질을 가지게 됨
전자 : - 특성을 갖는 물질

p-type 반도체 : + 전하의 성질을 가지는 반도체 ( + 이기 때문에 Positive type )
=>B(분소) + SI(실리콘)
n-type 반도체 : - 전하의 성질을 가지는 반도체  ( - 이기 때문에 Negative type )
=>AS(비소) + SI(실리콘)

<p type 과 n type을 합친 경우>

-p-type에 + 전기를 가하고 n-type에 – 전기를 가하고 붙여보면 p-type에서 n-type으로 전기가 흐른다
-p-type에 - 전기를 가하고 n-type에 + 전기를 가하고 붙여보면 p-type에서 n-type으로 전기가 흐르지 않는다  (절연체의 설징)
(즉, 다이오드 : 전기가 한쪽 방향으로 흐르게 됨)


트랜지스터 : Gate, Source, Drain 라는 단자가 있는데 Gate에 전기(+,-)에 가하는 것에 따라 source, drain 쪽으로 신호가 흘러갈 수도 있고 단절이 될 수도 있는 것
(신호가 들어가는 쪽과 나가는 쪽인 source, drain 은 정해져 있고, source drain 사이에 전기가 흐르는지 차단되는지 Gate라는 것이 중간에 스위치같은 역할을 해준다) 

<nMOS 트랜지스터>

-Sio2 : 실리콘 디옥사이드
-Polysilicon
-강의 자료 그림 보기
-p-type 바디위에 n-type source, drain 이 있으면 nMOS(negative) 트랜지스터다
-p-type을 그라운드로 접지를 시킨다. p-type과 n-type이 물려있으면 다이오드의 특성을 갖는다. p-type에 VDD를 가해주고 n-type에 -를 가해주면 p에서 n으로 전기가 흐른다.
따라서 이를 방지하기 위해 p-type을 그라운드에 접지시켜야 한다.
(p-type과 n-type에 전기가 흐를 수 없게 한다)
-p-type과 그라운드(-)로 되어있고 Gate 부분에도 그라운드(-)를 연결을 한다면 전기적 변화가 발생하지 않는다 . Source와 drain 사이도 연결이 되지 않는다
-따라서 nMOS는 전기가 흐르지않는, 스위치가 OFF된 상태다
-p body에 -를 입력하고 Gate에 +를 입력으로 해준다면, siO2 밑에 n+(Source), n+(Drain) 사이 바닥에 네모난 층(채녈)을 형성하면서 모이게 된다


<pMOS 트랜지스터>
-nMOS 트랜지스터와는 반대다 (p-type과 n-type의 위치 )
-n-type body가 +로 접지가 되어있다.
-만약에 n-type body가 +인데 Gate 부분에 +가 가해지면 아무런 상태가 발생하지 않는(off 상태)가 된다. 반대로 Gate에 – (그라운드)가 가해지면 n-type 상부에 + 전하가 위로 올라가서 채널을 형성한다 =>전류흐름(ON 상태)

-Vdd전압이 높으면 트랜지스터에 damage가 간다. 따라서 요즘은 회로 집적도가 높아짐에 따라 Vdd 전압이 낮아지고 있다


<CMOS 회로>
-하단부는 nMOS 트랜지스터로 구성하고 상단부는 pMOS 트랜지스터로 구성한다
-하단부와 상단부는 항상 논리적으로 반대의 상태를 가진다
-CMOS 구조의 회로는 출력신호가 항상 Strong 1 아니면 Strong 0으로 나가게 된다
-안정적인 strong1, strong0을 보장하기 위해 상단, 하단의 반대되는 로직을 구성하고 좀 더 많은 트랜지스터가 들어가게 된다  
-만약에 하단부에 직렬로 구성되어 있다면 반드시 상단부는 병렬로 구성되어야 함(상황 반대도 가능)

강의 자료에 CMOS NAND Gate에서 아래쪽은 직렬이고 위쪽은 병렬이다
병렬은 하나가 OFF가 되어도 전류가 흐르지만, 직렬은 하나가 OFF가 되면 전류가 흐르지 않는다
따라서, 아래쪽(하단부분)은 전류가 흐르지 않는다
=>강력한 1의 신호가 나간다
=>CMOS 회로는 항상 위 아래가 ON, OFF로 반드시 반대가 되어야 한다

CMOS NOR Gate
=>NOR 은 NAND 와 논리적으로 반대이다. 따라서 NAND를 반대로 해주면 된다



<베릴로그 3주차>

<수 표현>

1) 기본형태
-<크기> '<기본 형식> <숫자> 형식을 갖는다
ex) 4'b1111 // 4비트 2진수 '1111'
12'habc // 12비트 16진수 'abc'
16'd255 // 16비트 10진수 '255'

2) 크기 지정이 안된 수
-<기본 형식>을 지정하지 않은 숫자는 10진수
-<크기>를 지정하지 않은 숫자는 시뮬레이터나 기계마다 다른 기본 값을 갖는다(최소한 32비트)
ex)
23456 // 32비트 10진수 '23456'
'hc3 // 32비트 16진수 'c3'
'o21 // 32비트 8진수 '21'

3) x, z값
-Unknown Value : 'x'
ex)
12'h13x  // 12비트 16진수 '13x'; 하위4비트는 알 수 없는 값이다
6'hx  // 6비트 16진수 'x' 

-High Impedance : 'z'
ex)
32'bz  // 32비트 2진수 'zzzz....zzzz' ; 'z'값으로 32비트가 채워진다

4) 음수 표현
-<크기> 앞에 ' - ' 부호만 붙이면 된다
-부호와 상관 없이 <크기>는 양의 값만 갖는다
ex)
-6'd3  // 6비트 10진수 3의 2's complement로써 음수
4'd-2  // 불법적인 표현
 

5) 수 표현
-언더스코어 문자와 물음표
ex)
12'b1111_0000_1010  // 가독성 증가
4'b10??  // 4비트 2진수 '10zz' or '10xx' 와 같다

6) 문자열
-문자열은 일련의 1-바이트 아스키값으로 다루어진다
ex)
"Hello Verilog World" // 문자열
"a / b " // 문자열

<식별자와 키워드>
1) 식별자 (Identifiers)
-객체에 주어진 이름
-대소문자 구별, 알파벳, 숫자, 언더스코어( _ ), 달러기호($)로 구성
-언더스코어나 알파벳으로 시작 할 수 있고, 숫자나 달러기호로 시작될 수 없다
($ 기호가 맨 처음 나오는 것은 시스템 태스크에 예약 되어있다)

ex)
reg value;  // reg는 키워드, value는 식별자
input clk;  // input는 키워드, clk는 식별자

2) 이스케이프 식별자
-백슬래쉬(\) 문자로 시작하고, 백슬래쉬와 화이트 스페이스 사이에 있는 문자는 문자로 처리
ex)
\a+b-c
\**my_name**

<논리값>
0 : 논리적 '0', 거짓 상태
1 : 논리적 '1', 참 상태
x : 알 수 없는 논리값
z : 하이 임피던스, 플로팅 상태


<데이터 형>

-신호강도 	형		정도
supply		흐름		가장 강도가 높음
strong 		흐름		
pull		흐름		
large		저장
weak 		흐름
medium	저장
small		저장
highz		하이 임피던스		가장 강도가 낮음


2) 넷 (Nets) => wire 타입
 

wire a; // 옆 회로에서 넷 a를 정의
wire b, c; // 옆 회로에서 넷 b,c를 정의
wire d = 1'b0; // 넷 d는 논리값 '0'으로 선언

-넷은 하드웨어 요소 사이에 연결을 나타낸다
-키워드 wire에 의해 정의, 기본 값은 'z' 이다
-넷은 하드웨어 요소에서 유도된 출력 값을 갖게 되고, 유도된 값이 없다면 기본값 'z' 를 가진다
-넷 a는 g1에 의해 생성된 출력 b&c를 연속적으로 갖게 된다


3) 레지스터 => reg 타입
-다른 논리값이 들어오기 전까지 그 값을 유지
-단지 값을 저장할 수 있는 변수
-실제 회로에서의 레지스터 와는 다른 개념이고 키워드 reg로 선언되며 기본 논리값은 'z' 이다



<CMOS 반도체 공정>

Fist step will be to form the n-well  (n-type 우물을 먼저 만든다)

1) p type substrate(wafer) 위에 실리콘 디옥사이드(SiO2 Oxide) 층을 입힌다
-디옥사이드 층을 입히기 위해 p type substrate 층을 900도 에서 굽는다 (H2O, O2를 집어넣는다)
-위 과정을 하게되면 실리콘과 산소가 결합해서 디옥사이드(SiO2 Oxide) 층이 생기게 된다

2) Photoresist Process
-실리콘 디옥사이드(SiO2 Oxide)를 입힌 층 위에다가 n type 우물 형태를 만들기 위해 우선Photoresist 라는 물질을 입힌다
-Photoresist 라는 물질을 입히고 난 후 골고루 펴지게 하려고 회전을 시킨다

3) Lithography Process
-n type 우물의 형상태로 Photoresist 위에 빛을 쪼이면 해당 빛을 받은 Photoresist가 말랑말랑 해지는데 해당 부분을 긁는다
-실리콘 디옥사이드(SiO2 Oxide) 위에 Photoresist가 네모낳게 뚫리면 실리콘 디옥사이드(SiO2 Oxide) 층도 네모낳게 뚫기 위해 HF 라는 용액을 사용해서 뚫는다 (SiO2 층만 녹이는 설징을 가진 용액임)
=> 이 녹이는 과정을 에칭(Etching) 과정이라고 한다

4) Strip Photoresist
-실리콘 디옥사이드(SiO2 Oxide) 층을 네모낳게 뚫었으면 위에 덮고 있는 Photoresist 층을 제거한다
-피라냐 에치(piranah etch) 용액을 써서 Photoresist 층을 녹인다
-이 과정까지 하면 p type substrate 위에 네모낳게 뚫린 실리콘 디옥사이드(SiO2 Oxide) 층만 남는다

5) n-well
-네모낳게 뚫려있는 실리콘 디옥사이드(SiO2 Oxide) 층 밑에 실질적으로 n type 반도체 물질을 침투시켜야 하는데 두 가지 방법이 있다
*Diffusion 방식 : 
-전통적인 방식이고, n type 물질인 비소(AS)가스를 잔뜩 집어넣고 가열한다
-그러나, 정확한 사각형형태로 만들어 지지 않아서 Implant 방식으로 바꾸게 된다
*Ion Implant 방식 :
-용액대신 비소(AS) 빔을 위에서 쏘는 방식이다 

=> 오늘날은 Ion Implant 방식을 사용하지만, n type well 방식을 만드는 방식을 Diffusion 방식으로 부른다 (실질적으로 Ion Implant 방식이지만 이렇게 부른다는 의미임)
6) Strip Oxide
-n type well을 만들었으니 위에 씌워져 있는 실리콘 디옥사이드(SiO2 Oxide) 층을 제거한다
-HF 용액을 사용하여 제거한다

7) Polysilicon
-얇은 실리콘 디옥사이드(SiO2 Oxide) 층을 만든다
-그 위에 Polysilicon 이라는 CVD 층을 만들기 위해서 Silane gas(SiH4)가 있는 곳에 집어넣는다

8) Polysilicon Patterning
-Polysilicon 이 위에서 보았을 때, 'ㄷ' 자가 되게 하기 위해 Lithography process를 거친다 
-이러게 하면 비로소 gate 부분이 완성된다

9) Self-Aligned Process
-Source 와 Drain 부분을 만들기 위해 구멍을 뚫는 과정이다

10) N-diffusion cont.
-Source와 drain의 밑에도 n type 반도체 물질을 집어 넣는다
-n type 물질이 들어간 diffusion 영역이 만들어지고 나면, 위에 덮혀있던 실리콘 디옥사이드(SiO2 Oxide) 를 HF 용액을 사용해서 제거한다 

11) P-diffusion
-p type 물질도 집어넣기 위해 9번 과정인 Self-Aligned process ~ 10번을 동일하게 진행한다

12) Contacts
-여기까지 하면 nMos 트랜지스터와 pMos 트랜지스터 들이 만들어 진다
-Vdd 와 ground 를 연결시켜 주기 위해서 SiO2 Oxide 층을 만들어서 메탈 부와 아래쪽이 연결될 수직인 공간을 남겨준다

13) Metalization
-뜨거운 알루미늄의 용액을 위에서 붓는다

=>여기까지 하면 최종적인 Inverter의 레이아웃 형태가 된다

10나노 공정이란 source 와 drain 사이의 두께인 gate의 크기가 10 나노 라는 크기이다






<베릴로그 4주차>

4) 벡터 
-넷(wire)과 reg 데이터형은 벡터(여러 비트폭을 가진)로 선언 될 수 있다
-비트폭을 선언하지 않으면 기본 값은 스칼라(1비트) 이다.
ex) wire a; // 스칼라 넷 변수, 기본값(1비트)
wire [7:0] bus // 8비트 버스
wire[31:0] busA, busB, busC // 32 비트 버스 3개
reg clock // 스칼라 레지스터. 기본값

-벡터는 [ 높은 수 : 낮은 수 ] 또는 [ 낮은 수 : 높은 수 ]로 나타낸다
-그러나 항상 왼쪽에 있는 것이 최상위 비트를 나타내낟
-busA[7] : 벡터 busA의 7번째 비트
-bus[2:0] // 2부터 0 까지의 3비트

5) 정수, 실수, 시간, 레지스터 데이터형
정수 : integar
실수 : real
시간 : time

6) 배열
-reg, integer, time 벡터 레지스터형의 배열을 제공, 실수 변수의 배열은 제공하지 않는다
ex) integer count[0 : 7]
reg bool [31 : 0] // 32 1 비트 boolean 레지스터 변수의 배열
reg [4 : 0] port_id [0 : 7] // 8 port_id의 배열, 각 포트는 5비트 폭을 가진다
integer matrix[4 : 0][4 : 0] // 다차원 배열
time chk_point[1 : 100]  // 100 time checkpoint 변수 배열

7) 메모리
-메모리의 모델링은 레지스터의 배열로 만들어진다
ex) reg mem1bit[0 : 1023] // 메모리 mem1bit는 1K 1비트 워드
reg [7 : 0] membyte [0:1023] // 메모리 membyte는 1K 8비트 워드

8) 파라미터
-parameter로 선언하고, 상수를 정의 할 수 있다


9) 문자열
-문자열은 reg에 저장 될 수 있다

시스템 태스크
-모든 시스템 태스크는 $<키워드> 형태로 나타낸다. 화면에 출력, 넷의 값 모니터링 등

1) 화면 출력 테스크( $display) => printf 와 비슷하다
ex) $display(p1, p2, p3, ... pn)

2) 모니터링 태스크( $monitor)
ex) $monitor(p1, p2, p3, ..pn)
=>변수 또는 파라미터에 지정된 신호의 값이 변할 때 마다 그 신호를 출력
=>한번 선언을 해주면 해당 변수 값이 변할 때 마다 모니터가 실행됨
ex) 
initial
begin
	$monitor($time, "value of signals clock = %b reset = %b", clock, reset);
end
	
컴파일러 지시어
1) $stop : 시물레이션 중단 => 신호의 값을 조사 하고자 할 때마다 사용가능하다
2) $finish : 시뮬레이션을 끝낸다
3) `define : 텍스트 매크로를 정의 하는데 사용한다
ex) `define WORD_SIZE 32
   `define S $stop
4) `include => C언어의 #include










ASICs
-IC는 크게 표준(범용)IC와 ASIC으로 분류

ASICs의 종류
1) standard cell design
2) gate array design
3) full-custom design
4) PLD(programmable logic device)
-FPGA
-CPLD

FPGA
1) CLB block: 바둑판처럼 Mesh 구조로 깔려있다
-데이터를 저장할 수 있는 sRam, Sequential logic을 구현하기 위한 Filp flop이 있다
2) Programmable Interconnect : CLB block 사이를 wire로 연결시켜주는 형태
3) Input Output Blocks(IOB) : 입출력 포트

standard cell-based design
-셀 라이브러리에 포함되어 있는 정보
-Inverter, NAND 게이터 같은 셀들은 모두 일정한 높이를 가진다. 실제 회로를 구성할 때, 이미 만들어서 제공하는 셀 라이브러리에서 적당한 셀들이 선택이 되고 Wire 들이 적절히 구성된다 (회로구성)

gate array design -> PLD와 비슷한 디자인이다

full-custom design
-standard cell-based design은 다른 사람이 만들어놓은 셀들을 선택하는 반면에, full-custom design은 자신이 셀들 하나하나를 만드는 방식이다 (좀 더 세부적으로 고성능을 위해 일일히 셀을 다시 만듬)
즉, 표준화된 Cell library를 사용하지 않고 모든 회로를 설계자가 디자인 하는 방법을 말한다

ASIC 회로 설계 비교
		gate array		standard cell		full cursion
complexity	medium		medium to high	high to very high
spped		moderate		fast			fast
develop cost	moderate		high			high



포트 : 모듈이 외부 환경과 소통 할 수 있는 인터페이스
즉, 모듈이 다른 모듈 또는 외부 환경과 소통 할 수 있게 해준다

1) 포트 나열 ex)
module fulladder4 (sum, c_out, a, b, c_in) // 포트 리스트를 가진다
=>보통 출력부를 앞에 써준다 (sum, c_out). 입력부를 뒤에 쓴다 (a, b, c_in)

module Top; // 포트리스트가 없다, 테스트 하고자 하는 모듈은 외부 입출력이 없으므로 포트리스트X

2) 포트 선언
Verilog 키워드		포트의 형
-input			입력 포트
-output			출력 포트
-inout			양방향 포트

ex)
module fulladd4(sum, c_out, a, b, c_in);  // 4비트 fulladder 라면

output [3:0] sum; // 출력 4비트
output c_out;

input [3:0] a, b; // 입력 4비트
input c_in;
endmodule

-모듈 내부에서 input, inout, output 포트는 wire(net) 형태로 하던지, output 포트만 wire(net), reg 타입으로 할 수가 있다
-모듈 외부에서 inout, output 포트는 wire(net) 형태로 해야하고, input 포트는 wire(net), reg 타입으로 할 수가 있다







외부 신호에 포트 연결하기

module Top;

// 연결 변수의 선언
reg [3 : 0] A, B;
reg C_IN;
wire [3 : 0] SUM; => reg 변수로 선언하면 안된다 
wire C_OUT;

연결 방법 1번 fulladd4 fa0(SUM, C_OUT, A, B, C_IN);
// fulladd4 모듈에서 출력 포트 sum이 Top 모듈에서 레지스터 변수 SUM에 연결되어 있으면 불법적인 연결이다

연결 방법 2번 fulladd4 fa_byname( .c_out(C_OUT), .sum(SUM), .b(B), .c_in(C_in), .a(A));
// fulladd4에 파생시킨 모듈의 원래 포트이름을 . 하고 써주고 괄호(연결신호) 형식으로도 연결 가능
...
endmodule

gate 수준 설계 , 데이터 플로우 설계, 행위적 수준 설계와 같이 3가지의 설계가 있다

<Gate 수준의 회로 설계>
1) AND/OR 게이트
-하나의 스칼라 출력과 여러 개의 스칼라 입력이 있다

ex)
//인스턴스 이름이 존재하는 게이트
and a1 (OUT, IN1, IN2)
nand na1 (OUT, INT1, IN2)

//인스턴스 이름이 없는 게이트 파생
and (OUT, IN1, IN2)



< IP >

Design Reuse : 이전 설계에 들어간 것이 재사용 된다
-SOC의 복잡도가 계속 증가하고 , NRE(초기비용)이 엄청나기 때문이다

IP reuse : Reuse of the verified components. Do not invent the wheels! 라는 의미
(IP : '기존에 설계된 것' 이라는 의미)

Condition of IP
1) Usability
-Designed for the general purpose reuse
2) Documentation
-Quality documentation about the applications and limitations (주석과 같은 느낌)
3) Coding Quality
-Coding Guideline
4) Verification Environment
-High level of verification coverage
5) Well-known IP provider
-Technical support

IP Classification
1) Soft IP : 베릴로그 코드로 받아오는 것
-특정 공정(technology)와 무관하게 소프트웨어적으로 사용할 수 있음 (베릴로그 코드니까)
-Portability(이식성)이 좋다
2) Firm IP : 
-합성한 것을 게이트 수준의 회로도로 제공 ( Soft IP와 Hard IP의 중간단계임 )
3) Hard IP : 최종 레이아웃 형태로 받아오는 것
-특정 공정(technology)에 유관하게 사용해야 한다 (아날로그 회로니까)
-technology dependent 







IP Design Flow
1) Planning : 계획단계
-Documentation이 중요하다

2) Design Guideline
-System 레벨 : 
-Module 레벨 : System 레벨보단 낮은 단계이다
=> 이 두개 또한 Documentation(문서화)를 잘 해야한다

3) Algorithm / Architecture analysis
-High level design
-Detailed level design
=> 이 두개 또한 Documentation(문서화)를 잘 해야한다
=> 코딩하기 전에 블록도를 그리고 아주 세밀하게 디자인 하는 과정임 

4) Code Development
-먼저 Architecture C modeling을 하고 Verilog Code 로 코드를 짠다

5) Verification
-Unit test( 작은 블럭 테스트) -> Integration test ( 더 큰 Unit을 테스트 )
-FPGA Validation (칩에다가 전체 회로, 코드를 다운받아서 전체 검증)


Verilog 6주차
