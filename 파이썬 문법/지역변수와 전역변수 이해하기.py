param = 10
strdata = '전역변수'

def func1():
    strdata = '지역변수'
    print(strdata)

def func2(param):
    param = 1

def func3():
    global param
    param = 50

func1() #지역변수
print(strdata) #전역변수
print(param) #10
func2(param) #출력없음 print가 없어서 param에 1이 들어감
print(param) #10 
func3() #출력없음 print가 없어서
print(param) #50
