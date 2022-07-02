def solution(new_id):
    answer = ''

    for i in range(len(new_id)):
        answer += new_id[i].lower()

    answer2 = ''
    for i in range(len(answer)):

        if answer[i].isalpha() or answer[i].isdigit() or answer[i] == '-' or answer[i] == '_' or answer[i] == '.':
            answer2 += answer[i]

    answer3 = ''
    flag = True
    for i in range(len(answer2)):
        if answer2[i] == '.':
            if flag == False:
                continue
            else:
                answer3 += answer2[i]
                flag = False
        else:
            flag = True
            answer3 += answer2[i]

    # 4단계
    answer3 = answer3[1:] if answer3[0] == '.' and len(answer3) > 1 else answer3
    answer3 = answer3[:-1] if answer3[-1] == '.' else answer3

    if answer3 == '':
        answer3 += 'a'
    if len(answer3) >= 16:
        answer3 = answer3[:15]
        if answer3[-1] == '.':
            answer3 = answer3[:len(answer3) - 1]

    target = 3 - len(answer3)

    if target > 0:
        answer3 += target * answer3[-1]

    return answer3

# def solution(new_id):

#     # 1단계
#     new_id = new_id.lower()
#     # 2단계
#     answer = ''
#     for word in new_id:
#         if word.isalnum() or word in '-_.':
#             answer += word
#     # 3단계
#     while '..' in answer:
#         answer = answer.replace('..', '.')
#     # 4단계
#     answer = answer[1:] if answer[0] == '.' and len(answer) > 1 else answer
#     answer = answer[:-1] if answer[-1] == '.' else answer
#     # 5단계
#     answer = 'a' if answer == '' else answer
#     # 6단계
#     if len(answer) >= 16:
#         answer = answer[:15]
#         if answer[-1] == '.':
#             answer = answer[:-1]
#     # 7단계
#     if len(answer) <= 3:
#         answer = answer + answer[-1] * (3-len(answer))
#     return answer