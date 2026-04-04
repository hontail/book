names = {'Mary':10999,'Sams':2111, 'Aimy':9778, 'Tom':20245,'Michale':27115,'Bob':5887,'Kelly':7855 }
vals = names.values() #names딕셔너리에서 .values()로 값만 vals에 저장
print(vals) #Mary,Sams ... 

vals_list = list(vals) #변수 vals_list에 값들을 리스트형태로 저장
ret = sum(vals_list) #변수 ret은 vals_list에 저장한 값들을 다 더하라는 뜻
print('출생아 수 총계:%d'%ret) #총 합계를 출력
