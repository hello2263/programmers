def solution(numbers):
    from itertools import permutations
    import math
    import pandas as pd
    answer = 0
    count = []
    for i in range(1, len(numbers)+1):
        count.extend(list(int(''.join(i)) for i in permutations(numbers, i)))
    count = pd.unique(count).tolist()
    for j in count:
        num = math.sqrt(j)
        for k in range(2, int(num)+1):
            if j % k == 0:
                break
        if (j >= 2):
            answer += 1
    print(count)
    return answer

numbers = "17"
print(solution((numbers)))
numbers = "011"
print(solution((numbers)))
