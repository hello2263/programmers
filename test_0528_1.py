
def solution(n, lost, reserve):
    answer = n-len(lost)
    lost = sorted(lost)
    reserve = sorted(reserve)
    item = []
    for i in reserve:
        if (i in lost):
            answer += 1
            item.append(i)

    for j in item:
        lost.remove(j)
        reserve.remove(j)

    for i in range(0, len(lost)):
        for k in reserve:
            if((lost[i] + 1) == k) or ((lost[i] - 1) == k):
                reserve.remove(k)
                answer += 1
                break
    return answer
