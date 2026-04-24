url = 'http://news.naver.com/main/read,nhn?mode=LSD&mid=shm&sid1=105&oid=028&aid=0002334601' #url저장

tmp = url.split('/') #url을 /로 나눠서 tmp에 저장
domain = tmp[2] #2번 인덱스 news.naver.com
print(domain) #도메인만 출력
