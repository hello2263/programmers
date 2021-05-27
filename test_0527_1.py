# def solution(jobs):
#     import heapq
#     n = len(jobs)
#     time, end, heap = 0, -1, []
#     answer, count = 0, 0
#     while count < n:
#         for i in jobs:
#             if end < i[0] <= time:
#                 answer += (time - i[0])
#                 heapq.heappush(heap, i[1])
#         if len(heap) > 0:
#             answer += len(heap) * heap[0]
#             end = time
#             time += heapq.heappop(heap)
#             count += 1
#         else:
#             time += 1
#
#     return (int(answer / n))
#
# jobs = [[0, 3], [1, 9], [2, 6]]
# print(solution(jobs))




def solution(operations):
    import heapq
    answer = []
    item = []
    heap = []
    count, num = 0, 0
    for i in range(0, len(operations)):
        item.append(operations[i].split(" "))
    while count != len(operations):
        if (item[num][0] == 'I'):
            heapq.heappush(heap, item[num][1])
        elif (item[num][0] == 'D'):
            if(len(heap) != 0):
                if (item[num][1] == '1'):
                    heapq.heappop(heap)[-1]
                elif (item[num][1] == '-1'):
                    heapq.heappop(heap)
        num += 1
        count += 1
    answer = [0, 0]
    if (heap != []):
        answer = heap
    return answer

# operations = ["I 16","I -5643", "D -1", "D 1", "I 123", "D -1"]
# print(solution(operations))
# operations = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
# print(solution(operations))


















