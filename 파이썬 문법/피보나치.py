memo = {1: 1, 2: 1} #딕셔너리 형태로 값을 저장

def pibonachi(n): 
    if n in memo: #메모에 n이 있으면 memo[n]값을 리턴
        return memo[n]
    else:
        memo[n] = pibonachi(n-1) + pibonachi(n-2) #메모에 n이 들어있지않으면 재귀함수 호출
        return memo[n] #호출한 함수 memo[n]에 저장

for i in range(1,51): #1부터 50까지 i에 1씩 증가해서 저장
    print(pibonachi(i)) #1,2는 메모에 처음 값이 1로 저장되어 있음 
