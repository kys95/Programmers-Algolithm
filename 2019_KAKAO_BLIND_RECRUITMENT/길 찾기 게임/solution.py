import sys

sys.setrecursionlimit(10 ** 6)


def preorder(arrY, arrX, answer):
    node = arrY[0]
    idx = arrX.index(node)
    arrY1 = []
    arrY2 = []

    for i in range(1, len(arrY)):
        if node[0] > arrY[i][0]:
            arrY1.append(arrY[i])
        else:
            arrY2.append(arrY[i])

    answer.append(node[2])
    if len(arrY1) > 0:
        preorder(arrY1, arrX[:idx], answer)
    if len(arrY2) > 0:
        preorder(arrY2, arrX[idx + 1:], answer)
    return


def postorder(arrY, arrX, answer):
    node = arrY[0]
    idx = arrX.index(node)
    arrY1 = []
    arrY2 = []

    for i in range(1, len(arrY)):
        if node[0] > arrY[i][0]:
            arrY1.append(arrY[i])
        else:
            arrY2.append(arrY[i])

    if len(arrY1) > 0:
        postorder(arrY1, arrX[:idx], answer)
    if len(arrY2) > 0:
        postorder(arrY2, arrX[idx + 1:], answer)
    answer.append(node[2])
    return


def solution(nodeinfo):
    preanswer = []
    postanswer = []

    for i in range(len(nodeinfo)):
        nodeinfo[i].append(i + 1)

    arrY = sorted(nodeinfo, key=lambda x: (-x[1], x[0]))
    arrX = sorted(nodeinfo)

    preorder(arrY, arrX, preanswer)
    postorder(arrY, arrX, postanswer)

    return [preanswer, postanswer]
#
#
# 1. nodeinfo의 각 원소(x,y위치)에 노드번호(인덱스+1)를 추가한다.
# 2. nodeinfo를 x를 기준으로 오름차순 정렬한 arrX, y를 기준으로 내림차순 정렬한 arrY를 생성한다.
# 3. 전위순회하는 함수 preorder, 후위순회하는 함수 postorder를 정의한다.
# 4. preorder의 매개변수로 arrX, arrY, 답을 저장할 배열 answer을 받는다.
# 5. 중심이 될 노드 node=arrY[0]을 선언한다. (y축값이 제일 높은 노드가 루트이므로)
#    중심 노드의 arrX에서의 인덱스를 알아낸다. (idx)
#    중심 노드를 기준으로 왼쪽 노드들을 저장할 arrY1, 오른쪽 노드들을 저장할 arrY2를 준비한다.
# 6. arrY에서 중심노드를 제외한 인덱스 1~마지막까지 탐색한다.(i)
#   6-1. arrY[i]의 x값이 중심노드의 x값보다 작다면 arrY1에 삽입, 크다면 arrY2에 삽입한다.
# 7. 답을 저장하는 answer에 중심노드의 번호인 node[2]를 삽입한다.
# 8. 만약 arrY1의 크기가 0이 아니라면 arrY1과 arrX의 0부터 idx까지로 다시 preorder를 재귀호출한다.
# 9. 만약 arrY2의 크기가 0이 아니라면 arrY2와 arrX의 idx+1부터 끝까지로 다시 preorder를 재귀호출한다.
# 10. 후위순회 postorder도 똑같지만 7,8,9번의 순서를 후위순회 순서인 8,9,7로 바꾼다.