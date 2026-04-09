spos = 105 
size = 500

f = open('stockcode.txt', 'r') #stockcode텍스트 파일을 읽기 모드로 열기
h = open('stockcode_part.txt', 'w') #쓰기 모드로 읽기

f.seek(spos) #105비트 위치를 찾아
data = f.read(size) #찾은 105비트 위치에서 부터 500비트만큼 읽어서 data변수에 저장해 650비트까지
h.write(data) 

h.close()
f.close()