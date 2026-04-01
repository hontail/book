numbers = [] 
for x in range(5):
    numbers.append(x)

numbers = [x for x in range(5)] 
numbers = [ x for x in range(5) if x % 2 == 0] #0부터5의 값을 만약 2로 나누어 떨어지면 x의 저장해
print(numbers)

#딕셔너리
my_dict = {}

my_dict["apple"] = 1
my_dict["banana"] = 2
my_dict["cherry"] = 3
print(my_dict)
print(my_dict["apple"]) 