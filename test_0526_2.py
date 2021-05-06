def solution(answers):
    answer = []
    i = 0
    j = 0
    s_1 = [1, 2, 3, 4, 5]
    s_1 = s_1 * 2000
    count_1 = 0

    s_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    s_2 = s_2 * 1250
    count_2 = 0

    s_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    s_3 = s_3 * 1000
    count_3 = 0

    while (i < len(answers)):
        if (s_1[i] == answers[j]):
            count_1 += 1
        if (s_2[i] == answers[j]):
            count_2 += 1
        if (s_3[i] == answers[j]):
            count_3 += 1
        i += 1
        j += 1
        if (j > len(answers)):
            j = 0
    if (count_1 < count_2):
        if (count_2<count_3):
            answer.append(3)
        elif (count_2>count_3):
            answer.append(2)
        else:
            answer.append(2)
            answer.append(3)
    elif (count_1 > count_2):
        if (count_1 < count_3):
            answer.append(3)
        elif (count_1 > count_3):
            answer.append(1)
        else:
            answer.append(1)
            answer.append(3)
    else:
        if (count_1 < count_3):
            answer.append(3)
        elif (count_1 >count_3):
            answer.append(1)
            answer.append(2)
        else:
            answer.append(1)
            answer.append(2)
            answer.append(3)


    answer=sorted(answer)
    return answer

# def solution(answers):
#     pattern1 = [1,2,3,4,5]
#     pattern2 = [2,1,2,3,2,4,2,5]
#     pattern3 = [3,3,1,1,2,2,4,4,5,5]
#     score = [0, 0, 0]
#     result = []
#
#     for idx, answer in enumerate(answers):
#         if answer == pattern1[idx%len(pattern1)]:
#             score[0] += 1
#         if answer == pattern2[idx%len(pattern2)]:
#             score[1] += 1
#         if answer == pattern3[idx%len(pattern3)]:
#             score[2] += 1
#
#     for idx, s in enumerate(score):
#         if s == max(score):
#             result.append(idx+1)
#
#     return result