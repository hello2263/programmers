def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 3, reverse=True) #현재 문자열을 정렬하기에 x*3을 하여 문자열을 늘린다음 한자리씩 비교를하여 정렬
    answer = ""
    for n in numbers:
        answer = answer + str(n)
    return str(int(answer))

