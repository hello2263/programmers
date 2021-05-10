def solution(participant, completion):
    answer = ''
    x = {}
    for i in participant:
        if(i not in completion):
            answer = i
    if (answer == ''):
        for j in completion:
            x[j] = 0
        for key in participant:
            if (key in completion):
                x[key] = x[key] + 1
        for k in x:
            for z in x:
                if (x.get(k) > x.get(z)):
                    answer = k
    return answer

























# def solution(participant, completion):
#     answer = ''
#     participant.sort()
#     completion.sort()
#     for i in range(0, len(completion)):
#         if participant[i] != completion[i]:
#             answer = participant[i]
#             break
#     if answer == '':
#         answer = participant[len(completion)]
#     return answer

