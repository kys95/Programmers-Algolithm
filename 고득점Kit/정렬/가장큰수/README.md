# 문제
1. 0 또는 양의 정수가 주어질 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 구해라.
2. 예를 들어, 주어진 정수가 [6, 10, 2]라면 [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고, 
   이중 가장 큰 수는 6210이다.
3. numbers 원소는 0~1000이다.
4. 문자열로 바꾸어 return한다


# 해결과정
1. 배열 numbers 원소를 숫자가 아닌 문자열로 바꾼다.
2. 문자열의 첫번째 원소부터 차례대로 비교해야하므로 lambda x: x*3를 통해
   numbers 원소값을 3자리수로 맞춰 비교한다.(numbers 원소값이 1000이하)
3. 모든 값이 0일 수 있으니 int로 변한한 뒤에 str으로 변환하여 반환한다.