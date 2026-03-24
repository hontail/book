def sum_digits(n):
    # 여기에 코드를 작성하세요
    a = 0
    while a < 10:
        i = 1
        a = n/(10 ** int(len(n)-i))
        i + 1
        a += a
    
        return a
# 테스트 코드
print(sum_digits(22541))
print(sum_digits(92130))
print(sum_digits(12634))
print(sum_digits(704))
print(sum_digits(3755))
