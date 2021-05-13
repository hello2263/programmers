def solution(scoville, K):
    global count
    count = count + 1
    sorted(scoville)
    goal=scoville[0]+(scoville[1]*2)
    answer = count

    if (goal >= K):
        return answer
    else:
        scoville[0] = goal
        return solution(scoville, K)


count = 0
scoville = [1, 2, 3, 9, 10, 12]
goal = 0
k = 7
print(solution(scoville, k))



"""
heapify : 기존의 리스트를 힙으로 변환

heappop : 힙에서 원소 삭제. 원소를 삭제할 대상 리스트를 인자로 넘기면, 가장 작은 원소를 삭제 후에 그 값을 리턴한다.

ex) heap = [1, 3, 7, 4]

print(heapq.heappop(heap)) -->1

print(heap)  -->[3, 4, 7]

heappush : 힙에 원소 추가
"""