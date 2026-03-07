class MyClass:
    def sayHello(self): #안녕하세요 출력하는 함수
        print("안녕하세요")

    def sayBye(self, name):#매개변수다음에 보자 출력 
        print(f"{name}다음에 보자")
        
obj = MyClass() 
obj.sayHello()
obj.sayBye('철수')
