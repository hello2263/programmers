
def solution(priorities, location):
    answer = 0
    place = [i for i in range(len(priorities))]
    f_place = []
    print(place)

    while (len(priorities) !=0):
        if (priorities[0]==max(priorities)):
            f_place.append(place.pop(0))
            priorities.pop(0)
        else:
            priorities.append(priorities.pop(0))
            place.append(place.pop(0))

    
    answer = f_place.index(location) + 1
    return answer



priorities = [2, 1, 3, 2]
location = 2
print(solution(priorities, location))

priorities = [1, 1, 9, 1, 1, 1]
location = 0
print(solution(priorities, location))