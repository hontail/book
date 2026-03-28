solarsys = ["태양",'수성','금성','지구','화성','목성','토성','천왕성','해왕성']#태양계 리스트 생성
pos = solarsys.index('목성') #변수 pos에 태양계 리스트에 있는 '목성'의 인덱스값 저장 = 5
solarsys.insert(pos,'소행성') #5번인덱스에 소행성을 삽입
print(solarsys)
