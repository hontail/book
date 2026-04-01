from random import shuffle

listdata = list(range(1,11)) #1부타10까지 리스트를 만들어서 값 저장
for i in range(3): #0부터2까지 반복
    shuffle(listdata) #요소 섞기
    print(listdata) #출력하고 다시 섞기
