url = 'http://www.naver.com/nes/today=20160831'
log = 'name:홍길동 age:17 sex:남자 nation:조선' 

ret1 = url.split('/')  #1칸 띄고 ''로 감싸서 출력
print(ret1)

ret2 = log.split() 
for data in ret2: #ret2을 반복해서 data변수 안에 넣을거야
    d1, d2 = data.split(':') #d1,d2에 data에 넣은값을 :로 나눠서 넣어
    print(f"{d1}->{d2}") #처음 name이 d1에 홍길동이 d2에 
