### 해결과정
1. 모든 기록에서 보여지는 것들은 해당 유저의 최종 닉네임이 들어간 들어가거나 나간 행위이므로 최종 유저의 닉네임을 넣을 자료구조가 필요함
   -> 유저의 아이디를 key, 닉네임을 value로 하는 딕셔너리 자료형을 사용
2. 모든 기록에서 보여지는 것들은 유저가 들어가거나 나가는 행위를 순서대로 출력해야하므로 해당 순서를 (유저아이디,들어감or나감)의 형태로
   order 리스트에 넣는다.
3. order에서 for문으로 하나씩 꺼내면서 순서대로 유저의 최종 닉네임+들어감or나감의 형태로 출력한다.