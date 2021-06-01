def solution(numbers):
    from itertools import permutations
    import math
    answer = 0
    count = []
    flag = 0
    for i in range(1, len(numbers)+1):
        count.extend(list(int(''.join(i)) for i in permutations(numbers, i)))
    t_s = set(count)
    t_l = list(t_s)
    count = t_l
    for j in count:
        num = math.sqrt(j)
        for k in range(2, int(num)+1):
            if j % k == 0:
                flag = 0
                break
        if ((j >= 2)&(flag == 1)) == 1:
            answer += 1
        elif (j==2):
            answer += 1
        flag = 1
    return answer

