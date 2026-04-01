solarsys = ['태양','수성','금성','지구','화성','목성','토성','천왕성','해왕성']
ret1 = list(enumerate(solarsys)) #solatsys의 요소들을 인덱스랑 같이 저장
print(ret1)

for i,body in enumerate(solarsys): #요소,인덱스값을 i,body에 나눠서 저장
    print(f"태양계의 {i}번째 천체:{body}")
