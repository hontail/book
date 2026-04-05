f = lambda x:x*x #변수 f에 인자를 제곱해서 리턴하는 식을 저장?
args = [1,2,3,4,5] #리스트 생성
ret = map(f, args) #
print(list(ret))
