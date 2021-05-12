
def solution(clothes):
    count = {}
    answer = 1
    for i in clothes:
        if (count.get(i[1]) != None):
            count[i[1]] = count[i[1]] + 1
        else:
            count[i[1]] = 1
    for num in count.values():
        answer = answer * (num + 1)
    return answer - 1
