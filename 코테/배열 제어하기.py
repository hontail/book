#정수 배열을 하나 입력 받고 중복값 제거 내림차순으로 정렬해서 반환하는 sloution()함수

a = [] #빈 리스트 생성
for i in range(int(input())): #몇번 반복할지 입력
    b = int(input()) #리스트 안에 넣을 값 1개씩
    a.append(b) #리스트에 입력한 값이 들어감

def solution(): #파라매터 변수를 지정 안 하면 a리스트만 해서 실용성이 떨어짐 나중에 수정 핧 것
    a = list(set(a)) #리스트에 넣은 값들 중복 제거
    a.sort(reverse = True) #e리스트에 넣은 값들 내림차순으로 정렬
    return a

print(solution()) #
