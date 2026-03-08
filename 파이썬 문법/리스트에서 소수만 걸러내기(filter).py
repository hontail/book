def getPrime(x): 
    if x%2 == 0: #만약 파라매터 x를 2로 나눈 나머지가 0이면 실행
        return #그냥 return만 있으면 그냥 종료하라는 뜻
    
    for i in range(3, int(x/2),2): #3부터 x를 2로 나눈 몫까지 2를 더하면서 i에 저장 반복
        if x%i == 0: #만약 x를 i로 나눈 나머지가 0이면 종료
            break
    else: #만약 x를 i로 나눈 나머지가 0이 아니면 x반환
        return x
    
listdata = [117,119,1113,11113,11119]
ret = filter(getPrime, listdata) #ret변수에 listdata의 값을 getPrime함수를 돌려서 값을 반한
print(list(ret)) #반환받은 값의 리스트를 출력

#5번째 줄 보충
#x가 15면 3부터 7까지 2를 더하면서 i에 넣으라는거 3 , 5가 됨
