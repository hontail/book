class MyClass:
    var = "안녕하세요"
    def sayHello(self): #self뒤에 "안녕하세요" 출력
        print(self.var)

obj = MyClass()
print(obj.var)#"안녕하세요 출력" var임
obj.sayHello()#self.var출력
