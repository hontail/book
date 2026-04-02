empty_set = set() #빈 set생성
print(empty_set)

list_to_set = set([1,2,3,3,2]) #list를 set으로 
print(list_to_set)

set_from_braces = {12,14,1,7}
print(set_from_braces)

string_to_set = set("Hello") #문자열을 set으로
print(string_to_set) #1개씩 출력

#셋에 원소추가
my_set = {1,5,3}
my_set.add(4) #4 추가
print(my_set)

my_set.update([5,6])
print(my_set)

#셋에 원소 제거
my_set = {1,2,3,4}
my_set.remove(2)#3제거, remove는 제거할 원소가 없으면 오류 발생
print(my_set)

my_set.add(2)
my_set.discard(3) #discard는 제거할 원소가 없어도 오류 발생 x
print(my_set)

my_set.clear() #set()모든 원소 제거
print(my_set)

#셋의 합집합
set1 = {1,2,3,}
set2 = {3,4,5}
union_set = set1.union(set2) #union_set변수에 set1 set2의 합집합 저장
print(union_set) #12345출력

set1 |= set2 #set1에 set2의 원소를 추가
print(set1)

#셋의 교집합
set1 = {1,2,3}
set2 = {3,4,5}
intersection_set = set1.intersection(set2) #set1과 set2의 교집합 저장
print(intersection_set)

set1 &= set2
print(set1)

#셋의 차집합
set1 = {1,2,3}
set2 = {3,4,5}
difference_set = set1.difference(set2) #
print(difference_set)

set1 = {1,2,3}
set1 -= set2 #set1에 set2와의 차집합을 저장 123 - 3빼면 1,2 
print(set1)
