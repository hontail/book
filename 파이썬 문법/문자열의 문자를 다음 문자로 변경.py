text = input("문자열을 입력하세요") #키보드로 입력값을 문자열로 저장

ret = '' 
for i in range(len(text)): #입력한 길이만큼 반복
    if i != len(text)-1: #인덱스가 맨뒤랑 다르면 실행
        ret += text[i+1] #입력한 i+1번째 인덱스의 값을 저장
    else:
        ret += text[0] #0번째 인덱스 공백 저장

print(ret)
