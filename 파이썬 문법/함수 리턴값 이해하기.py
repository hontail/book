def reverse(x,y,z):
    return x,y,z #xyz그대로 반환

ret = reverse(1,2,3) 
print(ret) #1,2,3 반환

r1, r2, r3 = reverse('a','b','c')#왜 a b c출력 r1,r2,r3에 각각 abc가 들어가는거 아닌가
print(r1); print(r2); print(r3)#언패킹(왼쪽변수에 ,를 사용하면 순서대로 값을 하나씩 넣기 때문)
