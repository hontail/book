text = input("파일을 입력하세요") #아무거나 입력
f = open("mudata.txt", 'w') #변수 f는 mydata파일을 열어서 쓸거임
f.write(text) #f에 입력한 text를 쓰기
f.close()
