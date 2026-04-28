from random import shuffle

male = ['슈퍼맨','심봉사','로미오','이몽룡','마루치']
female = ['원더우먼','빵덕','줄리엣','성춘향','아라치']
shuffle(male) #male리스트 섞기
shuffle(female) #female리스트 섞기
couples = zip(male,female) #인자들을 1쌍으로 묶어서 리턴 한쪽이 적으면 적은쪽이 기준 즉 shuffle하고 0번인덱스끼리,1번인덱스끼리 묶는것

for i, couple in enumerate(couples): #1쌍으로 묶은 것을 인덱스는 i,값은 couple변수에 저장
    print("커플%d:[%s]-[%s]"%(i+1,couple[0],couple[1])) #1쌍은 튜플형태로 저장 되는데 0번 인덱스는 남자, 1번 인덱스는 여자
