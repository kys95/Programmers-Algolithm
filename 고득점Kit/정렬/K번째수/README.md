# 문제

1. 배열 array의 i번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때, k번째에 있는 수를 구한다.
2. 매개변수 commands는 [i,j,k]를 원소로 가진 2차원 배열이다.



# 해결과정 
1. commands의 i,j,k를 for문으로 받고 array의 i번째~j번째 원소를 자른 data 리스트를 구한다.
2. 오름차순 정렬한 후, data의 k번째 원소를 answer 리스트에 추가한다.
3. return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands)) 람다 이용 풀이 참고

