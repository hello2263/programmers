def solution(genres, plays):
    answer = []
    length = range(0, len(genres))
    num = {}
    type = {}
    item = {}
    count = 0
    for i in length:
        num[i] = plays[i]
        type[genres[i]] = type.get(genres[i], 0) + plays[i]
        item[i] = genres[i]
    type_s = sorted(type, key=lambda y: type[y], reverse=True)
    num_s = sorted(sorted(sorted(num.items(), key=lambda x: x[0], reverse=True)), key=lambda x: x[1], reverse=True)
    for i in type_s:
        for j in num_s:
            if item.get(j[0]) == i:
                count = count + 1
                if count == 3:
                    break
                answer.append(j[0])
        count = 0
    return answer

genres = ["classic", "pop", "classic", "pop", "classic", "classic"]
plays = [400, 600, 150, 600, 500, 500]
print(solution(genres, plays))
