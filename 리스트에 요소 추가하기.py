listdata = [] #빈 리스트 생성
for i in range(3): #0부터3까지 i에 1개씩 넣어서 반복
    txt = input("리스트에 추가할 값을 입력하세요[%d/3]:"%(i+1))#3번 입력,하면 [1/3] > [2/3] > [3/3]몇번입력했는지 숫자가 올라감
    listdata.append(txt) #txt에 저장된 입력한 값들을 빈 리스트에 추가
    print(listdata)#입력한 값들을 3번 출력
