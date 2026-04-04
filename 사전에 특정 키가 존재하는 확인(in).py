names = {'Mary':10999,'Sams':2111, 'Aimy':9778, 'Tom':20245,'Michale':27115,'Bob':5887,'Kelly':7855 }
k = input("이름을 입력하세요:")
if k in names:
    print(f"이름이 {k}인 출생아 수는 {names[k]}먕입니다.")
    
else:
    print(f"자료에 이름이 {k}인 출생아는 없습니다.")
    