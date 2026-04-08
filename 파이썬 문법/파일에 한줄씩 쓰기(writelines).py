count = 1 
data = [] #빈 리스트
print("파일에 내용을 저장하려면 애용을 입력하지 말고 Enter를 누르세요") 
while True: #나올때 까지 반복
    text = input(f"{count}파일에 저장할 내용을 입력하세요") 
    if text == '': #빈 데이터를 입력하면 입력 종료
        break
    data.append(text+'\n') #빈 데이터가 아니면 빈 data리스트에 값을 넣고 줄바꿈
    count += 1 #count에 1 증가하고 다시 텍스트 입력

f = open('myudata.text','w') #f는 mydata파일을 열어서 쓰기 모드
f.writelines(data) #1줄씩 쓰는거
f.close()
