
def solution(citations):
    answer = 0
    citations.sort()
    cit_l = len(citations)

    for i in range(cit_l):
        if cit_l-i <= citations[i]:
            return cit_l - i

    return answer


