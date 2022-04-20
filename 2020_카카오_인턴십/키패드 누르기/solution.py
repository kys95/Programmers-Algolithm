# def solution(numbers, hand):
#     answer = ''

#     pad = {1:['L',(0,0)], 4:['L',(1,0)], 7:['L',(2,0)],
#           3:['R',(0,2)], 6:['R',(1,2)], 9:['R',(2,2)],
#           2:(0,1), 5:(1,1),8:(2,1), 0:(3,1)}

#     Le = (3,0)  #왼손 위치
#     Ri = (3,2)  #오른손 위치

#     for num in numbers:
#         if pad[num][0] == 'L':      #왼손
#             answer += pad[num][0]
#             Le = pad[num][1]        #왼손 위치 갱신

#         elif pad[num][0] == 'R':        #오른손
#             answer += pad[num][0]
#             Ri = pad[num][1]

#         else:
#             if abs(Le[0] - pad[num][0]) + abs(Le[1] - pad[num][1]) > abs(Ri[0] - pad[num][0]) + abs(Ri[1] - pad[num][1]):
#                 answer += 'R'
#                 Ri = pad[num]

#             elif abs(Le[0] - pad[num][0]) + abs(Le[1] - pad[num][1]) < abs(Ri[0] - pad[num][0]) + abs(Ri[1] - pad[num][1]):
#                 answer += 'L'
#                 Le = pad[num]

#             else:
#                 if hand == 'left':
#                     answer += 'L'
#                     Le = pad[num]
#                 else:
#                     answer += 'R'
#                     Ri = pad[num]


#     return answer

def solution(numbers, hand):
    answer = ''

    pad = {1: (0, 0), 4: (1, 0), 7: (2, 0),
           3: (0, 2), 6: (1, 2), 9: (2, 2),
           2: (0, 1), 5: (1, 1), 8: (2, 1), 0: (3, 1),
           '*': (3, 0), '#': (3, 2)}

    Le = [1, 4, 7]
    Ri = [3, 6, 9]
    lhand = '*'
    rhand = '#'

    for num in numbers:
        if num in Le:
            answer += 'L'
            lhand = num

        elif num in Ri:
            answer += 'R'
            rhand = num

        else:
            ldis = abs(pad[num][0] - pad[lhand][0]) + abs(pad[num][1] - pad[lhand][1])
            rdis = abs(pad[num][0] - pad[rhand][0]) + abs(pad[num][1] - pad[rhand][1])

            if ldis > rdis:
                answer += 'R'
                rhand = num

            elif ldis < rdis:
                answer += 'L'
                lhand = num

            else:
                if hand == 'left':
                    answer += 'L'
                    lhand = num

                else:
                    answer += 'R'
                    rhand = num

    return answer