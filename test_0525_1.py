def solution(jobs):
    answer = 0
    start = 0
    count = []
    result = 0
    jobs = sorted(jobs)
    print(jobs)
    for i in jobs:
        count.append(i[1] - i[0])
        result = result + i[1]
    start = count.pop(0)
    for j in range(1, len(count)):
        count[j] = count[j] + count[j-1]
    print(count)
    return answer

jobs = [[0, 3], [1, 9], [2, 6]]
print(solution(jobs))

