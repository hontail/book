names = {'Mary':10999,'Sams':2111, 'Aimy':9778, 'Toms':20245,'Michale':27115,'Bobs':5887,'Kelly':7855 }
ks = names.keys() #names딕셔너리에서 .key()로 키값만 ks에 저장
print(ks) #10999~~7855

for k in ks: #변수 ks에서 1개씩 꺼내서 k에 저장
    print('Key:%s\tValue:%d'%(k,names[k])) #Key:k 이때 k는 문자열 정수가 아님 탭누르고 names에서 값만 추출
