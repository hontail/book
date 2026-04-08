f = open('stockcode.txt', 'r') #stockcode텍스트파일을 r읽기모드로 열어서 f에 저장
lines = f.readlines() #lines변수에 f에 저장한 파일을 1줄씩 읽고 리스트로 리턴
for line_num, line in enumerate(lines): #line_num,line에 1줄씩 저장한 리스트에서 꺼내서 저장
    print(f"{line_num+1}{line},end=''") #저장한 line_num, line출력
f.close()
