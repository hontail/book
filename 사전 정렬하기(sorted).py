names = {'Mary':10999,'Sams':2111, 'Aimy':9778, 'Tom':20245,'Michale':27115,'Bob':5887,'Kelly':7855 }
ret1 = sorted(names) #names사전을 정리해서 ret1에 저장 키값만
print(ret1) #

def f1(x):   #f1은 파라매터로 리스트를 받고 0번 인덱스 리턴
    return x[0]

def f2(x):  
    return x[1]

ret2 = sorted(names.items(),key=f1) #ret2는 names사전의 키,값들을 정렬, key값의 인덱스?
print(ret2)

ret3 = sorted(names.items(),key=f2)
print(ret3)

ret4 = sorted(names.items(), key=f2, reverse=True)
print(ret4)
