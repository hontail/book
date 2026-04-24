url = 'http://news.naver.com/main/read,nhn?mode=LSD&mid=shm&sid1=105&oid=028&aid=0002334601'

tmp = url.split('?') #?로 나눠서 리스트에 저장 
queries = tmp[1].split('&') #queries변수는 &를 나눈걸 리스트에 저장
for query in queries:
    print(query)
