with open('mydata.txt','r') as f: #mydata텍스트파일 열어서 읽기
    data = f.read() #텍스트파일 내용을 data변수에 저장
    tmp = data.split() #공백을 기준으로 나눠서 tmp에 저장 단어별로 저장
    print("단어수:[%d]"%len(tmp))
