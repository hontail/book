def countWord(filename,word): #파일이름,단어를 파라매터로 받음
    with open(filename,'r') as f: #파일이름 파라매터를 열어서 읽음
        text = f.read() #파일전체를 읽어서 변수에 저장
        text = text.lower() #파일 전체를 소문자로 다시 저장
        pos = text.find(word) #단어 파라매터를 파일전체에서 찾기
        count=0 #처음 카운드는 0
        while pos != -1: #찾는 단어가 파일에 없을때까지 반복 
            count += 1 #있을때마다 1씩증가
            pos = text.find(word,pos+1) #찾은 다음 단어위치부터 다시 찾기
    return count #총 갯수 리턴

word = input("mydata.txt에서 개수를 구할 단어를 입력하세요") #단어를 입력하면 문자열로 저장
word = word.lower() #저장한 문자열을 소문자로 다시 저장
ret = countWord('mydata.txt',word) #내가 입력한 단어를 함수에 넣고 출력값 저장
print('[%s]의 개수: %d'%(word,ret)) 
