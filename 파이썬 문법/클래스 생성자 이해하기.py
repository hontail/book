class MyClass:
    def __init__(self): #인자에 안녕하세요 저장하고 print문 출력
        self.var = '안녕하세요'
        print('MyClass인스턴스 객체가 생성되었습니다')
    
obj = MyClass() 
print(obj.var)
