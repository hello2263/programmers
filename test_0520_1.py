def solution(progresses, speeds):
    finish = []
    count = 1
    date = 0
    date_list = []
    answer = []
    for i in range(0, len(progresses)):
        while (progresses[i] < 100):
            progresses[i] = progresses[i] + speeds[i]
            date = date + 1
            if progresses[i] >= 100:
                finish.append(progresses[i])
        date_list.append(date)
        date = 0
    for j in range(0, len(date_list)):
        if j == 0:
            start = date_list[j]
        else:
            if date_list[j] <= start:
                count = count + 1
                if j == len(date_list)-1:
                    answer.append(count)
            elif date_list[j] > start:
                answer.append(count)
                count = 1
                start = date_list[j]
                if j == len(date_list)-1:
                    answer.append(count)
    return answer
