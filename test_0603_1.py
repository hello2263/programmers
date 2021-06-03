def solution(brown, yellow):
    import math
    num = []
    block = brown + yellow - 4
    width_b = 2 * yellow
    height_b = 2 * 1
    if (brown == (width_b + height_b + 4)):
        answer = [yellow + 2, 3]
    elif ((block/4) == math.sqrt(yellow)):
        answer = [math.sqrt(yellow)+2, math.sqrt(yellow)+2]
    else:
        for i in range(1, yellow+1):
            if yellow % i == 0:
                num.append(i)
        while (1):
            x = num[0]
            y = num[-1]
            if (((brown-4)/2) == (x + y)):
                answer = [y+2, x+2]
                break
            else:
                num.remove(x)
                num.remove(y)
    return answer
