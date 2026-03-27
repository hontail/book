solarsys = ['태양','수성','금성','지구','화성','목성','토성','천왕성','해왕성'] #행성 리스트
planet = '화성' 
pos = solarsys.index(planet) #pos에 planet인덱스 값 저장
solarsys[pos] = 'Mars' #solarsys리스트에 4번째 인덱스 값에 Mars 저장
print(solarsys)
