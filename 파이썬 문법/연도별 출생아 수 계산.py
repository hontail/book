def countBirths(): 
    ret = [] #빈 리스트
    for y in range(1880,2016): #1880년생 부터 2015년생까지
        count = 0 
        filename = 'names/yob%d.txt'%y #파일 이름은 names/yob년도.txt
        with open(filename,'r') as f: #년도 파일을 읽기 모드로 열기
            data = f.readlines() #data변수에 각 년도파일을 1줄씩 저장
            for d in data: #data파일에 줄갯수 만큼 만복
                if d[-1] == '\n': #마지막 줄이 엔터로 끝나면 엔터 전까지 변수 d에 저장
                    d = d[:-1]
                
                birth = d.split(',')[2] #d에 저장한 data를 ,를 기준으로 나눈 3번 인덱스를 변수에 저장
                count += int(birth) 
            ret.append((y,count)) #빈 리스트에 년도,출생아 수 합 추가
        return ret #각 년도, 총 출생아 수 리턴
    
result = countBirths() #함수 실행결과를 변수에 저장
with open("birth_by_year.csv",'w') as f: 
    for year,birth in result: 
        data = '%s,%s\n' %(year,birth)
        print(data)
        f.write(data)
