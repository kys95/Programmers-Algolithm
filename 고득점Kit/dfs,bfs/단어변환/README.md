# 문제
1. 두 개의 단어 begin, target과 단어의 집합 words가 있습니다. 
2. 아래와 같은 규칙을 이용하여 begin에서 target으로 변환하는 가장 짧은 변환 과정을 찾으려고 합니다.
   1. 한 번에 한 개의 알파벳만 바꿀 수 있습니다.
   2. words에 있는 단어로만 변환할 수 있습니다.
3. 예를 들어 begin이 "hit", target가 "cog", words가 
   ["hot","dot","dog","lot","log","cog"]라면 "hit" -> "hot" -> "dot" -> "dog" -> "cog"와 같이 4단계를 거쳐 변환할 수 있습니다.
4. 두 개의 단어 begin, target과 단어의 집합 words가 매개변수로 주어질 때, 
   최소 몇 단계의 과정을 거쳐 begin을 target으로 변환할 수 있는지 return 하도록 solution 함수를 작성해주세요.



# 해결과정
1. 한 번에 한 개의 알파벳만 바꿀 수 있으므로 begin과 배열 words에 있는 데이터들을 비교하여 알파벳 차이가 1인 단어들과 1단계 cnt를 queue에 
   삽입하고 방문표시를 한다.
2. queue에 들어있는 단어들을 다시 pop하여 알파벳 차이가 1인 단어들을 words에서 찾아 queue에 삽입한다. 단, 선택하지 않은 단어들만 해당된다.
3. 이처럼 bfs를 통해 찾아가면서 target과 동일한 단어를 찾게될 경우 해당 cnt를 return해준다.
   