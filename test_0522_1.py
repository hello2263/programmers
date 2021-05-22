def solution(bridge_length, weight, truck_weights):
    weight_list = []
    weight_sum = 0
    count = []
    finish = len(truck_weights)
    f_c = 0
    sec = 0
    while (f_c != finish):
        sec = sec + 1
        if (sec > 2):
            if (count[0] == bridge_length):
                count.pop(0)
                weight_sum = weight_sum - weight_list[0]
                weight_list.pop(0)
                f_c = f_c + 1
        if(len(truck_weights) != 0):
            if (weight_sum + truck_weights[0] <= weight):
                weight_sum = weight_sum + truck_weights[0]
                weight_list.append(truck_weights.pop(0))
                count.append(0)
        for i in range(0, len(count)):
            count[i] = count[i] + 1
        if (f_c == finish):
            break
    answer = sec
    return answer


bridge_length = 2
weight = 10
truck_weights = [7, 4, 5, 6]
print(solution(bridge_length, weight, truck_weights))

bridge_length = 100
weight = 100
truck_weights = [10]
print(solution(bridge_length, weight, truck_weights))










