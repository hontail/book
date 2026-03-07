class MyClass:
    var = '안녕하세요'
    def sayHello(self):
        param1 = '안녕'
        self.param2 = '하이'
        print(param1)
        print(self.var)
#MyClass함수에 '안녕하세요'가 들어간 var 변수,sayHello함수가 들어있고
#sayHello함수는 '안녕'이 들어간 param1변수, param2에는
#print(param1)은 '안녕'출력
#print(self.var)

obj = MyClass() #obj변수에 MyClass클래스 저장 질문 여기서 왜 클래스 이름을 안적었지 적어야하는거 아닌가
print(obj.var) #'안녕하세요'출력
obj.sayHello() #
#obj.param1
