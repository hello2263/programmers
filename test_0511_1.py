#
# def solution(phone_book):
#     answer = True
#     phone_book = sorted(phone_book, key=len)
#     for i in range(0,len(phone_book)):
#         min_num = phone_book[i]
#         phone = [h[:len(min_num)] for h in phone_book]
#         phone.pop(i)
#         if min_num in phone:
#             answer = False
#             break
#     return answer
#
def solution(phone_book):
    answer = True
    phone_book = sorted(phone_book)
    count = 0
    for h in phone_book:
        min_num = h
        phone = h[:len(min_num)]
        if (phone == min_num ):
            count = count + 1
            if (count > 1):
                answer = False
    return answer


phone_book = ["123", "456", "789"]
print(solution(phone_book))
phone_book = ["119", "97674223", "1195524421"]
print(solution(phone_book))