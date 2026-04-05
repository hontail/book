expr1 = '2+3'
expr2 = 'round(3.7)' #round()는 반올림 하는 내장함수

ret1 = eval(expr1) #eval은 문자열을 실행하는 함수?
ret2 = eval(expr2) 

print(f"{expr1}을 eval()로 실행한 결과: {ret1}")
print(f"{expr2}을 eval()로 실행한 결과: {ret2}")
