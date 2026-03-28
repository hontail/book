listdata = list(range(5)) #0부터5까지 리스트 생성
ret1 = reversed(listdata) #리스트 역순으로 저장
print('원본 리스트',end="");print(listdata) #0부터5까지 출력
print('durtns 리스트',end="");print(list(ret1)) #5부터 0까지 출력

ret2 = listdata[::-1] #0부터5까지 리스트 역순으로 저장
print('슬라이싱 이용',end='');print(ret2) #5부터 0까지 출력
#reversed는 reverse와 달리 원본 데이터를 변경하지 않는다
