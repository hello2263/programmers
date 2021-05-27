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
            heapq.heappush(heap, int(item[num][1]))
        elif (item[num][0] == 'D'):
            if(len(heap) != 0):
                if (item[num][1] == '1'):
                    heap.sort(reverse=True)
                    heapq.heappop(heap)
                elif (item[num][1] == '-1'):
                    heap.sort()
                    heapq.heappop(heap)
        num += 1
        count += 1
    if (heap != []):
        heap.sort(reverse=True)
        answer.append(heapq.heappop(heap))
        heap.sort()
        answer.append(heapq.heappop(heap))
    else :
        answer = [0, 0]
    return answer