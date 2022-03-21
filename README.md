# blind_sqli

webhacking.kr old-2를 풀기 위한 blind sql injection을 수행하는 스크립트입니다.

문제에서 사용되는 cookie 중 time cookie의 참, 거짓에 따라 페이지에 보여지는 소스가 달라져 blind sql injection 적용이 가능합니다.

time cookie에 DB이름, table이름, 컬럼이름, 내용에 대한 질의문을 넣어 blind sql injection을 진행하였습니다.
