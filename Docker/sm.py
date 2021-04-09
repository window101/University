도커 컨테이너: 서비스 배포
-cmd 에서 ssh로도 접속가능 (AWS 인스턴스 연결 탭=>ssh-i 복사)

=>sudo apt-get update
=>sudo apt-get python3-pip
=>sudo pip3 install notebook
=>python3
=>from notebook.auth import passwd
=>passwd()         설정하고 나면 sha1 으로 돌린 해쉬값이 나온다 (저장)
=>jupyter notebook –generate-config (환경 설정 파일 만듬->환경설정 경로값 반환)
=>sudo vi 환경설정 경로
=>환경 설정 하기
=>sudo jupyter-notebook –-allow-root
=> 해당 포트 열어주고 AWS 인스턴스 공인 IP:포트 로 접속하면 jupyter 노트북의 화면이 뜬다
거기서 cmd 에서 진행한 서버로 접속했던 과정을 동일하게 명령프롬프트로 수행할 수가 있다.
(cmd에서 설정한 비밀번호 사용)
=>bg : 백그라운드로 실행
=>disown -h : 소유권 포기     ->jupyter 노트북 서버가 항상 실행되게 하기 위해서

=>sudo netstat -nap | grep 포트
=>sudo kill -9 PID
=>cd /home/ubuntu (홈 경로로 이동)
=> mkdir ssl && cd ssl
=>sudo openssl req -x509 -nodes -days 365 -newkey rsa:1024 -keyout "cert.key" -out "cert.pem" -batch
 (https ssl 인증서 만듬(유효기간), 개인키(cert.key), 공개키(cert.pem) 만듬)
=>ls 하면 cert.key, cert.pem이 나와야 함
=>환경설정을 열어주고 C.NotebookApp.certfile=u'/home/ubuntu/ssl/cert.pem'
			C.NotebookApp.keyfile=u'/home/ubuntu/ssl/cert.key'

=>sudo jupyter-notebook –-allow-root (다시 jupyter notebook 실행)
(https가 적용됨)
다시 https://AWS공개IP:포트 로 접속하면 신뢰할 수 없다고 나오는데 크롬 브라우저가 내가 만든 사설ssl을 신뢰하지 못하기 때문에 발생하는 경고창인데 그냥 무시하면 된다.


서버가 재부팅 되었을 때 (노트북) jupyter notebook이 자동실행 될 수 있게 아래처럼 한다 
->jupyter notebook을 시스템 서비스로써 등록 시켜야 함

=>which jupyter-notebook   (jupyter-notebook의 실행파일 경로)
=>sudo vi /etc/systemd/system/jupyter.service  (서비스 파일 작성)

//////////////////////////////////////////jupyter.service 파일 – 정해진 양식이 있음
[Unit]
Description=Jupyter Notebook Server

[Service]
Type=simple
User=ubuntu        (AWS 기본 유저 계정)
ExecStart=/usr/bin/sudo /usr/local/bin/jupyter-notebook –allow-root –config=/home/ubuntu/ .jupyter/jupyter_notebook_config.py
(sudo 명령으로 jupyter notebook을 root 권한을 허용한 상태로써 jupyter notebook 환경설정 파일을 사용해서 jupyter notebook을 구동하겠다)

[Install]
WantedBy=multi-user.target

///////////////////////////////////////////////////////////////////////////////////////////////////////// 

=>sudo systemctl daemon-reload      (데몬 재시작)
=>sudo systemctl enable jupyter      (jupyter notebook을 사용가능한 상태로 만듬)
=>sudo systemctl start jupyter        (jupyter를 항상 실행상태로 만듬)
=>sudo systemctl status jupyter       (jupyter가 성공적으로 실행이 되었나 확인)
=>sudo systemctl restart jupyter      (jupyter 서비스 재시작)

//도커 설치
=>df -h : 메모리 공간 확인
=>sudo apt update
=>sudo apt install apt-transport-https
=>sudo apt install ca-certificates
=>sudo apt install curl     (특정 웹 사이트에서 데이터를 다운로드 받을 때 사용)
=>sudo apt install software-properties-common
=>curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add-
=>sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable"
=>sudo apt update
=>apt-cache policy docker-ce
=>sudo apt install docker-ce
(도커는 설치되면 자동으로 시스템 서비스로써 등록이 된다)


// 도커 실습
hello world 이미지를 다운로드 받아서 실행
=>docker pull hello-world            //pull:특정한 서버파일을 이미지 형태로써 다운로드 받게 함
=>docker images  (다운로드 받은 도커 이미지 확인)
=>docker run hello-world   (다운로드 받은 이미지 -hello world 컨테이너 형태로 띄워보기)
해당 작업을 하게 되면 우리의 서버위에 별도의 하나의 서버가 더 생성되어서 서버가 동작하고 작업이 종료된것임

=>docker ps -a  (어떤 컨테이너가 동작했는지 확인가능 – 아래와 같이 나옴)
CONTAINER ID 	IMAGE		COMMAND		CREATED		STATUS
700cdeb001bbgo	hello-world	"/hello"		36 seconds age	   Exited(0) 34 seconds ago

=>docker rm 700cdeb001bbgo    (해당 컨테이너 삭제)
=>docker images   (컨테이너를 삭제하더라도 해당 이미지 파일은 남아있음)
=>docker run hello-world  (와 같은 명령어로 언제든지 해당 이미지를 컨테이너로 띄울 수 있음)

//도커 파일을 직접 작성해서 하나의 서버 이미지를 직접 만들어 보자

=>cd /home/ubuntu
=>ls        (기존에 작성한 ssl 디렉터리가 있는 곳에 새로운 도커 이미지 파일을 만든다)
=>mkdir example && cd example
=>sudo vi Dockerfile





////////////////////////Dockerfile 내부 ///////////////////////// - 일정한 형식이 있음

FROM ubuntu:18.04
MAINTAINER HwaJun Park <hwajun15@naver.com>   //도커파일을 누가 작성했는지 명시

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update
RUN apt-get install -y apache2
RUN apt-get install -y software-properties-common    //php5.6 respository 설치위해
RUN add-apt-repository ppa:ondrej/php
RUN apt-get update
RUN apt-get install -y php5.6

RUN apt-get install -y php5.6-mysql     //php-mysql 연동
EXPOSE 80
CMD ["apachectl", "-D", "FOREGROUND"]         //아파치를 데몬상태로 만듬(항상 실행)

//ubunu18.04 서버가 구동되면 간단히 웹 서버를 구동할 수 있도록 설정
도커 파일을 명시해서 이미지 파일을 생성한 뒤에 그것으로 컨테이너를 만들게 되면 그 컨테이너를 실제로 구동하고 있는 그 서버 컴퓨터에서 해당 컨테이너에 접속하기 위해서 실제로 몇번 포트를 이용해서 연결을 할 것인지

// ENV DEBIAN_FRONTEND=noninteractive
하는 이유는 컨테이너 빌드시에 선택옵션이 나왔을 때 사용자가 입력을 할 수가 없기에 미리 선택옵션을 제거 해주는 것임
////////////////////////////////////////////////////////////////////////////////////////////////////////////

=>docker build -t example .
		  도커파일이름(아무거나), 현재경로(.)

=>dockert images     하면 아래와 같이 나옴
REPOSITORY		TAG		IMAGE ID		CREATED		SIZE
example		latest		9770f001e7a5	      5 seconds ago		209MB
ubuntu			18.04		94e814e2efa8		~			~	

=>docker build -t example .


=>docker run -p 80:80 -v /home/ubuntu/example/html:/var/www/html example
왼쪽 80 : 현재 example 컨테이너가 구동될때 사용하는 포트  (위의 도커파일에서 명시된)
오른쪽 80: 현재 아마존 서버의 ec2 포트   를 서로 연결하고 구동한다.

/var/www/html : php의 기본적인 경로

그 후에, ec2ip:80 으로 접속했을 때 Apache2 Ubuntu Default Page가 나와야 한다.
여기까지 하면 example 이라는 이미지안에 apache, php가 설치되어 있는 개발환경이 구축된 것임

//mysql 은 도커 허브에 존재하는 이미지 이기때문에 별도의 과정없이 즉시 mysql 이미지를 다운받아서 사용이 가능하다

=>docker run -d -p 9876:3306 -e MYSQL_ROOT_PASSWORD=password mysql:5.6
(mysql 5.6 이미지를 다운로드 받아서 MYSQL ROOT PASSWORD를 password로 설정)

=>docker ps -a  (mysql 연결 확인)

1) Mysql 접속 하는 방법   (mysql 과 apache && php 환경은 분리되어 있는 것임 밑에서 연동)
=> docker exec -it MYSQL CONTAINER ID /bin/bash
( /bin/bash 명령어를 사용해서 도커 컨테이너의 mysql에 접속)
=>mysql -u root -p    로 접속 가능
=>exit   

2) 
=>docker inspect MYSQL CONTAINER ID     (도커 컨테이너의 세부 정보 확인 하면 아래쪽에서 "IPAddress" 라는 필드가 있다)

=>mysql -u root -p –-host IPADDRESS –-port 3306  
// 해당 명령어는 aws instance 내에 mysql이 깔려있을 때만 적용된다. 만약 깔려있지 않다면 
Command 'mysql' not found, but can be installed with 이라는 문구가 뜬다
=>sudo apt install mysql-client-core-5.7 로 설치가능

3) mysql -u root -p –-host 127.0.0.1 –-port 9876 
(호스트와 mysql이 9876:3306으로 연결되어 있기 때문에 사용가능하다)
// php, mysql 연동
php와 mysql을 연동하기 위해 위의 Dockerfile에서 php5.6-mysql을 추가한다.
=>다시 재빌드하기

아까 만든 index.php 에서 php와 mysql을 연결하는 구문을 작성한다(영상 참고)
