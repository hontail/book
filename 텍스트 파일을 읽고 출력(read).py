f = open('stockcode.txt','r') #stockcode라는 텍스트 파일을 열어라, 읽기모드로
data = f.read #data변수에 
print(data)
f.close()
