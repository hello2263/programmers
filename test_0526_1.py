def solution(jobs):
    import heapq
    n = len(jobs)
    time, end, heap = 0, -1, []
    answer, count = 0, 0
    while count < n:
        for i in jobs:
            if end < i[0] <= time:
                answer += (time - i[0])
                heapq.heappush(heap, i[1])
        if len(heap) > 0:
            answer += len(heap) * heap[0]
            end = time
            time += heapq.heappop(heap)
            count += 1
        else:
            time += 1

    return (int(answer / n))

jobs = [[0, 3], [1, 9], [2, 6]]
print(solution(jobs))

