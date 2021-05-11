def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    count = len(participant)
    for i in range(0,count-1):
        if (participant[i] != completion[i]):
            answer = participant[i]
            break
    if(answer == ''):
        answer = participant[count-1]
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

