

def solution(array, commands):
    answer = []
    k = []
    for i in commands:
        for j in i:
            k.append(j)
        a = array[k[0]-1:k[1]]
        a = sorted(a)
        answer.append(a[(k[2]-1)])
        k = []
    return answer


array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(array, commands))
