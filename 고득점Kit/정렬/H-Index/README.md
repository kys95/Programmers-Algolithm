# 문제
1. 어떤 과학자가 발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고 
   나머지 논문이 h번 이하 인용되었다면 h의 최댓값이 이 과학자의 H-Index이다.
2. 과학자가 발표한 논문의 인용 횟수를 담은 배열 citations가 매개변수로 주어질 때, 
   이 과학자의 H-Index를 return 하도록 solution 함수를 작성해라.



# 해결과정
1. 인용된 논문이 많은 순으로 정렬한다. -> 인용된 논문의 갯수의 최댓값을 용이하게 구할 수 있음
2. for문을 통해 h번 이상 인용된 논문이 h편이상인 경우를 탐색한다. 
