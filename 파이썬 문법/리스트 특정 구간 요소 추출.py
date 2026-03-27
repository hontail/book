solarsys = ['태양','수성','금성','지구','화성','목성','토성','천왕성','해왕성'] #행성 리스트
rock_planets = solarsys[1:4] #암석형 행성에 행성 리스트 1번 인덱스부터 4번째 전까지 저장 수성 ~ 지구
gas_planets = solarsys[4:] #가스형 행성에 행성 리스트 4번 인덱스 이후부터 저장 화성 ~ 해왕성
print("태양계에서 암석형 행성:", end="");print(rock_planets) #end는 줄변경 안 하고 이어서 출력
print('태양계에서 가스형 행성:', end="");print(gas_planets)
