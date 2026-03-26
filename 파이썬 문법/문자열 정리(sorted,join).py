strdata = input("정렬할 문자열을 입력하세요")
ret1 = sorted(strdata) #입력한 문자열 순서를 정리해줌
ret2 = sorted(strdata, reverse=True) #reverse가 뒤집으라는 뜻이고 True는 내림차순으로 하라는 뜻
                                        #sorted()랑 reverse=False랑 같은 오름차순으로 한다는 뜻
print(ret1)
print(ret2)
ret1 = ''.join(ret1) #공백없이 합치라는 뜻 ' '는 한칸 띄워서 연결
ret2 = ''.join(ret2) #공백없이 합치라는 뜻 
print('오른차순으로 정렬된 문자열은 <' + ret1 + '>입니다')
print('내림차순으로 정렬된 문자열은 <' + ret2 + '>입니다')
