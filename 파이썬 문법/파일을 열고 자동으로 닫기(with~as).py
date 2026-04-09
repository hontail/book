with open('stockcode.txt', 'r') as f: #stockcode텍스트 파일을 f라는 변수 이름으로 열어서 실행
    for line_num, line in enumerate(f.readlines()): #f에 저장한 stocktext파일을 1줄씩 번호를 매겨서 각각 line_num, line으로 저장
        print(f"{line_num},{line},end=''") #줄의 번호랑 줄의 내용을 출력
