listdata1 = [0,1,2,3,4]
listdata2 = [True,True,True]
listdata3 = ['',[],(),{},None,False]
print(all(listdata1)) #all은 리스트의 모슨 요소가 참일때만 True 하나라도 거짓이면 False
print(any(listdata1)) #any는 리스트의 요소가 1개라도 참이면 True 모든 요소가 거짓이면 False
print(all(listdata2))
print(any(listdata2))
print(all(listdata3))
print(any(listdata3))
#거짓은 정수0,빈 문자열 ' ', " ", 빈 리스트[],(),{}, None값
