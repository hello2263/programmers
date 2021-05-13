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