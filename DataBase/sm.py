select ifnull(null, '널이군요'), ifnull(100, '널이군요');
select if(100> 200, '참이다', '거짓이다');

select case 10
	when 1 then '일'
    when 5 then '오'
    when 10 then '십'
    else '모름'
end as 'case연습';

select concat_ws('/', '2025', '01', '01');

select substring('대한민국만세', 3, 2);

select substring_index('cafe.naver.com', '.', 2), substring_index('cafe.naver.com', '.', -2);

select mod(157, 10), 157 % 10, 157 mod 10;

select pow(2,3), sqrt(9);

select truncate(12345.12345, 2), truncate(12345.12345, -2);

select adddate('2025-01-01', interval 31 day), adddate('2025-01-01', interval 1 month);
select subdate('2025-01-01', interval 31 day), subdate('2025-01-01', interval 1 month);

select addtime('2025-01-01 23:59:59', '1:1:1'), addtime('15:00:00', '2:10:10');
select subtime('2025-01-01 23:59:59', '1:1:1'), subtime('15:00:00', '2:10:10');

// curdata : 현재 연-월-일, curtime : 현재 시:분:초
;

select year(curdate()), month(curdate()), dayofmonth(curdate());
select hour(curtime()), minute(curtime()), second(curtime());

select date(now()), time(now());

select datediff('2025-01-01', now()), timediff('23:23:59', '12:11:10');

select curdate();
// 요일 (1 : 일, 2: 월 ~ 7: 토)
// 현재 요일과 월 이름 그리고 일년 중 몇 일이 지났는지 반환한다
select dayofweek(curdate()), monthname(curdate()), dayofyear(curdate());

select last_day('2025-01-01');
// 주어진 날짜의 마지막 날짜를 구한다

select makedate(2025, 32);

select period_add(202501, 11), period_diff(202501, 202312);

select quarter('2025-07-07');
// 날짜가 4분기 중에서 몇 분기인지 구한다

select time_to_sec('12:11:10');
// 시간을 초 단위로 구한다

// 영화 테이블 구현 예시
CREATE TABLE ~ (
...
movie_script LONGTEXT,
movie_film LONGBLOB
)
INSERT INTO ~ VALUES (1, '쉰들러 리스트', '스필버그', '리암 니슨', LOAD_FILE('C:/SQL/Schindler.txt'), LOAD_FILE('C:/SQL/.mp4'));
// 하기 전에 show variables like 'max_allowed_packet' 확인, show variables like 'secure_file_priv' 확인

select movie_script from ~ where movie_id = 1     // outfile 에 적힌 파일로 대본 다운로드 받아진다
	into outfile 'C:/SQL/Schindler_out.txt'
    lines terminated by '\\n';
    
select movie_film from ~ where movie_id = 3
	into dumpfile 'C:/SQL/Movies/Mohiacn_out.mp4';    // 영화 다운로드
    

// 피벗의 구현
uName		season		amount =>		uName	봄	여름		가을		겨울		합계
김범수		겨울			10				김범수	40	14		25		32		111
윤종신		여름			15				윤종신	0	79		0		40		119
김범수		가을			25
김범수		봄			3
김범수		봄			37
윤종신		겨울			40
김범수		여름			14
김범수		겨울			22
윤종신		여름			64

select uName,
	sum(if(season='봄', amount, 0)) as '봄',
    sum(if(season='여름', amount, 0)) as '여름',
    sum(if(season='가을', amount, 0)) as '가을',
    sum(if(season='겨울', amount, 0)) as '겨울',
    sum(amount) as '합계' from pivotTest group by uName;
    


// Inner join 의 활용 중에서 한번도 구매한 적이 없는 유령회원 같은 정보도 뽑을 수 있다

select U.userID, U.name, B.prodName, U.addr, CONCAT(U.mobile1, U.mobile2) AS '연락처'
	from usertbl U
		LEFT OUTER JOIN buytbl B
			ON U.userID = B.userID
		WHERE B.prodName IS NULL
		ORDER BY U.userID;
        
// SELF JOIN은 조직도 구성에 쓰인다
ex) 	부하 직원		직속 상관		직속 상관 연락처
		우대리		이부장		2222-2
        
select A.emp as '부하직원', B.emp as '직속상관', B.empTel as '직속상관연락처'
	from empTbl A
		inner join empTbl B
        on A.manager = B.emp
	where A.emp = '우대리';
    
// UNION : 주로 월 마다 분리된 실적을 연말에 합쳐서 계산해야 될때 사용한다
UNION : 중복된 열은 제거, UNION ALL : 중복된 열까지 출력

// NOT IN : 첫번째 쿼리의 결과 중에서, 두번째 쿼리에 해당하는 것을 제외
(EX. sqldb의 사용자를 모두 조회하되, 전화가 없는 사람을 제외하고 싶다면)

select name, concat(mobile1, mobile2) as '전화번호' from usertbl
	where name not in ( select name from usertbl where mobile1 is null);
    
// IN : 첫번째 쿼리의 결과 중에서, 두번째 쿼리에 해당되는 것만 조회하기 위해서는
(EX2. 전화가 없는 사람만 조회하고자 하면)

select name, concat(mobile1, mobile2) as '전화번호' from usertbl
	where name in ( select name from usertbl where mobile1 is null);


