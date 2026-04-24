mystack = [] #빈 리스트 생성

def putdata(data): #data를 파라매터로 받는 함수
    global mystack #함수 밖 mystack변수를 사용하겠다
    mystack.append(data) #빈 리스트에 파라매터를 추가

def popdata(): 
    global mystack
    if len(mystack) == 0: #만약 리스트가 비어 있다면 아무것도 반환하지 않고 종료
        return None
    return mystack.pop() #리스트가 뭐라도 있으면 맨 마지막를 지움

putdata('데이터1') #빈 리스트 mystack에 데이터1을 넣음
putdata([3,4,5,6]) #데이터1,[3,4,5,6]이 들어있음
putdata(12345) #데이터1,[3,4,5,6],12345들어있음

print('<스택상태>:',end='');print(mystack) #스택상태는 데이터1,[3,4,5,6],12345 출력

ret = popdata() #popdata()함수 실행 결과를 변수 ret에 넣음 처음은 12345가 ret에 저장됨
while ret != None: #ret이 비어있을때까지 popdata() 반복 처음 ret은 None값이 아니기 때문에 12345로 프린트문 실행
    print('스택에서 데이터 추출:',end='');print(ret) #마지막 12345부터 1개씩 추출
    print('<스택상태>:',end='');print(mystack) #추출 할때마다 출력
    ret=popdata() #12345를 제거한 popdata()실행값 [3,4,5,6]을 다시 ret변수에 저장 반복 None이면 종료
