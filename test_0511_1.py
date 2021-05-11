
def solution(phone_book):
    answer = True
    phone_book = sorted(phone_book, key=len)
    for i in range(0,len(phone_book)):
        min_num = phone_book[i]
        phone = [h[:len(min_num)] for h in phone_book]
        phone.pop(i)
        if min_num in phone:
            answer = False
            break
    return answer
















