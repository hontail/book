add = lambda x,y: x+y #람다식 x,y를 사용해서 x+y를 리턴
ret = add(1,3) #인자 1,3은 각각 x,y에 들어감
print(ret) 

funcs = [lambda x: x+'.pptx', lambda x: x+'.docx'] #func의 리스트는 2개 처음 인덱스는 .pptx를 붙고 두번째 인덱스 뒤에 .docx를 받아 저장
ret1 = funcs[0]('intro') #funcs는 리스트형 0번 인덱스에 intro저장 .pptx가 붙음
ret2 = funcs[1]('Report') #1번 인덱스에 Report를 저장, .docx가 붙음
print(ret1) #intro.pptx
print(ret2) #intro.docx

names = {'Mary':10999,'Sams':2111,'Aimy':9778,'Tom':20245,'Michale':27115} #딕셔너리 키는 영문 값은 정수로 저장

ret3 = sorted(names.items(),key=lambda x:x[0]) #sorted는 원본은 두고 새로 만들고 바꿔서 정렬, items()내장 함수는 키,값 1쌍을 튜플로 추출 x는 튜플 한 쌍을 의미 
print(ret3)
