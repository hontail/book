text = input("문장을 입력하세요") 

ret = '' #ret은 비어있음 만약 엔터로 띄면 공백이 들어있는거임
for i in range(len(text)): #입력한 문장 길이만큼 반복
    if i != len(text)-1: #문장 길이 -1 만큼은 ret에 반복에서 저장 
        ret += text[i+1] #문자열 연결해서 저장
    else: #처음단어를 마지막에 붙힘
        ret += text[0]

print(ret) 
