def solution(begin, target, words):
    use = []
    for i in begin:
        use.append(i)
    answer = 0
    return answer
begin = "hot"
target = "cog"
count = 0
sum = 0
start = ""
begin1 = list(begin)
words = ["dot", "dog", "lot", "log", "cog"]
while(start != target):
    for i in range(0, len(words)):
        for j in range(0, len(begin1)):
            if(begin1[j] == words[i][j]):
                sum = sum + 1
        if (sum == (len(begin1)-1)):
            start = words[i]
            sum = 0
            break
    words.pop(start)


