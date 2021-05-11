
def solution(clothes):
    count = {}
    item = 0
    sum = 0
    cos = 1
    for i in clothes:
        if (count.get(i[1]) != None):
            count[i[1]] = count[i[1]] + 1
        else:
            count[i[1]] = 1
    for num in count.values():
        item = item + 1
        sum = sum + num
        cos = cos * num
    if item == 1:
        cos = 0
    answer = sum+cos

    return answer


clothes = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["soky_makeup", "fce"], ["soky_maeup", "fce"]]
print(solution(clothes))
