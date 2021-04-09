<개요>
인공 지능 : 인간의 학습능력, 추론능력 등을 컴퓨터를 통해 구현하는 포괄적인 개념
머신 러닝 : 데이터를 이용하여 명시적으로 정의도지 않은 패턴을 학습하여 미래 결과를 예측
-Regression : 연속적인 데이터를 학습하여, 학습된 결과를 바탕으로 미래의 임의의 데이터가 올 경우 예측
-Classification : 데이터의 분포를 학습하여, 학습된 결과를 바탕으로 미래의 임의의 데이터가 올 경우 해당 데이터가 어느 분포에 속하는지 예측
-Neural Network : 인간의 뇌세포인 뉴럴(nucleus) 의 역할 즉, 이전 뉴런 출력을 각각의 입력으로 받아, + 또는 - 가중치를 통해 전체의 합을 합하여 특정 임계치(threshold)를 넘으면 다음 뉴런으로 전달 하는 원리
( * 데이터 마이닝 : 데이터 간의 상관관계나 속성을 찾는 것이 주목적 )
딥 러닝 : 머신러닝의 한 분야로서 신경망(Neural Network)을 통하여 학습하는 알고리즘의 집합
<데이터 타입>
DATA TYPE
1.	list
-리스트 인덱스는 0부터 시작하며, 마이너스(-) 인덱스를 지원한다
(-1 의 인덱스는 마지막 인덱스)
ex) a = [10, 20, 30, 40, 50]
-각 요소의 데이터타입을 다르게 해서 생성 가능, 리스트 안에 또 다른 리스트를 포함 가능
ex) b = [10, 20, "Hello", [True, 3.14] ]
-빈 리스트 생성 후 append method를 사용하여 데이터 추가 가능
ex) c = []; c.append(100);
-콜론(:)을 이용한 '슬라이싱' 기능이 있음. 범위를 지정해 부분 리스트를 얻을 수 있다
ex) a[0:2] ⇒ 인덱스 0 부터 1까지, a[:3] ⇒ 인덱스 처음부터 2까지, a[:]⇒인덱스 처음부터 끝까지
2.	tuple
-리스트와 거의 비슷하나, 리스트 내의 원소를 변경할 수 없다는 차이점이 있다.
ex) a = (10, 20, 30, 40, 50)
3.	dictionary
-키(key)와 값(value)을 한 쌍으로 해서 데이터를 저장함
ex) score = { "Kim":90, "Lee":85, "Jun":95 }
-dictionary는 입력한 순서대로 데이터가 들어가는 것이 아니다
ex) score['Kim'] = 90 으로 데이터 추가 시, print(score)을 하면
{'Kim' : 90, 'Lee' : 85, 'Han':100, 'Jun':95 } 와 같이 데이터가 출력됨을 알 수 있다.
-score.keys() : key 값만 조회, score.values() : value 값만 조회, score.items() : key+value 조회 가능
4.	string
-홀따옴표(''), 쌍따옴표("")를 사용해서 생성
ex) a = 'A73'
-'+' 연산자를 사용하여 문자열 추가 가능
ex) a = a + ', EFG'
-split method를 사용하여 특정 separator를 기준으로 문자열을 분리하여 list 리턴
b = a.split(',');
기타 유용한 함수
1.	type(data) : 입력 data의 데이터 타입을 알려주는 함수
2.	len(data) : 입력 데이터의 길이(요소의 개수)를 알려주는 함수
3.	size(data) : 모든 원소의 개수를 알려주는 함수
4.	list(data) : 입력 data를 리스트로 만들어 리턴 하는 함수
ex) a = ' Hello';
b = { "KIM" : 90, "LEE" : 80 }
print( list(a), list(b.keys()), list(b.values()), list(b.items()) )
// [ 'H', 'e', 'l', 'l', 'o' ] [ 'KIM', 'LEE'] [90, 80] [('KIM', 90), ('LEE', 80) ]
5.	str(data) : 입력되는 data를 문자열로 변환하여 리턴 하는 함수
ex) str ( [1, 2, 3] )
// '[1, 2, 3] '
6.	int(data) : 문자열 형태로 입력되는 숫자나 소수점이 있는 숫자등을 정수로 type casting
<반복문>
1.	range 사용
ex) for data in range(10): for data int range(0, 10) for data in range(0, 10, 2)
print(data, " ", end='') print(data, " ", end='') print(data, "",end='')
// 0 ~ 9 , 0 ~ 9, 0 2 4 6 8
2.	in 사용
ex) list_data = [10, 20, 30, 40, 50] dict_data = { 'key1':1, 'key2' : 2}
for data in list_data : for data int dict_data : ⇒ for key,value in dict_data.items()
print(data, "", end=''); print(data, "", end='');
// 10 20 30 40 50 // key1 key 2 // key 1 1 , key2 2
3.	list comprehension
ex) list_data = [ x **2 for x in range(5) ]
print(list_data) // [ 0, 1, 4, 9, 16 ]
ex) raw_data = [ [ 1, 10], [2, 15], [3, 30], [4, 55] ]
all_data = [ x for x in raw_data ] // [ [ 1, 10], [2, 15], [3, 30], [4, 55] ]
x_data = [ x[0] for x in raw_data] // [ 1, 2, 3, 4 ]
y_data = [ x[1] for x in raw_data ] // [10, 15, 30, 55 ]
<람다>
함수 정의
-def 함수이름 ( 입력1, 입력2, ... ):
-한 개 이상의 return 값을 반환할 수 있음
ex) def multi_ret_func(x) :
return x + 1, x + 2, x + 3
x = 100
y1, y2, y3 = multi_ret_func(x) // 101, 102, 103
-Python 에서는 입력 parameter로 mutable(list, dictionary, numpy) 데이터 형을 넘겨주는 경우 원래의 데이터에 변형이 일어난다.
-반면, immutable(숫자, 문자, tuple 등)은 원래의 데이터에 변형이 일어나지 않음
-람다(lamda) 함수는 def를 사용하지 않고 한 줄로 함수를 작성하는 방법이다 == 익명함수
(수치 미분과 신경망에서 활성화 함수 등을 표현할 때 많이 사용된다)
람다 함수 정의
-함수명 = lambda 입력1 , 입력2, .. : 대체되는 표현식(#define 과 같은 의미)
ex) f = lambda x : x + 100
for i in range (3)
print(f(1)) // 100, 101, 102
<클래스>
-Python 클래스는 class 키워드를 사용하여 자신만의 데이터타입을 만들 수 있음
ex) ⇒C++ 클래스와 비슷하다!
class Person :
count = 0
def __ init __ (self, name) :
self.name = name
Person.count += 1 // Python은 class 내에서 변수를 선언하면 전역 클래스 변수와 비슷한 의미
print(self.name + " is initialized ")
def work(self, company):
print(self.name + " is working in " + company)
def sleep(self)
print(self.name + " is sleeping ")
@classmethod // 반드시 선언해야 함
def getCount(cls): // class method
return cls.count
obj = Person("PARK)
obj.work("ABCDEF")
obj.sleep();
-Python은 기본적으로 모든 멤버가 public 이기 때문에 private로 선언하고 싶다면 __멤버변수, __멤버메서드 형태로 선언해야 함
-__멤버메서드 형태는 public 형태의 멤버메서드를 통해서 호출할 수 있다
-내부 메서드와 외부 메서드의 이름이 동일한 경우, 내부 메서드를 호출하고 싶으면 self.내부메서드 를 사용해야 한다.
<예외처리>
-Python exception은 try ~ except 문을 사용한다
(try 문에서 에러가 발생하면 except 문으로 이동하여 예외 처리 수행한다)
⇒javascript의 try ~ catch ~ finally와 유사
-발생된 exception을 그냥 무시하려면 pass 문을 사용, 에러를 던지기 위해서는 raise 사용
<with 구문>
-Python 에서 with 구문을 사용하면 파일, 세션 close()를 해주지 않아도 자동으로 close() 해줌
(with 블록을 벗어나는 순간 파일 파일이나 세션 등의 리소스를 자동으로 close 시켜준다)
⇒딥러닝 프레임워크인 TensorFlow의 session 사용시 자주 사용된다
ex) with open("./file_test", 'w') as f :
f.write("Hello, Python !!!")
<numpy 라이브러리>
-pip install <라이브러리 이름> 을 통해 라이브러리 설치 가능
사용방법
1.	import numpy
A = numpy.array( [1,2] )
2.	import numpy as np
A = np.array( [1, 2] )
3.	from numpy import exp
result = exp(1)
4.	from numpy import *
result = exp(1) + log(1.7) + sqrt(2)
vector/matrix 생성
-행렬을 나타내기 위해 리스트(list)를 사용할 수도 있지만, numpy를 주로 사용한다
ex) import numpy as np
A = np.array( [ [1, 0], [0, 1] ])
B = np.array( [ [1, 1], [1, 1 ] ])
A + B
-벡터는 np.array( [ ] ) 를 사용하여 생성함
-벡터를 행렬로 변경하거나 행렬을 다른 형상의 행렬로 변경하기 위해서는 reshape() 를 사용하여 행렬의 shape를 변경한다
행렬 곱(dot product)
-np.dot(A,B) 를 통해서 행렬 곱을 수행한다
브로드캐스트(broadcast)
-크기가 다른 두 행렬간에도 사칙연산을 할 수 있다
-차원이 작은 쪽이 큰 쪽의 행 단위로 반복적으로 크기를 맞춘 후에 계산
indexing/slicing
-행렬 원소를 명시적으로 접근하기 위해 리스트(list)처럼 인덱싱/슬라이싱이 가능하다
iterator
-명시적(explicit) 인덱싱/슬라이싱 이외에, 행렬 모든 원소를 access하는 경우 iterator 사용
ex) import numpy as np
A = np.array([ [10,20, 30, 40], [50, 60, 70, 80] ])
it = np.nditer(A, flags=['multi_index'], op_flags=['readwrite'])
while not it.finished:
idx = it.multi_index
print("current value⇒", A[idx])
it.iternext() // iter는 자동으로 증가하지 않기 때문에 while ~ next 구문으로 자주 사용한다
concatenate
-행렬에 행 또는 열을 추가하기 위한 numpy.concatenate
ex) A = np.array([ [10, 20, 30], [40,50,60] ])
row_add = np.array( [70, 80, 90]).reshape(1, 3)
B = np.concatenate( (A, row_add), axis = 0) // axis = 0 : 행 기준, axis = 1 : 열 기준
-위의 예제는 '행' 에 새로운 행을 추가하는 것이고, 새로운 '열'도 추가할 수 있다
loadtxt
-seperator로 구분된 파일에서 데이터를 읽기 위한 numpy.loadtxt(..)
-리턴값을 행렬이다
ex) loaded_data = np.loadtxt('./data-01.csv', delimiter=',', dtype=np.float32)
x_data = loaded_data[ :, 0:-1] // 모든 행이면서 열은 0 ~ -2
기타
-numpy.max(..), numpy.min(..), numpy.argmax(..), numpy.argmin(..)
-numpy.ones([ ]) : 주어진 형상의 행렬을 모두 1로 채운다
-numpy.zeros([ ]) : 주어진 형상의 행렬을 모두 0으로 채운다
matplotlib
-데이터의 분포와 데이터의 시각화를 위해서 matplotlib 라이브러리를 사용함 (그래프 그리기)
1.	scatter plot
ex) import matplotlib.pyplot as plt
import numpy as np
x_data = np.random.rand(100)
y_data = np.random.rand(100)
plt.title('scatter plot')
plt.grid()
plt.scatter(x_data, y_data, color='b', market='o')
plt.show() //그래프 출력
2.	line plot : scatter plot과 마찬가지로 사용하며, 그래프의 한 종류임
<수치미분>
// def numerical_deriative(f,x) 와 같은 코드도 미분의 정의에 의거하여 그대로 구현하면 된다
// 따로 정리는 하지 않음
// 다변수 함수의 미분 코드도 동일하여 그닥 어렵지 않다
import numpy as np
def numerical_derivative(f, x) // f : 다변수 함수, x : 모든 변수를 포함하고 있는 numpy 객체(배열..)
delta_x = 1e-4
grad = np.zeros_like(x) // 계산된 수치미분 값 저장 변수, x의 동일한 크기를 0으로 초기화 한다
it = np.nditer(x, flags=['multi_index'], op_flags=['readwrite'])
while not it.finished: // 변수의 개수 만큼 반복
idx = it.multi_index
tmp_val = x[idx] // numpy 타입은 mutable이므로 원래 값 보관
x[idx] = float(tmp_val) + delta_x // 이후는 수치미분 계산법 (미분 공식 그대로 적용)
fx1 = f(x)
x[idx] = tmp_val - delta_x
fx2 = f(x)
grad[idx] = (fx1 - fx2) / (2 *delta_x)
x[idx] = tmp_val
it.iternext()
return grad
//결과적으로 그냥 코드따라서 함수 사용해서 그대로 구현하면 됨..
<머신러닝 지도/비지도 학습>
지도학습 : 학습할 데이터의 입력과, 입력에 대응되는 정답을 이용해서 미래 결과를 예측
-training data (입력, 정답의 data set) 를 사용하여 학습한다
제목 없음
1.	회귀 (Regression) : training data를 이용하여 학습하고, 연속적인 (숫자) 값을 예측
Linear regression
학습의 개념
-입력(x)인 공부시간에 비례해서 출력(y)인 시험성적도 증가하는 경향이 있음
-즉, 입력(x)과 출력(y)은 y = Wx + b 형태로 나타낼 수 있음
-결과적으로, training data의 특성을 가장 잘 표현할 수 있는 가중치 W(기울기), 바이어스 b( y절편)를 가장 잘 찾는 것이 학습 개념의 목표임
손실함수(loss function)
-training data의 정답(t)과 입력(x)에 대한 계산 값 y의 차이를 모두 더해 수식으로 나타낸 것
-각각의 오차인 (t - y)를 모두 더해서 손실함수(loss function)을 구하면 각각의 오차가 (+), (-) 등이 동시에 존재하기 때문에 오차의 합이 0 이 나올 수가 있다
⇒따라서 오차를 계산할 때는
$(t1-y1)^2+(t2-y2)^2+..+(tn-yn)^2$ $/n$ 을 사용한다
-해당 손실함수인 E(W,b) 값이 작다는 것은 정답 (t, target)과 y = Wx + b에 의해 계산된 값의 평균 오차가 작다는 의미이며, 미지의 데이터 x 가 주어질 경우 확률적으로 미래의 결과값도 오차가 작을 것이라고 추측이 가능하다
손실함수(loss function)의 최소값을 찾을 수 있는 알고리즘
1.	gradient decent algorithm(경사 하강법)
-임의의 가중치 W 선택
-그 W 에서의 직선의 기울기를 나타내는 미분 값( 해당 W에서의 편미분)
-그 미분 값이 작아지는 방향으로 W 감소 또는 증가 시켜 나가면
-최종적으로 기울기가 더 이상 작아지지 않는 곳이 있는데 그곳이 손실함수 E(W) 최솟값
 
// 기초 Linear Regression Python 코드 1

import numpy as np
x_data = np.array([1,2,3,4,5].reshape(5,1)  //입력 데이터
t_data = np.array([2,3,4,5,6]).reshape(5,1)  // 정답 데이터

W = np.random.rand(1,1) // W를 0 ~ 1 사이로 지정
b = np.random.rand(1)
print("W = ", W, ", W.shape = ", W.shape, ".b = ", b, ", b.shape = ", b.shape)

def loss_func(x,t) :  // 손실함수 정의
	y = np.dot(x,W) + b  // 행렬 곱
	return ( np.sum ( (t - y) **2 ) ) / (len(x) )

def numerical_derivative(f,x) : // 수치미분
	delta_x = 1e-4
	grad = np.zeros_like(x)
	it = np.nditer(x, flags=['multi_index'], op_flags=['readwrite'])
	while not it.finished:
		idx = it.multi_index
		tmp_val = x[idx]
		x[idx] = float(tmp_val) + delta_x
		fx1 = f(x)
		
		x[idx] = tmp_val - delta_x
		fx2 = f(x)
		grad[idx] = (fx1-fx2) / (2 *delta_x)
		x[idx] = tmp_val
		it.iternext()
	return grad

def error_val(x,t) :            // 손실함수 값 계산 함수, 입력변수 x, t : numpy type
	y = np.dot(x, W) + b         
	return ( np.sum( (t - y) ** 2 ) ) / ( len(x) )
def predict(x) :                // 학습을 마친 후, 임의의 데이터에 대해 미래 값 예측 함수
	y = np.dot(x,W) + b
	return y

learning_rate = 1e-2   // 학습율 초기화 및 손실함수가 최소가 될 때까지 W, b 업데이트
f = lambda x : loss_func(x_data, t_data)
print("Initial error value = ", error_val(x_data, t_data), "Initial W = ", W, "\\n", b = ", b)

for step in range(8001)
	W -= learning_rate * numerical_derivative(f, W)
	b -= learning_rate * numerical_derivative(f, b)
	if( step % 400 == 0) :        // 400번째마다 손실함수 값, 가중치W, 바이어스b의 현재 값 출력
		print("step = ", step, "error value = ", error_val(x_data, t_data), "W = ", W, ", b = ", b)

// 기초 Multi-Variable Linear Regression Python 코드 2
/*  
학습데이터가 아래와 같을 경우 25 X 4
x1    x2    x3    t
73    80    75    152
93    88    93    185
...................
76    83    71    149
96    93    95    192

		X     dot product    W     +  b   = Y
(25 X 3 ) dot product ( 3 X 1) +  b   = ( 25 X 1)
*/

import numpy as np
loaded_data = np.loadtxt('./data-01-test-score.csv', delimiter=',', dtype=np.float32) // 파일로 부터 데이터를 읽는다
x_data = loaded_data[:, 0:-1]  // 1 ~ 3열 Slicing 통해 입력데이터로 
t_data = loaded_data[:,[-1]]   // 4열의 데이터를 정답 데이터로

/*  y = W1x1 + W2x2 + W3x3 + b 정의 */
W = np.random.rand(3,1) // 3 X 1 행렬
b = np.random.rand(1)
print("W = ", W, ", W.shape = ", W.shape, ", b = ", b, ", b.shape = ", b.shape)

/* 손실함수 E(W,b) 정의 */

def loss_func(x,t) :  // 손실함수 정의
	y = np.dot(x,W) + b  // 행렬 곱
	return ( np.sum ( (t - y) **2 ) ) / (len(x) )

def numerical_derivative(f,x) : // 수치미분
	delta_x = 1e-4
	grad = np.zeros_like(x)
	it = np.nditer(x, flags=['multi_index'], op_flags=['readwrite'])
	while not it.finished:
		idx = it.multi_index
		tmp_val = x[idx]
		x[idx] = float(tmp_val) + delta_x
		fx1 = f(x)
		
		x[idx] = tmp_val - delta_x
		fx2 = f(x)
		grad[idx] = (fx1-fx2) / (2 *delta_x)
		x[idx] = tmp_val
		it.iternext()
	return grad

def error_val(x,t) :            // 손실함수 값 계산 함수, 입력변수 x, t : numpy type
	y = np.dot(x, W) + b         
	return ( np.sum( (t - y) ** 2 ) ) / ( len(x) )
def predict(x) :                // 학습을 마친 후, 임의의 데이터에 대해 미래 값 예측 함수
	y = np.dot(x,W) + b
	return y

learning_rate = 1e-2   // 학습율 초기화 및 손실함수가 최소가 될 때까지 W, b 업데이트
f = lambda x : loss_func(x_data, t_data)
print("Initial error value = ", error_val(x_data, t_data), "Initial W = ", W, "\\n", b = ", b)

for step in range(8001)
	W -= learning_rate * numerical_derivative(f, W)
	b -= learning_rate * numerical_derivative(f, b)
	if( step % 400 == 0) :        // 400번째마다 손실함수 값, 가중치W, 바이어스b의 현재 값 출력
		print("step = ", step, "error value = ", error_val(x_data, t_data), "W = ", W, ", b = ", b)

2.	분류 (Classification) : training data를 이용하여 주어진 입력값이 어떤 종류의 값인지 예측
Logistic Regression
ex) 스팸 문자 분류 [Spam(1) or Ham(0)] , 암 판별 [악성종양(1) or 종양(0) ]
-training data 특성과 분포를 나타내는 최적의 직선을 찾고 (Linear Regression)
-그 직선을 기준으로 데이터를 위(1) 또는 아래(0) 등으로 분류 (Classification) 해주는 알고리즘
⇒이러한 Logistic Regression은 Classification 알고리즘 중에서 정확도가 높은 알고리즘이다
sigmoid function
 
$y = sigmoid(z) = 1/(1+e^-z)$
-출력 값 y 가 1 또는 0만을 가져야만 하는 분류(classification) 시스템에서, 함수 값으로 0 ~ 1사이의 값을 가지는 sigmoid 함수를 사용 할 수 있음
⇒즉, linear regression 출력 Wx + b 가 어떤 값을 갖더라도, 출력 함수로 sigmoid를 사용해서
sigmoid 계산 값이 0.5 보다 크면 1이 나올 확률이 높다는 것이고, sigmoid 계산 값이 0.5 미만이면 결과가 0이 나올 확률이 높다는 의미이다
손실함수(loss function) : 최종 출력 값 y는 sigmoid 함수에 의해 논리적으로 1 또는 0 값을 가지기 때문에, 연속 값을 갖는 선형회귀 때와는 다른 손실함수가 필요함
$E(W,b) = -∑ tlogy + (1-t)log(1-y)$
⇒해당 sigmoid 식을 유도하는건 패스 ~
/* 
공부시간(x)    Fail/Pass(t)
		2              0
		4              0
	...
		14             1
*/

import numpy as np
x_data = np.array([2,4,6,8,10,12,14,16,18,20]).reshape(10,1)
t_date = np.array([0,0,0,0,0,0,1,1,1,1]).reshape(10,1)

W = np.random.rand(1,1)
b = np.random.rand(1)
print("W = ", W, ", W.shape =", W.shape, ", b = ", b ", b.shape = ", b.shape)

def sigmoid(x):
	return 1 / (1 + np.exp(-x))
def loss_func(x,t) :
	delta = 1e-7
	z = np.dot(x, W) + b
	y = sigmoid(z)
	return -np.sum(t * np.log(y+delta) + (1-t)*np.log( (1-y) + delta) )

def numerical_derivative(f,x) :   // 수치 미분 함수
	delta_x = 1e-4
	grad = np.zeros_like(x)
	it = np.nditer(x, flags=['multi_index'], op_flags=['readwrite'])
	while not it.finished:
		idx = it.multi_index
		tmp_val = x[idx]
		x[idx] = float(tmp_val) + delta_x
		fx1 = f(x)
		x[idx] = tmp_val - delta_x
		fx2 = f(x)
		grade[idx] = (fx1 -fx2) / (2 * delta_x)
		x[idx] = tmp_val
		it.iternext()
	return grad

def error_val(x,t) :  // 손실함수 값 계산
	delta = 1e-7
	z = np.dot(x, W) + b
	y = sigmoid(z)
	return -np.sum( t *np.log(y+delta) + (1-t)*np.log((1-y)+delta) )

def predict(x):
	z = np.dot(x,W) + b
	y = sigmoid(z)
	if y > 0.5:
		result = 1
	else 
		result = 0
	return y, result

learning_rate = 1e-2
f = lambda x : loss_function(x_data, t_data)
print("Initial error value = ", error_val(x_data, t_data), "Initial W = ", W, "\\n", ", b = ", b)

for step in range(10001) :
	W -= learning_rate * numerical_derivative(f,W)
	b -= learning_rate * numerical_derivative(f, b)
	if(step % 400 == 0) :
		print("step = ", step, "error value = ", error_val(x_data, t_data), "W = ", W, ", b = ", b)
-AND, OR, XOR , NAND 논리 구조도 Python 으로 구현할 수 있는데 간단하다
-다만, XOR 같은 경우는 NAND, OR, AND 의 조합으로 이루어져 있는데 이것이 신경망(Neural Network) 기반의 딥러닝(Deep Learning) 핵심 아이디어 이다
(즉, Logistic Regression 시스템을 다양하게 조합해서 분석해서 미래값을 예측하는 머신러닝의 분야)
비지도학습 : 학습할 데이터의 입력만 있고 정답은 없다
-입력 데이터의 정답이 없기 때문에 Grouping에 주로 쓰인다
1.	군집화(Clustering) : 뉴스 그룹핑, 백화점의 상품 추천 시스템 등에 사용
<딥러닝과 신경망>
-신경 세포 뉴런(neuron)은 이전 뉴런으로부터 입력신호를 받아 또 다른 신호를 발생시킴
-입력에 비례해서 출력을 내는 형태가 아니라 입력 값들의 모든 합이 어느 임계점에 도달해야만 출력 신호를 발생시킴
-이처럼 입력신호를 받아 특정 값의 임계점을 넘어서는 경우에, 출력을 생성해주는 함수를 활성화 함수(activation function) 이라고 하는데, Logistic Regression 시스템의 sigmoid 함수가 대표적이다.
즉, 딥러닝은 노드가 서로 연결되어 있는 신경망 구조를 바탕으로 입력층(Input Layer), 1개 이상의 은닉층(Hidden Layer), 출력층(Output Layer)를 구축하고 출력층에서의 오차를 기반으로 각 노드의 가중치를 학습하는 머신러닝의 한 분야
⇒1개 이상의 은닉층을 이용하여 학습시키면 정확도가 높은 결과를 얻을 수 있어서 Deep Learning
피드포워드(feed forward) 방식
-이전 층에서 나온 출력값 ⇒ 층과 층 사이에 적용되는 가중치 영향을 받고 ⇒ 다음 층의 입력값으로 들어가는 방식
 
b : 바이오스 , z : 선형회귀 값, a :
/* Deep Learning 으로 XOR 구현*/

import numpy as np

def sigmoid(x):
	return 1 / (1 + np.exp(-x))

def numerical_derivative(f,x) :   // 수치 미분 함수
	delta_x = 1e-4
	grad = np.zeros_like(x)
	it = np.nditer(x, flags=['multi_index'], op_flags=['readwrite'])
	while not it.finished:
		idx = it.multi_index
		tmp_val = x[idx]
		x[idx] = float(tmp_val) + delta_x
		fx1 = f(x)
		x[idx] = tmp_val - delta_x
		fx2 = f(x)
		grade[idx] = (fx1 -fx2) / (2 * delta_x)
		x[idx] = tmp_val
		it.iternext()
	return grad

class LogicGate:
	def __init__(self, gate_name, xdata, tdata) :
		self.name = gate_name
		self.__xdata = xdata.reshape(4,2) // 4개의 입력데이터 x1, x2에 대하여 batch 처리 행렬
		self.__tdata = tdata.reshape(4,1) 

		// 2층 hidden layer unit
		self.__W2 = np.random(2, 6) // 입력데이터가 2개, 은닉층을 6개로 정의
		self.__b2 = np.random(6)    // 은닉층의 노드의 수 6개를 갖는 벡터
		// 3층 output layer unit
		self.__W3 = np.random.rand(6,1) // 은닉층의 노드수가 6개, 출력층의 노드수가 1개
		self.__b3 = np.random.rand(1)  // 출력층의 노드 수 1개를 갖는 벡터

		self.__learning_rate = 1e-2 // 학습율 초기화
		print(self.name + "object is created")

	def feed_forward(self):
		delta = 1e-7
		z2 = np.dot(self.__xdata, self.__W2) + self.__b2  // 은닉층의 선형회귀 값
		a2 = sigmoid(z2)  // 은닉층의 출력
		z3 = np.dot(a2, self.__W3) + self.__b3 // 출력층의 선형회귀 값
		y = a3 = sigmoid(z3) // 출력층의 출력
		return -np.sum( self.__tdata * np.log(y+delta) + (1-self.__tdata)*np.log( (1-y)+delta) )

	def loss_val(self):
		delta = 1e-7
		z2 = np.dot(self.__xdata, self.__W2) + self.__b2
		a2 = sigmoid(z2)
		z3 = np.dot(a2, self.__W3) + self.__b3
		y = a3 = sigmoid(z3)
		return -np.sum( self.__tdata * np.log(y+delta) + (1-self.__tdata)*np.log( (1-y)+delta) )

def train(self): // 수치미분을 이용하여 손실함수가 최소가 될때 까지 학습하는 함수
	f = lambda x : self.feed_forward()
	print("Initial loss value = ", self.loss_val())
	
	for step in range(10001) :
		self.__W2 -= self.__learning_rate * numerical_derivative(f, self.__W2)	
		self.__b2 -= self.__learning_rate * numerical_derivative(f, self.__b2)	
		self.__W3 -= self.__learning_rate * numerical_derivative(f, self.__W3)	
		self.__b3 -= self.__learning_rate * numerical_derivative(f, self.__b3)	
		if(step % 400 == 0) :
			print("step = ", step, " , loss value = ", self.loss_val())

def predict(self, xdata):
	z2 = np.dot(xdata, self.__W2) + self.__b2  // 은닉층의 선형회귀 rkㅄ
	a2 = sigmoid(z2) // 은닉층의 출력
	z3 = np.dot(a2, self.__W3) + self.__b3 // 출력층의 선형회귀 값
	y = a3 = sigmoid(z3) // 출력층의 출력
	if(y > 0.5)
		result = 1
	else
		result = 0
	return y, result

xdata = np.array([ [0,0], [0,1], [1,0], [1,1] ])
tdata = np.array([0,1,1,0])
xor_obj = LogicGate("XOR", xdata, tdata)
xor_obj.train()
<오차역전파>
-수치미분의 문제점 : 수치미분으로 가중치/바이어스 업데이트 시 많은 시간이 소요 됨
-가중치나 바이어스가 변할 때 최종오차가 얼마나 변하는지를 나타내는 $\sigma E/\sigma W^(2)$와 같은 편미분을 체인 룰을 이용하여 분리하여 사용해서 빠르다
-수치미분이 아닌 행렬 기반의 수학공식을 이용한다
-출력층, 은닉층 오차역전파 공식
// 유도과정이 있긴한데 체인률 사용하고 W, b, E 상관관계를 파악하면 그냥 단순함
