
def solution(phone_book):
    answer = True
    j = 0
    phone_book = sorted(sorted(phone_book, key=len))
    for i in range(0, len(phone_book)):
        min_num = phone_book[i]
        j = j + 1
        if (j >= len(phone_book)):
            break
        phones = phone_book[j]
        phone = phones[:len(min_num)]
        if min_num in phone:
            answer = False
            break
    return answer


