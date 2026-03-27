solarsys = ['태양','수성','금성','지구','화성','목성','토성','천왕성','해왕성','지구'] #행성 리스트
planet = '지구' #index('지구')를 해도 되지만 유지보수 측면에서 변수명으로 지정하는 게 더 좋은 코드
pos = solarsys.index(planet) #pos는 행성리스트에서 planet 인덱스를 저장
print('%s은(는) 태양계에서 %d번째에 위치하고 있습니다.'%(planet, pos))
pos = solarsys.index(planet,5) #pos는 행성리스트에서 planet을 인덱스 5이상에서 찾아서 저장 즉 9번째 지구 인덱스 출력
print('%s은(는) 태양계에서 %d번째에 위치하고 있습니다.' %(planet, pos))
